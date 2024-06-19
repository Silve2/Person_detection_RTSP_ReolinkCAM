
# Real-Time Person Detection via RTSP Stream

This project utilizes a trained YOLOv10 model to detect people in real-time from an RTSP video stream.

## Requirements

Make sure you have the following packages installed:

- `opencv-python`
- `ultralytics` -----> pip install -q git+https://github.com/THU-MIG/yolov10.git
- `supervision`

You can install them using `pip`:

```bash
pip install opencv-python ultralytics supervision
```


## Configuration
1. YOLOv10 Model: Ensure you have the best.pt weights file for the YOLOv10 model.
   This is model trained with my date. You can train the model on your own data or download a pre-trained model.
3. RTSP URL: Insert your camera's RTSP URL into the code.

## Training YOLOv10

This is the script for training your YOLOv10 model. Require a Roboflow account for data processing.
<a>https://colab.research.google.com/drive/1wTKPzregHNyulhTbpeLGp-UiEmLemGdZ?usp=sharing</a>

## RTSP URL

In your Python file, replace the rtsp_url string with your RTSP camera URL:

```python
rtsp_url = "rtsp://utente:password@indirizzo_ip:porta"
```
## Technical aspects
### What is RTSP protocol?
RTSP (Real-Time Streaming Protocol) is a network protocol designed for controlling media streaming servers. The protocol enables remote control of real-time multimedia streams. For example, it is commonly used to view live video feeds from IP cameras. RTSP manages the transmission of video streams and allows functions such as play, pause, and record.
### What is YOLO?
YOLO (You Only Look Once) is a family of computer vision algorithms used for real-time object detection in images and videos. YOLO is known for its speed and accuracy. The algorithm divides the image into a grid and passes through each grid cell to predict bounding boxes and probabilities for each object. YOLOv10 is an advanced version of the model that offers improvements in speed and accuracy.
### How does video threading work?
Threading is a programming technique that allows simultaneous execution of multiple operations. In this project, we use a separate thread to capture frames from the RTSP stream in real-time. The VideoCaptureThreading class manages frame reading in a separate thread to reduce latency and improve real-time detection performance. The thread's update method continuously reads frames from the camera and stores them in shared variables, which can be accessed by the main thread for object detection.

