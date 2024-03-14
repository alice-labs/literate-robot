from abc import ABC, abstractmethod
import threading
import time

# Strategy Pattern
class JobStrategy(ABC):
    @abstractmethod
    def execute(self):
        pass

class EmailJobStrategy(JobStrategy):
    def execute(self):
        print("------- Sending Email ---------")

class CleanupJobStrategy(JobStrategy):
    def execute(self):
        print("-------- Cleaning up ---------------")


# Concrete Observer
class JobObserver(threading.Thread):
    def __init__(self, name, interval, strategy, delay=0):
        super().__init__()
        self._name = name
        self._interval = interval
        self._strategy = strategy
        self._delay = delay
        self._stop_event = threading.Event()

    def run(self):
        time.sleep(self._delay)
        while not self._stop_event.is_set():
            print(f"{self._name} triggered")
            self._strategy.execute()
            self._stop_event.wait(self._interval)

    def stop(self):
        self._stop_event.set()


# Observer Pattern
class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update()


# Concrete Subject
class JobScheduler(Subject):
    def __init__(self):
        super().__init__()

    def schedule_job(self, name, interval, strategy, delay=0):
        observer = JobObserver(name, interval, strategy, delay)
        self.attach(observer)
        observer.start()

    def stop_jobs(self):
        for observer in self._observers:
            observer.stop()


if __name__ == "__main__":

    email_strategy = EmailJobStrategy()
    cleanup_strategy = CleanupJobStrategy()

    scheduler = JobScheduler()
    scheduler.schedule_job("Cleanup", 10, cleanup_strategy, delay=10)  # Cleanup after 10 seconds
    scheduler.schedule_job("Email", 5, email_strategy)  # Every 5 seconds

    time.sleep(30)
    scheduler.stop_jobs()
