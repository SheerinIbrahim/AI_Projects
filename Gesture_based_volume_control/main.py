from HandTrackingSheerin import handDetector as htm
import cv2
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import time
import math
import numpy as np

# Windows volume control
def set_volume_to(volume_level):

    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = interface.QueryInterface(IAudioEndpointVolume)

    if volume_level=='mute':
        volume.SetMute(1,None)

    elif isinstance(volume_level, int):
        volume_level = max(0, min(volume_level, 100))
        scaled_value = volume_level/100
        volume.SetMasterVolumeLevelScalar(scaled_value, None)

# Open webcam feed
def volume_control():

    detector = htm()
    cap =cv2.VideoCapture(0)
    pTime = 0

    if not cap.isOpened():
        print("Cannot open camera")
        exit()

    while 1:
        # Read frame-by-frame
        ret, frame = cap.read()

        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break

        frame = detector.findHands(frame)
        positionList = detector.findPosition(frame)

        if positionList:

            frame = detector.drawCircle(img = frame,idNo = 4)
            frame = detector.drawCircle(img = frame, idNo = 8)
            thumbx, thumby = positionList[4][1],positionList[4][2]
            indexx, indexy = positionList[8][1],positionList[8][2]
            colour = (134,62,250)
            cv2.line(frame,(thumbx,thumby),(indexx,indexy),colour,5)
            distance = math.hypot(indexx - thumbx, indexy - thumby)
            mapped_distance = int(np.interp(distance,[40,200],[0,100]))
            set_volume_to(mapped_distance)
            vol = int(np.interp(100-mapped_distance,[0,100],[200,400]))

            cv2.rectangle(frame, (70,200),(100,400),(255,200,240),3)
            cv2.rectangle(frame, (70,vol),(100,400),(155,100,140),cv2.FILLED)
            cv2.putText(frame, (str(mapped_distance)+" %"), (60, 180), cv2.FONT_HERSHEY_PLAIN, 2, (15, 150, 155), 3)
            #print(mapped_distance, vol)

        # Display fps
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(frame, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (190, 100, 150), 3)

        # Show the frame in a window
        cv2.imshow('Camera Feed', frame)

        # Press 'q' to quit the window
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close window
    cap.release()
    cv2.destroyAllWindows()



if __name__ == "__main__":
    volume_control()
