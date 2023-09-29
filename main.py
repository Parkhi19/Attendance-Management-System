import cv2
import face_recognition

if __name__ == '__main__':
    cap = cv2.VideoCapture("testVideo.mp4")

    # Check if the video capture was successful
    if not cap.isOpened():
        print("Error: Video file not found or cannot be opened.")
        exit()

    while True:
        # Grab a single frame of video
        ret, frame = cap.read()

        if not ret:
            print("Video has ended.")
            break

        # Resize the frame for faster processing (optional)
        frame = cv2.resize(frame, (640, 480))

        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_frame = frame[:, :, ::-1]

        # Find all the faces in the current frame of video
        face_locations = face_recognition.face_locations(rgb_frame)

        for top, right, bottom, left in face_locations:
            # Draw a box around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Display the resulting image
        cv2.imshow('Video', frame)

        # Wait for a short amount of time and check for user input to stop
        if cv2.waitKey(10) == 27:  # Press 'Esc' key to exit
            break

    # Release the video capture and close all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()
