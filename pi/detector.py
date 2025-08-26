import time
import yaml
import numpy as np
from tfmini_reader import TFminiReader
import threading
import os
import datetime
import subprocess

def load_config(path="config.yaml"):
    with open(path, 'r') as f:
        return yaml.safe_load(f)

class BumpDetector:
    def __init__(self, cfg):
        self.cfg = cfg
        self.baseline_window = cfg.get('baseline_window', 40)
        self.min_h = cfg.get('min_bump_height', 0.10)
        self.max_h = cfg.get('max_bump_height', 0.20)
        self.min_consec = cfg.get('min_consecutive_triggers', 3)
        self.post_suppress = cfg.get('post_trigger_suppression_sec', 1.5)
        self.samples = []
        self.last_trigger_time = 0
        self.consec = 0
        self.log_file = cfg.get('log_file', 'detections.log')

    def add_sample(self, d):
        # d in meters
        self.samples.append(d)
        if len(self.samples) > self.baseline_window:
            self.samples.pop(0)

    def baseline(self):
        if len(self.samples) == 0:
            return None
        # robust baseline: median
        return float(np.median(self.samples))

    def process(self, distance):
        self.add_sample(distance)
        base = self.baseline()
        if base is None:
            return None
        height = base - distance  # positive when beam hits raised bump
        now = time.time()
        if now - self.last_trigger_time < self.post_suppress:
            # suppress events immediately after trigger
            self.consec = 0
            return None
        if self.min_h <= height <= self.max_h:
            self.consec += 1
            if self.consec >= self.min_consec:
                # detection confirmed
                self.last_trigger_time = now
                self.consec = 0
                det = {'timestamp': datetime.datetime.utcnow().isoformat() + 'Z',
                       'baseline_m': base,
                       'distance_m': distance,
                       'height_m': height}
                self.log_detection(det)
                self.alert()
                return det
        else:
            self.consec = 0
        return None

    def log_detection(self, det):
        line = f"{det['timestamp']}, base={det['baseline_m']:.3f}, dist={det['distance_m']:.3f}, height={det['height_m']:.3f}\n"
        with open(self.log_file, 'a') as f:
            f.write(line)
        print("DETECTION:", line.strip())

    def alert(self):
        # simple audio beep using aplay or system beep
        try:
            # try to play a short beep (requires beep.wav or use system speaker)
            # For Pi OS you can use: speaker-test -t sine -f 1000 -l 1
            subprocess.Popen(['speaker-test', '-t', 'sine', '-f', '1000', '-l', '1'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except Exception:
            # fallback: print
            print("ALERT (audio)")


def run_loop(cfg):
    port = cfg.get('serial_port', '/dev/ttyUSB0')
    baud = cfg.get('baudrate', 115200)
    reader = TFminiReader(port, baud)
    detector = BumpDetector(cfg)
    try:
        while True:
            frame = reader.read_frame()
            if frame:
                d = frame['distance_m']
                det = detector.process(d)
            else:
                time.sleep(0.01)
    except KeyboardInterrupt:
        reader.close()

if __name__ == "__main__":
    cfg = load_config("config.yaml")
    run_loop(cfg)
