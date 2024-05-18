import cv2

def take_picture(file_name="user_picture.jpg"):
    # Initialize the webcam
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Unable to access the webcam.")
        return

    # Capture a frame from the webcam
    ret, frame = cap.read()

    if not ret:
        print("Error: Unable to capture frame.")
        cap.release()
        return

    # Save the captured frame as an image
    cv2.imwrite(file_name, frame)

    # Release the webcam
    cap.release()

    print(f"Picture saved as {file_name}")

if __name__ == "__main__":
    take_picture()