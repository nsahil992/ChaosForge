import time


def burn_cpu(duration=10):

    print("[WARNING] CPU burn simulation started")

    end_time = time.time() + duration

    while time.time() < end_time:
        _ = 99999 * 99999

    print("[INFO] CPU burn simulation completed")