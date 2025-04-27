Gesture-Based Volume Control 🎚️🖐️
A Python project that controls your system volume by detecting hand gestures using your webcam!
Move your thumb and index finger closer or farther to decrease or increase the volume dynamically.
Built with OpenCV, MediaPipe, PyCaw, and hand tracking modules.

📸 Demo
(You can add a GIF or screenshot here showing the app in action!)

📂 Project Structure
bash
Copy
Edit
GestureBasedVolumeControl/
├── main.py                # Main file to run the application
├── requirements.txt       # List of required Python libraries
├── HandTrackingSheerin/   # Custom hand tracking module
└── README.md              # Project description (this file)
🛠️ Technologies Used
Python 3.8+

OpenCV – for video capture and drawing

MediaPipe – for real-time hand tracking

NumPy – for mathematical operations

PyCaw – to control system audio (Windows only)

Math – for distance calculation between fingers

comtypes – for COM interface with system volume

✨ Features
Detects hand landmarks in real-time using your webcam.

Measures the distance between thumb and index fingertips.

Dynamically maps the distance to volume percentage (0–100%).

Visual feedback:

Circle on thumb and index finger.

Line between fingers.

Volume bar showing current volume.

Real-time FPS displayed on the screen.

Smooth volume control without any physical contact with your system!

🔥 How It Works
Hand Detection:
Using HandTrackingSheerin, your hand is detected, and landmarks (points on fingers) are identified.

Distance Calculation:
The distance between the tip of the thumb (id=4) and the tip of the index finger (id=8) is calculated using the Pythagoras theorem (math.hypot).

Volume Mapping:
The measured distance (between 40 to 200 pixels) is mapped to a volume range (0% to 100%) using numpy.interp().

Volume Adjustment:
Volume is updated in real-time through PyCaw, directly controlling your Windows system volume.

Visual Interface:
Real-time drawing on webcam feed — finger positions, connection line, volume percentage, and a dynamic volume bar.

🚀 Getting Started
1. Clone the repository
bash
Copy
Edit
git clone https://github.com/your-username/GestureBasedVolumeControl.git
cd GestureBasedVolumeControl
2. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
Or install individually:

bash
Copy
Edit
pip install opencv-python mediapipe pycaw comtypes numpy
3. Run the Project
bash
Copy
Edit
python main.py
📜 Requirements
Operating System: Windows (PyCaw is Windows-specific)

Python: 3.8 or higher

Webcam: Internal or external webcam required

⚡ Controls
Bring thumb and index finger close → Volume decreases

Move thumb and index finger apart → Volume increases

Press 'q' → Exit the application

📋 Notes
The project uses a custom hand tracking module (HandTrackingSheerin) based on MediaPipe for detecting hands.

The volume bar and percentage provide visual feedback for better interaction.
Accuracy may depend on lighting conditions and webcam quality.

🎯 Future Improvements
Add volume mute with specific gesture (e.g., closed fist ✊).

Add gesture calibration for different users.

Make it cross-platform (support macOS/Linux).

Add support for media controls (play/pause/next/previous).
