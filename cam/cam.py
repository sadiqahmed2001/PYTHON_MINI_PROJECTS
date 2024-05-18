
import cv2
import pyaudio
import numpy as np

def capture_video_and_audio(output_file="output.avi"):
    # Video settings
    video_width = 640
    video_height = 480
    frame_rate = 30

    # Audio settings
    audio_rate = 44100  # Increased audio sampling rate
    audio_channels = 2  # Increased number of audio channels for stereo
    audio_chunk = 1024

    # Initialize video capture
    video_capture = cv2.VideoCapture(0)
    video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, video_width)
    video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, video_height)
    video_capture.set(cv2.CAP_PROP_FPS, frame_rate)

    # Initialize audio capture
    audio_capture = pyaudio.PyAudio()
    audio_stream = audio_capture.open(format=pyaudio.paInt16,
                                      channels=audio_channels,
                                      rate=audio_rate,
                                      input=True,
                                      frames_per_buffer=audio_chunk)

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_file, fourcc, frame_rate, (video_width, video_height))

    while True:
        # Capture video frame
        ret, frame = video_capture.read()

        # Capture audio frame
        audio_frame = audio_stream.read(audio_chunk)
        audio_data = np.frombuffer(audio_frame, dtype=np.int16)

        # Write video frame to output file
        out.write(frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release everything when finished
    video_capture.release()
    out.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    capture_video_and_audio()


 
