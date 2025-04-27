# Gesture-Based Brightness Control 🎚️🖐️

This project uses hand gesture recognition to control the system's screen brightness via the webcam. The distance between the thumb and index finger, detected through hand tracking, is mapped to adjust the screen brightness in real-time. The project is developed in Python using OpenCV, MediaPipe, and the screen_brightness_control library for managing screen brightness.

The system captures hand gestures from the webcam feed, calculates the distance between the thumb and index finger, and adjusts the brightness based on that distance. The closer the thumb and index finger are, the dimmer the screen, and the farther apart, the brighter the screen becomes.

## Features

- Real-time hand gesture detection

- Volume control via hand gestures

- Interactive graphical interface showing current volume

- Works in real-time with a webcam feed

## Technologies Used

- Python: The programming language used to develop the project.

- OpenCV: A computer vision library for real-time image processing.

- MediaPipe: A framework for building multimodal applied ML pipelines for hand tracking.

- PyAudio: A library for audio processing (used internally by pycaw).

- PyCaw: A Windows audio library for controlling system volume.

- NumPy: A package for scientific computing, used here for handling numerical operations like interpolation.

- HandTrackingSheerin: A custom Python package used for hand tracking and gesture recognition (uploaded to PyPI).

- Math: For calculating the distance between the thumb and index finger.

## Installation

Clone this repository to your local machine:

	git clone https://github.com/SheerinIbrahim/GestureBasedVolumeControl.git

Navigate to the project directory:

	cd GestureBasedVolumeControl

Install the dependencies from the requirements.txt:

	pip install -r requirements.txt

## Usage

To run the gesture-based volume control system:

- Ensure you have a webcam connected to your system.

- Execute the following command:

		python main.py

This will open the webcam feed, and as you move your hand, the volume will adjust based on the distance between your thumb and index finger.

Press 'q' to quit the webcam feed.
