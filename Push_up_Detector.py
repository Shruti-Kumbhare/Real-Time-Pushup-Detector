import cv2
import mediapipe as md
#specific versions of these files are required. Please check ReadMe file for the specific versions of the libraries.

md_drawing=md.solutions.drawing_utils
md_drawing_styles=md.solutions.drawing_styles
md_pose=md.solutions.pose

count = 0
position=None

cap=cv2.VideoCapture(0)   # captures the video

with md_pose.Pose(
        min_detection_confidence=0.7,
        min_tracking_confidence=0.7) as pose:
    while cap.isOpened():
        success, image=cap.read()
        if not success:
            print("empty camera")       #prints empty camera and exits the camera window.
            break
        image=cv2.flip(image, 1)
        #image=cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        result=pose.process(image)
        imlist=[]
        if result.pose_landmarks:
            md_drawing.draw_landmarks(
            image, result.pose_landmarks, md_pose. POSE_CONNECTIONS)
            for id, im in enumerate(result.pose_landmarks.landmark):
                h,w, _ =image.shape
                X,Y=int(im.x*w), int(im.y*h)
                imlist.append([id,X,Y])

            if len(imlist)!=0:
                #calculates the angle to determine the position
                if ((imlist[12][2] - imlist[14][2]) >= 15 and (imlist[11][2] - imlist[13][2]) >= 15):
                    position = "down"
                if ((imlist[12][2] - imlist[14][2]) <= 5 and (imlist[11][2] - imlist[13][2]) <= 5) and position == "down":
                    count = count+1
                    #for displalying text on the image
                    cv2.putText(image, "No Push-up", (image.shape[1] - 600, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, bottomLeftOrigin=False)
                else:
                    cv2.putText(image, "Push-up", (image.shape[1] - 600, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, bottomLeftOrigin=False)

        cv2.imshow("Push-up counter",image)   #displays camera window
        key=cv2.waitKey(1)
        if key==ord('q'):                     #press q to exit the camera window.
            break
cap.release()