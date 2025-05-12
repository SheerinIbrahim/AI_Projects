import random
import cv2
import time
from HandTrackingSheerin import handDetector as htm
from playsound import playsound
import threading


class Balloon:
    def __init__(self, width, height):
        self.x = random.randint(100, width - 100)
        self.y = random.randint(150, height - 100)
        self.radius = 20
        self.color = (random.randint(0, 255),
                      random.randint(0, 255),
                      random.randint(0, 255))
        self.popped = False
        self.speed = random.randint(1, 3)

    def draw(self, frame):
        if not self.popped:
            self.y -= self.speed
            cv2.circle(frame, (self.x, self.y), self.radius, self.color, -1)

    def check_collision(self, finger_x, finger_y):
        if not self.popped:
            distance = ((self.x - finger_x) ** 2 + (self.y - finger_y) ** 2) ** 0.5
            if distance < self.radius:
                self.popped = True
                return True
        return False

    def is_off_screen(self):
        return self.y + self.radius < 0


class BalloonGame:
    def __init__(self):
        self.detector = htm()
        self.cap = cv2.VideoCapture(0)
        if not self.cap.isOpened():
            print("Cannot open camera")
            exit()

        self.balloons = []
        self.is_paused = False
        self.palm_open_last_frame = False
        self.score = 0
        self.last_toggle_time = 0
        self.start_time = time.time()
        self.game_duration = 60  # seconds

    def position_values(self, positionList, list_values):
        x_pos = [positionList[x][1] for x in list_values]
        y_pos = [positionList[x][2] for x in list_values]
        return x_pos, y_pos

    def play(self):
        while True:
            ret, frame = self.cap.read()
            if not ret:
                print("Can't receive frame. Exiting...")
                break
            frame = cv2.flip(frame, 1)

            frame = self.detector.findHands(frame)
            positionList = self.detector.findPosition(frame)

            elapsed_time = time.time() - self.start_time

            # Game Over Check
            if elapsed_time > self.game_duration:
                cv2.putText(frame, f"Game Over! Score: {self.score}", (100, 200),
                            cv2.FONT_HERSHEY_SIMPLEX, 1.2, (255, 0, 0), 3)
                cv2.imshow("Balloon Pop", frame)
                if cv2.waitKey(3000) & 0xFF == ord('q'):
                    break
                self.reset_game()
                continue

            if positionList:
                finger_x, finger_y = self.position_values(positionList, [8])

                # Detect Open Palm
                x_pos, y_pos = self.position_values(positionList, [4, 8, 12, 16, 20])
                _, compy = self.position_values(positionList, [3, 6, 10, 14, 18])
                is_open = [y_pos[i] < compy[i] for i in range(5)]

                if all(is_open):
                    if not self.palm_open_last_frame and time.time() - self.last_toggle_time > 1:
                        self.is_paused = not self.is_paused
                        self.last_toggle_time = time.time()
                        print("Paused" if self.is_paused else "Resumed")
                    self.palm_open_last_frame = True
                else:
                    self.palm_open_last_frame = False

                if not self.is_paused:
                    new_balloons = []
                    for balloon in self.balloons:
                        if not balloon.popped and not balloon.is_off_screen():
                            balloon.draw(frame)
                            if balloon.check_collision(finger_x[0], finger_y[0]):
                                threading.Thread(target=playsound, args=("pop.mp3",), daemon=True).start()
                                new_balloons.append(Balloon(frame.shape[1], frame.shape[0]))
                                self.score += 1
                            else:
                                new_balloons.append(balloon)
                        else:
                            new_balloons.append(Balloon(frame.shape[1], frame.shape[0]))
                    self.balloons = new_balloons
                else:
                    cv2.putText(frame, "PAUSED", (frame.shape[1] // 2 - 100, frame.shape[0] // 2),
                                cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 4)

                # Draw score
                cv2.putText(frame, f"Score: {self.score}", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)
                cv2.putText(frame, f"Time Left: {int(self.game_duration - elapsed_time)}s", (20, 90),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (155, 55, 100), 2)

            else:
                cv2.putText(frame, "Show your hand to play", (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

            cv2.imshow('Balloon Pop', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.cap.release()
        cv2.destroyAllWindows()

    def reset_game(self):
        self.balloons = [Balloon(640, 480) for _ in range(random.randint(5, 15))]
        self.score = 0
        self.is_paused = False
        self.palm_open_last_frame = False
        self.start_time = time.time()


if __name__ == '__main__':
    game = BalloonGame()
    game.reset_game()
    game.play()
