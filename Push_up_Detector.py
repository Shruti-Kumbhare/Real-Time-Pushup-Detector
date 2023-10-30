
import cv2
import mediapipe as md

md_drawing = md.solutions.drawing_utils
md_drawing_styles = md.solutions.drawing_styles
md_pose = md.solutions.pose

count = 0
position = None

cap = cv2.VideoCapture(0)  # captures the video

# Ask the user for the angle thresholds
# down_threshold = int(input("Enter the threshold for 'down' position: "))
# up_threshold = int(input("Enter the threshold for 'up' position: "))


# Initialize the angle thresholds
down_threshold = 15
up_threshold = 5

with md_pose.Pose(
        min_detection_confidence=0.7,
        min_tracking_confidence=0.7) as pose:
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("empty camera")  # prints empty camera and exits the camera window.
            break
        image = cv2.flip(image, 1)
        # image=cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        result = pose.process(image)
        imlist = []
        if result.pose_landmarks:
            md_drawing.draw_landmarks(
                image, result.pose_landmarks, md_pose.POSE_CONNECTIONS)
            for id, im in enumerate(result.pose_landmarks.landmark):
                h, w, _ = image.shape
                X, Y = int(im.x * w), int(im.y * h)
                imlist.append([id, X, Y])

            if len(imlist) != 0:
                # calculates the angle to determine the position
                if ((imlist[12][2] - imlist[14][2]) >= down_threshold and (imlist[11][2] - imlist[13][2]) >= down_threshold):
                    position = "down"
                if ((imlist[12][2] - imlist[14][2]) <= up_threshold and (imlist[11][2] - imlist[13][2]) <= up_threshold) and position == "down":
                    count = count + 1
                    # for displaying text on the image
                    cv2.putText(image, "No Push-up", (image.shape[1] - 600, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, bottomLeftOrigin=False)
                else:
                    cv2.putText(image, "Push-up", (image.shape[1] - 600, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, bottomLeftOrigin=False)

        cv2.imshow("Push-up counter", image)  # displays camera window
        key = cv2.waitKey(1)
        if key == ord('q'):  # press q to exit the camera window.
            break
        
        # Press 'd' to decrease the angle thresholds
        if key == ord('d'):
            down_threshold -= 1
            up_threshold -= 1
        
        # Press 'i' to increase the angle thresholds
        if key == ord('i'):
            down_threshold += 1
            up_threshold += 1

cap.release()
