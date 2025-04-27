# Gesture-Based Volume Control 🎚️🖐️

This project uses hand gesture recognition to control the system's volume using the webcam. It leverages computer vision techniques to detect hand gestures and maps the distance between the thumb and index finger to control the volume. The project is built using Python, OpenCV, MediaPipe, and PyAudio, with additional integration for volume control using the pycaw library for Windows.

The system uses the webcam to detect hand positions, and based on the distance between the thumb and index finger, it adjusts the system volume. When the distance is small, the volume is set low, and as the distance increases, the volume increases accordingly.

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

	git clone https://github.com/SheerinIbrahim/AI_Projects.git

Navigate to the project directory:

	cd AI_Projects/Gesture_based_volume_control

Install the dependencies from the requirements.txt:

	pip install -r requirements.txt

## Usage

To run the gesture-based volume control system:

- Ensure you have a webcam connected to your system.

- Execute the following command:

		python main.py

This will open the webcam feed, and as you move your hand, the volume will adjust based on the distance between your thumb and index finger.

Press 'q' to quit the webcam feed.
