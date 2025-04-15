# Vehicle Detection

## Overview
**Vehicle Detection** is a real-time traffic control system designed to detect vehicles in live traffic density at intersections. The system uses the YOLO object detection algorithm to detect vehicles in real-time, allowing for dynamic control of traffic signals, which can be used to reduce congestion and improve traffic flow.

## Features
- **Real-time vehicle detection** using YOLO.
- Integration with traffic signal hardware (e.g., Raspberry Pi, GPIO control).

## Problem Statement
Traditional traffic management systems operate on fixed timers or manual control, which often leads to inefficient traffic flow, increased waiting times, and higher fuel consumption. This project aims to solve these issues by utilizing real-time vehicle detection resulting in:
- Reduced waiting times.
- Lower fuel consumption and pollution.
- Decreased accident frequency by optimizing traffic flow.

## Technology
- **YOLO**: A powerful object detection model that uses a single forward pass of a convolutional neural network to detect vehicles in real-time. YOLO's efficiency makes it ideal for traffic management applications where real-time processing is essential.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Lalwaniamisha789/Adaptive-Traffic-Manager.git
   cd AdaptiveTrafficManager

2. Install dependencies
   ```bash
   pip install -r requirements.txt

3. Ensure you have YOLO installed:
   ```bash
   git clone https://github.com/ultralytics/yolo.git
   cd yolo
   pip install -r requirements.txt

## Usage 
1. Start the system with live video feed
   ```bash
   python main.py --source <path_to_video_or_camera_feed>
2. Adjust the settings in configuration files.

## How it works 
1. The camera feed captures videos from intersection
2. YOLO detects vehicles in the video feed and counts the number of vehicles in each lane.
   
## Sample Images

### 1. Detecting vehicles and pedestrians
![Screenshot 2024-10-06 163736](https://github.com/user-attachments/assets/7915aa71-ff3e-43e3-83f0-bfa75322df92)
![Screenshot 2024-10-06 163810](https://github.com/user-attachments/assets/9dd94fec-fb10-45b2-86a9-242fe56ea011)

### 2. IDing all vehicles(car, bus, truck, motorbikes) crosssing a threshold under a mask restricting the detection to required part of the lane
![Screenshot 2024-10-07 001848](https://github.com/user-attachments/assets/b6c044d1-2a6f-4b42-b074-fc073d2d5fb8)



