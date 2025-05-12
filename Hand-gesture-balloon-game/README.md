# 🎈 PalmPop - Hand Gesture Balloon Game

PalmPop is an interactive OpenCV-based game where you pop balloons using hand gestures detected via your webcam! Raise your palm to pause the game, and use your index finger to pop floating balloons. Great for experimenting with computer vision and real-time gesture control.

## 📸 Features

- 🎯 Pop balloons using your fingertip
- ✋ Raise your palm to pause/resume
- 🎨 Randomized balloon colors and float speeds
- 🔊 Sound effects when popping balloons
- 🤖 Built with OpenCV and MediaPipe for hand detection

## 🛠 Requirements

- Python 3.7+
- Webcam

Install dependencies using:

```bash
pip install -r requirements.txt
```

## 🚀 Getting Started

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/palmpop.git
cd palmpop
```

2. **Add your pop sound**
Place your `pop.mp3` file inside a `sounds/` directory:
```
palmpop/
├── main.py
├── HandTrackingSheerin.py
├── sounds/
│   └── pop.mp3
```

3. **Run the game**
```bash
python main.py
```

## 📁 File Structure

- `main.py` – Main game loop
- `HandTrackingSheerin.py` – Hand detection module
- `requirements.txt` – Python dependencies
- `sounds/pop.mp3` – Balloon popping sound

## 💡 Controls

- **New Game**: Move finger over green "New Game" button
- **Pause/Resume**: Hold open palm in view

## 🧠 Credits

- Built with [OpenCV](https://opencv.org/) and [MediaPipe](https://mediapipe.dev/)
- Sound from [freesound.org](https://freesound.org/) or generated manually

## 📜 License

This project is open-source under the MIT License.