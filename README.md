# Adaptive Traffic Manager

## Abstract
Traffic congestion is a growing issue due to the increasing number of vehicles on roads. Conventional traffic systems, which rely on fixed timers or manual control, fail to account for real-time traffic conditions, leading to longer waiting times, higher fuel consumption, and increased pollution. This project proposes a **computer vision-based traffic signal controller** that dynamically adjusts traffic light durations based on real-time traffic density. By utilizing the **YOLO (You Only Look Once)** object detection algorithm, the system can recognize and classify vehicles in real-time, allowing for optimized green signal timings and improved traffic flow.

## Problem Statement
The goal of this project is to develop a self-adaptive traffic light control system using YOLO. Traditional traffic management systems allocate equal time to each lane, regardless of actual traffic conditions, leading to inefficiencies. Our solution enables the traffic management system to make time allocation decisions based on the traffic density in each lane using cameras and image processing modules. This approach helps reduce delays, lower traffic and waiting times, decrease accident frequency, and minimize fuel consumption, ultimately contributing to lower air pollution.

## Conventional Systems
1. **Manual Controlling**: Traffic police manually manage traffic signals based on observed road conditions.
2. **Automatic Controlling**: Timers and electrical sensors automate traffic lights, operating on a fixed timer regardless of actual traffic conditions.
3. **Electronic Sensors**: Loop detectors or proximity sensors provide data on road traffic, but they can be costly and may not provide real-time adaptability.

## Introduction
Traffic congestion is a major problem faced by many cities, especially megacities like Mumbai, Hyderabad, Bengaluru, and Delhi. The ever-increasing nature of this problem necessitates real-time knowledge of road traffic density for improved signal control and traffic management. One of the key factors affecting traffic flow is the traffic controller. Current traffic management systems are primarily static, which means they do not respond to the needs of the traffic flow.

## Technology
The term 'You Only Look Once' (YOLO) refers to an object detection algorithm that performs real-time object detection and classification in images. It uses convolutional neural networks (CNNs) to predict multiple bounding boxes and class probabilities for objects in a single forward propagation through the neural network, making it extremely efficient for real-time applications.

## Adaptive Traffic Manager

### Overview
The **Adaptive Traffic Manager** is a real-time traffic control system that utilizes YOLO for object detection to assess traffic density at a crossroads. Based on vehicle counts, the system dynamically adjusts traffic light durations to optimize traffic flow and reduce congestion.

### Features
- Real-time vehicle detection using YOLOv5.
- Dynamic traffic light control based on traffic density.
- Adjustable green light durations based on detected vehicle count.
- Easy integration with traffic light control hardware (e.g., Raspberry Pi with GPIO).

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


