import cv2

def detect_face(image_path):
    # Load the pre-trained face detection model
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Load the input image
    image = cv2.imread(image_path)

    # Convert the image to grayscale for face detection
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Draw rectangles around the detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display the image with detected faces
    cv2.imshow('Detected Faces', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Ask user for verification
    verified = input("Is this your face? (yes/no): ").lower()
    if verified == "yes":
        return True
    else:
        return False

def main():
    name = input("Enter the name of the user: ")
    photo_path = input("Enter the path to the user's photo: ")

    print("Detecting faces...")
    if detect_face(photo_path):
        print("Face detected and verified. Access granted.")
    else:
        print("Face not verified. Access denied.")

if __name__ == "__main__":
    main()