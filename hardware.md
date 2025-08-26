# Hardware & Wiring Guide

## Parts List

- TFMini Plus LiDAR (time-of-flight single-point LiDAR sensor)
- Arduino UNO (ATmega328P) or alternate MCU with hardware serial
- Raspberry Pi (3/4/Zero2) — for detection, logging, audio alerts
- USB A to TTL adapter (if connecting TFMini directly to Pi) or USB cable for Arduino
- Optional: GPS module (e.g., u-blox NEO-6M) for mapping detections
- Speaker or buzzer for driver alert

## Wiring

### Direct Pi Connection (recommended)

- TFMini TX → Pi RX (via TTL 3.3V)
- TFMini RX → Pi TX
- TFMini Vcc → 5V/3.3V per module spec
- GND → GND

### Arduino UNO as Bridge

- TFMini TX → Arduino D2 (SoftwareSerial RX)
- TFMini RX → Arduino D3 (SoftwareSerial TX)
- Arduino GND → TFMini GND

> **Note:** UNO + SoftwareSerial at 115200 baud is unreliable. Prefer hardware UART or direct Pi connection.

## Mounting

- Mount the sensor pointing downward (centerline or slightly forward of vehicle).
- Ensure rigid mounting to minimize vibration noise.

## Calibration

- With vehicle stationary on flat surface, collect ~100 samples for baseline (distance i).
- Use rolling baseline in software to compensate for drift.
- Validate detection by placing a known 10–20 cm ramp under the beam.

## Additional Notes

- Power TFMini per specs (do not exceed voltage).
- For robust detection, use moving average and debounce logic (see code).