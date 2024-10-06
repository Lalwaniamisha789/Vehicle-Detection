# Adaptive Traffic Manager

## Overview
**Adaptive Traffic Manager** is a real-time traffic control system designed to optimize traffic light durations based on live traffic density at intersections. The system uses the YOLOv5 object detection algorithm to detect vehicles in real-time, allowing for dynamic control of traffic signals, which reduces congestion and improves traffic flow.

## Features
- **Real-time vehicle detection** using YOLOv5.
- **Dynamic traffic light control** based on traffic density.
- **Configurable green light durations** based on detected vehicle counts.
- Integration with traffic signal hardware (e.g., Raspberry Pi, GPIO control).

## Problem Statement
Traditional traffic management systems operate on fixed timers or manual control, which often leads to inefficient traffic flow, increased waiting times, and higher fuel consumption. This project aims to solve these issues by utilizing real-time vehicle detection to adapt signal timings dynamically, resulting in:
- Reduced waiting times.
- Lower fuel consumption and pollution.
- Decreased accident frequency by optimizing traffic flow.

## Technology
- **YOLOv5**: A powerful object detection model that uses a single forward pass of a convolutional neural network to detect vehicles in real-time. YOLOv5's efficiency makes it ideal for traffic management applications where real-time processing is essential.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Lalwaniamisha789/Adaptive-Traffic-Manager.git
   cd AdaptiveTrafficManager

2. Install dependencies
   ```bash
   pip install -r requirements.txt

3. Ensure you have YOLOv5 installed:
   ```bash
   git clone https://github.com/ultralytics/yolov5.git
   cd yolov5
   pip install -r requirements.txt

## Usage 
1. Start the system with live video feed
   ```bash
   python main.py --source <path_to_video_or_camera_feed>
2. Adjust the settings in configuration files.

## How it works 
1. The camera feed captures videos from intersection
2. YOLOv5 detects vehicles in the video feed and counts the number of vehicles in each lane.
3. I used the SORT model to ID vehicles crossing a threshold.
4. Based on the traffic density, the traffic signal controller adjusts the green light duration for each lane dynamically, optimizing traffic flow and reducing congestion.
   
## Sample Images

### 1. Detecting vehicles and pedestrians
![Screenshot 2024-10-06 163736](https://github.com/user-attachments/assets/7915aa71-ff3e-43e3-83f0-bfa75322df92)
![Screenshot 2024-10-06 163810](https://github.com/user-attachments/assets/9dd94fec-fb10-45b2-86a9-242fe56ea011)

### 2. IDing all vehicles(car, bus, truck, motorbikes) crosssing a threshold under a mask restricting the detection to required part of the lane
![Screenshot 2024-10-07 001848](https://github.com/user-attachments/assets/b6c044d1-2a6f-4b42-b074-fc073d2d5fb8)

## Algorithm Used
![165362571-06875fea-9fe9-4075-a74e-871503363649](https://github.com/user-attachments/assets/8e14a18a-d8cf-4e9c-9aa1-cba033074236)


