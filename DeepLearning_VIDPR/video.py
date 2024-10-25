import cv2

video_sources = [
    "D:/INTERNSHIP/853844-hd_1920_1080_25fps.mp4",
    "D:/INTERNSHIP/855564-hd_1920_1080_24fps.mp4",
    "D:/INTERNSHIP/ 2117231-hd_1920_1080_24fps.mp4"
]

caps = [cv2.VideoCapture(src) for src in video_sources]

for i, cap in enumerate(caps):
    if not cap.isOpened():
        print(f"Error: Could not open video stream {i+1} from source: {video_sources[i]}")
        exit()

while True:
    frames = [cap.read()[1] for cap in caps]

    if any(frame is None for frame in frames):
        print("Error: Could not read one or more frames.")
        break

    for i, frame in enumerate(frames):
        window_name = f'Video {i+1}'
        cv2.imshow(window_name, frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

for cap in caps:
    cap.release()
cv2.destroyAllWindows()