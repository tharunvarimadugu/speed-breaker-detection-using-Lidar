# Speed Breaker Detection & Alert System — Using TFMini Plus LiDAR

## Overview

This repository implements the LiDAR-based speed breaker detection and alert system described in the paper:

**"Speed breaker detection and alert system using LiDAR"**  
R. Nidhya, S. Goutham, V. Maheshwar Reddy & V. Tharun Reddy  
DOI: 10.1201/9781003559092-104

---

## Motivation

Speed breakers are responsible for ~30 accidents and 9 deaths per day in India ([2019 Ministry of Road Transport](https://morth.nic.in)). Unmarked or poorly visible speed breakers pose significant danger, especially in low-light or adverse weather. Faulty road infrastructure contributes to thousands of deaths and injuries annually. This project aims to provide a robust, real-time solution using LiDAR technology.

---

## Literature Survey (Summary)

- **Camera/image processing:** Effective in good light, struggles with poor illumination or unmarked bumps.
- **Radar/MEMS:** Robust in adverse weather, higher cost and complexity.
- **GPS/accelerometer:** Limited by real-time adaptability, less effective on new routes.
- **LiDAR:** Accurate, reliable in low light, cost-effective for real-time speed breaker detection.

---

## System Description

- **TFMini Plus LiDAR:** Measures distance (4 cm–12 m), low power, time-of-flight sensor.
- **Arduino UNO (ATMega328P):** Handles sensor I/O, forwards data to Raspberry Pi.
- **Raspberry Pi:** Runs Python detection and alert logic.
- **Detection logic:** Rolling baseline measurement; sudden distance drop indicates a bump. If elevation change is between 10–20 cm, an audio alert is triggered for the driver.
- **Alerts:** Audio beep/voice issued via Pi speaker.

---

## Key Files

- `firmware/arduino_tfmini_uno.ino`: Arduino sketch to forward TFMini data to USB serial.
- `pi/tfmini_reader.py`: Python serial reader for TFMini frames.
- `pi/detector.py`: Bump detection and alert logic.
- `config.yaml`: Adjustable thresholds and serial settings.
- `hardware.md`: Wiring, parts list, mounting and calibration instructions.
- `docs/paper_abstract_corrected.md`: Corrected abstract for documentation.
- `docs/full_paper.md`: Full research paper text.
- `tests/synthetic_test.py`: Automated logic test.

---

## Challenges in Existing Systems

1. **Low light conditions:** Vision-based systems struggle with poor illumination.
2. **Real-time adaptivity:** Previous methods (GPS/accelerometer) lack dynamic real-time alerts.
3. **Data quality:** Collecting diverse, labeled real-world training data is difficult.
4. **Processing speed and scalability:** Real-time operation with high accuracy is challenging.
5. **Generalization and robustness:** Models must perform well in varied environments.

---

## Proposed Method

- Rolling baseline for flat road detection.
- Detect sudden road elevation drop using LiDAR.
- If the difference is between 10–20 cm, trigger an alert.
- Results: 99.5% accuracy (day/night), 98% (fog), 95% (rain).

---

## Results & Discussion

- System tested in varied conditions, outperforming vision-only systems in poor visibility.
- Suitable for integration with adaptive cruise control, mapping, and driver-assist systems.
- Table of performance comparison provided in `docs/full_paper.md`.

---

## Conclusion & Future Scope

LiDAR-based speed breaker detection improves safety, especially in adverse conditions. Further integration with camera/GPS can enhance accuracy and expand functionality.

---

## License

Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)

---

## Citation

Please cite the published paper (DOI: 10.1201/9781003559092-104) if you use this repo.
