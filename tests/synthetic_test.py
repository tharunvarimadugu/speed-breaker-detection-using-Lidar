import time
from pi.detector import BumpDetector
import yaml

def test_synthetic_bump(tmp_path):
    cfg = {
        'baseline_window': 20,
        'min_bump_height': 0.10,
        'max_bump_height': 0.20,
        'min_consecutive_triggers': 2,
        'post_trigger_suppression_sec': 0.5,
        'log_file': str(tmp_path / "log.txt")
    }
    det = BumpDetector(cfg)
    # simulate flat road at 1.50 m for 30 samples
    for _ in range(30):
        res = det.process(1.50)
        assert res is None
    # now simulate bump: beam distance drops to 1.38 m (height 0.12)
    detections = []
    for _ in range(3):
        r = det.process(1.38)
        if r:
            detections.append(r)
    assert len(detections) >= 1
