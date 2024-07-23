
# import cv2

# # Function to zoom in on a specific region of the frame
# def zoom_at_point(frame, x, y, zoom_factor=2):
#     height, width = frame.shape[:2]
#     zoom_width, zoom_height = width // zoom_factor, height // zoom_factor
    
#     x1 = max(0, x - zoom_width // 2)
#     y1 = max(0, y - zoom_height // 2)
#     x2 = min(width, x + zoom_width // 2)
#     y2 = min(height, y + zoom_height // 2)

#     roi = frame[y1:y2, x1:x2]
#     zoomed_frame = cv2.resize(roi, (width, height), interpolation=cv2.INTER_LINEAR)
#     return zoomed_frame

# # Mouse callback function to handle zooming
# def mouse_callback(event, x, y, flags, param):
#     global zoom_center
#     if event == cv2.EVENT_LBUTTONDOWN:
#         zoom_center = (x, y)

# # Load the video
# cap = cv2.VideoCapture('small.mp4')

# # Check if the video opened successfully
# if not cap.isOpened():
#     print("Error: Could not open video.")
#     exit()

# # Create a named window and set the mouse callback
# cv2.namedWindow("Frame")
# cv2.setMouseCallback("Frame", mouse_callback)

# zoom_center = None

# while True:
#     # Capture frame-by-frame
#     ret, frame = cap.read()
    
#     if not ret:
#         break
    
#     # Check if a zoom center is set and apply zoom
#     if zoom_center is not None:
#         frame = zoom_at_point(frame, zoom_center[0], zoom_center[1])
    
#     # Display the resulting frame
#     cv2.imshow("Frame", frame)
    
#     key = cv2.waitKey(30) & 0xFF
    
#     # If the 'q' key is pressed, break from the loop
#     if key == ord('q'):
#         break

# # Release the capture and close windows
# cap.release()
# cv2.destroyAllWindows()