import cv2
import threading
import time
from ultralytics import YOLOv10
import supervision as sv

model = YOLOv10('best.pt')
bounding_box_annotator = sv.BoundingBoxAnnotator()
label_annotator = sv.LabelAnnotator()

rtsp_url = "rtsp://user:password@ip_address:port"

class VideoCaptureThreading:
    def __init__(self, src):
        self.cap = cv2.VideoCapture(src)
        self.cap.set(cv2.CAP_PROP_BUFFERSIZE, 3)
        self.ret = False
        self.frame = None
        self.stopped = False
        self.lock = threading.Lock()
        self.thread = threading.Thread(target=self.update, args=())
        self.thread.start()

    def update(self):
        while not self.stopped:
            if not self.cap.isOpened():
                continue
            ret, frame = self.cap.read()
            with self.lock:
                self.ret = ret
                self.frame = frame
            time.sleep(0.01)

    def read(self):
        with self.lock:
            return self.ret, self.frame

    def stop(self):
        self.stopped = True
        self.thread.join()
        self.cap.release()


video_capture = VideoCaptureThreading(rtsp_url)

time.sleep(2) # wait for rtsp connection

if not video_capture.cap.isOpened():
    print("Error opening video stream")
    exit()


window_name = 'Cam1'
cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
cv2.resizeWindow(window_name, 640, 480)

while True:
    ret, frame = video_capture.read()
    if not ret or frame is None:
        print("Error reading frame")
        continue

    results = model(frame)[0]
    detections = sv.Detections.from_ultralytics(results)

    annotated_image = bounding_box_annotator.annotate(scene=frame, detections=detections)
    annotated_image = label_annotator.annotate(scene=annotated_image, detections=detections)

    cv2.imshow(window_name, annotated_image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.stop()
cv2.destroyAllWindows()
