import cv2

def take_picture(file_name="user_picture.jpg"):
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cv2.imwrite(file_name, frame)
    cap.release()
    print(f"Picture saved as {file_name}")

if __name__ == "__main__":
    take_picture()