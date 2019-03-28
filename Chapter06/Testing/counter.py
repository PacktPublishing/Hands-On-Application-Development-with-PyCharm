import threading
import sys; sys.setswitchinterval(.000001)


class Counter:
    def __init__(self, target, num_threads):
        self.value = 0
        self.target = target
        self.num_threads = num_threads

    def update(self):
        current_value = self.value
        self.value = current_value + 1

    def run(self):
        threads = [threading.Thread(target=self.update)
                   for _ in range(self.target)]

        for t in threads:
            t.start()

        for t in threads:
            t.join()
