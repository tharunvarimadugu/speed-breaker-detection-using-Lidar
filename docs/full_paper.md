# Speed Breaker Detection and Alert System Using LiDAR

## 1. Introduction

According to a 2019 study by the Ministry of Road Transport of India, speed breakers are alarmingly responsible for 30 accidents per day, resulting in the loss of nine lives daily. These innocuous road features pose a significant threat to both vehicles and passengers. The 2019 Indian Road Accidents Report further highlights that faulty road infrastructure contributes to over 2,800 deaths and 9,900 accidents. In adverse weather conditions such as fog and mist, drivers face additional challenges. Reduced visibility impairs their ability to spot speed breakers ahead. On highways, where vehicles often travel at an average speed of 60 km/h, failing to perceive a speed breaker can lead to severe consequences. The sudden impact can cause the automobile to jerk violently, potentially damaging the vehicle and endangering passengers. Injuries such as back pain and skull trauma may result from these unexpected encounters with unmarked speed breakers.

## 2. Literature Survey

- [1] Zed stereo camera + Nvidia GPU: Cost and lighting issues.
- [2] Image processing: Good lighting only.
- [3] GPS + accelerometer: Marks GPS coordinates on acceleration spike.
- [4, 6] Radar/MEMS: Reliable in adverse weather, electromagnetic waves penetrate fog.
- [5] Three cameras + YOLO V4: Comprehensive road view.
- [7] LiDAR: 3D point clouds, robust in low light.
- [8] LiDAR loop closure: Accuracy improvements in mapping.
- [9] 2D LiDAR for micro-mobility: Compact, cost-effective, limited density.
- [10] Radar for vulnerable road user detection.
- [11] Driving support systems for hump detection.
- [12] 2D LiDAR + IoT for 3D mapping.
- [13] Intelligent transport systems: Safety, efficiency.
- [14] Outdoor localization for navigation.
- [15] 2D LiDAR + monocular camera fusion for vehicle detection/tracking.

## 3. System Description

Democratizes LiDAR technology by integrating a roof-mounted sensor into regular cars, enabling real-time safety features like collision avoidance. TFMini Plus LiDAR sensor measures distances (4 cm to 12 m) using Time-of-Flight technology, providing real-time analysis for collision avoidance and object tracking. Arduino UNO (ATMEGA328P) manages sensor I/O. System flow: LiDAR → Arduino → Raspberry Pi.

## 4. Challenges in Existing Speed Breaker Detection Systems

- **Low light conditions:** Vision algorithms struggle.
- **Real time adaptivity:** GPS/accelerometer methods lack dynamic alerts.
- **Data quality and availability:** Hard to obtain diverse, labeled data.
- **Real-time processing and scalability:** Technical challenges in handling video data.
- **Generalization and robustness:** Models must work across diverse environments.

## 5. Proposed Speed Breaker Detection Method

- **Architecture:** LiDAR sensor issues early alerts, effective in low light/fog.
- **Working Principle:** Time-of-Flight; measures distance using light pulses.
- **Method:** Detects elevation change of 10–20 cm (i - k) between baseline and bump; triggers audio alert.

## 6. Results & Discussion

- **Performance:** System tested in day, night, fog, and rain.
- **Integration:** Can be linked to adaptive cruise control, automatic braking, and mapping.
- **Table 1. Performance Comparison:**

| Conditions         | Proposed System Accuracy | Existing System Accuracy |
|--------------------|------------------------|-------------------------|
| Day                | 99.5%                  | 97.44%                  |
| Night              | 99.5%                  | 90%                     |
| Foggy, Mist        | 98%                    | 87%                     |
| Rainy              | 95%                    | 80%                     |

## 7. Conclusion & Future Scope

LiDAR sensor technology for speed breaker detection enhances road safety, especially at night and in adverse weather. Integrating camera and LiDAR data increases object identification accuracy. 3D LiDAR provides depth, improving detection. Continued refinement and integration with GPS and camera systems will further improve road safety.

---

**License:**  
This chapter has been made available under a CC BY-NC-ND 4.0 license

---

**References:**  
(See your original paper for full citations)