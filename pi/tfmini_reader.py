import serial
import time
import struct

class TFminiReader:
    """
    Parses TFMini frame format (standard frame)
    Frame structure (TFMini standard, typical):
    0x59 0x59  - header
    Dist_L Dist_H  - distance (little endian) in cm
    Flux_L Flux_H - signal strength
    Temp_L Temp_H - optional
    Checksum
    """
    def __init__(self, port="/dev/ttyUSB0", baud=115200, timeout=1.0):
        self.ser = serial.Serial(port, baud, timeout=timeout)

    def read_frame(self):
        s = self.ser
        # find header 0x59 0x59
        while True:
            b = s.read(1)
            if not b:
                return None
            if b == b'\x59':
                b2 = s.read(1)
                if b2 == b'\x59':
                    # read next 7 bytes (distance low, high, strength low, high, temp low, high, checksum)
                    payload = s.read(7)
                    if len(payload) < 7:
                        return None
                    dist_l = payload[0]
                    dist_h = payload[1]
                    dist = (dist_h << 8) + dist_l  # in cm
                    # optional: signal strength
                    strength = payload[2] + (payload[3] << 8)
                    # checksum could be validated
                    return {'distance_m': dist / 100.0, 'strength': strength}
                # else continue searching
    def close(self):
        self.ser.close()


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', default="/dev/ttyUSB0")
    parser.add_argument('--baud', type=int, default=115200)
    args = parser.parse_args()
    reader = TFminiReader(args.port, args.baud)
    try:
        while True:
            frame = reader.read_frame()
            if frame:
                print(f"{time.time():.3f}, {frame['distance_m']:.3f}, strength:{frame['strength']}")
            else:
                time.sleep(0.01)
    except KeyboardInterrupt:
        reader.close()