# Real-Time-Pushup-Detector
Pushup Detector: A Customizable AI Athlete Analyzer

**Introduction:**

The Pushup Detector project is an AI model designed to analyze an athlete's actions based on a camera feed. What sets this project apart is its adaptability, allowing users to calibrate it according to their needs. 

**Key Features:**

- **User Calibration:** The project lets you customize its detection and tracking sensitivity using key inputs.

**Prerequisites:**

- Python version: Python 3.9.5

- OpenCV (cv2) library: opencv-contrib-python==4.5.5.62 opencv-python==4.6.0.66 cv2imshow==0.10 cvzone==1.4.1

- Mediapipe library: mediapipe==0.10.1

**Installation:**

1. Clone this repository to your local machine.

2. Install the required dependencies by running the following command: `pip install opencv-python mediapipe`

**Usage:**

1. Connect a camera device to your computer.

2. Run the `pushup_detector.py` script: `python pushup_detector.py`

3. The camera window will open, displaying the camera feed.

4. Perform pushups or other skills in front of the camera.

5. The output will be shown on the camera window, either "PUSHUP" if performing pushups or "NOT A PUSHUP" for other skills.

**Calibration:**

- To adjust detection and tracking sensitivity, use the keys provided in the project.

**Notes:**

- Ensure that the camera is properly positioned and has a clear view of the athlete.

- Press 'q' to quit and exit the program.
- Press 'i' to increase the angle.
- Press 'd' to decrease the angle.

Enjoy customizing it to your needs! If you have any questions or need further assistance, please feel free to reach out.

**Happy Analyzing!**
