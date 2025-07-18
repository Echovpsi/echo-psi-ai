# presence_watcher.py – obecność i czas ciszy
import time

class PresenceWatcher:
    def __init__(self):
        self.last_active = time.time()
        self.user_present = False

    def update(self, user_present):
        self.user_present = user_present
        if user_present:
            self.last_active = time.time()

    def silence_duration(self):
        return time.time() - self.last_active
