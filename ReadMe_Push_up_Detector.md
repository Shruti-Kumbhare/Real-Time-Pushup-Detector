Pushup Detector
This project implements an AI model, the Pushup Detector, which analyzes the actions of an athlete based on the camera feed. The model can detect whether the athlete is performing pushups or any other skill and display the corresponding label.

Acknowledgment
This project is based on the code from the following GitHub repository: Link to Repository

Prerequisites
Python version:
Python 3.9.5

OpenCV (cv2) library:
opencv-contrib-python==4.5.5.62
opencv-python==4.6.0.66
cv2imshow==0.10
cvzone==1.4.1

Mediapipe library:
mediapipe==0.10.1

Installation
Clone this repository to your local machine.

Install the required dependencies by running the following command:
pip install opencv-python mediapipe

Usage
Connect a camera device to your computer.
Run the pushup_detector.py script:
python pushup_detector.py

The camera window will open, displaying the camera feed.
Perform pushups or other skills in front of the camera.

The output will be shown on the camera window. If you are performing pushups, it will display "PUSHUP." If you are performing any other skill, it will display "NOT A PUSHUP."

Notes
Ensure that the camera is properly positioned and has a clear view of the athlete.
Adjust the min_detection_confidence and min_tracking_confidence parameters in the code to control the detection and tracking sensitivity.
Press 'q' to quit and exit the program.

Additional Information
This project utilizes the Mediapipe library for pose estimation and OpenCV for image processing and visualization.

Acknowledgments
This project was completed as part of a pre-screening short assignment for an Artificial Intelligence internship opportunity. 
Good luck with your project! If you have any questions or need further assistance, please feel free to reach out.
