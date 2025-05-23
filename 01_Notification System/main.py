from abc import ABC, abstractmethod

class Notifier(ABC):
    @abstractmethod
    def send(self, message: str):
        pass


class Email(Notifier):
    def send(self, message: str):
        print(f"Sending an Email...{message}")

class SimpleMessageService(Notifier):
    def send(self, message: str):
        print(f"Sending an SMS...{message}")
        

class Push(Notifier):
    def send(self, message: str):
        print(f"Sending a Push notification...{message}")
        
        
class NotificationManager:
    def __init__(self, notifier: Notifier) -> None:
        self.notifier = notifier
        
    def notify(self, message: str):
        self.notifier.send(message)
        
email = Email()
sms = SimpleMessageService()
push = Push()

manager = NotificationManager(email)

manager.notify("Hi mera name Maaz hai.")