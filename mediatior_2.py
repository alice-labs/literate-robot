from abc import ABC, abstractmethod

"""
    Channel: A room that handles messages for its subscribers.
    Subscriber: Individuals who can receive and post messages in a channel.
"""


class AbstractSubscriber(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def post(self, message: str):
        """Post a message"""

    @abstractmethod
    def receive(self, sender_name: str, message: str):
        """Receive posted message"""


class Subscriber(AbstractSubscriber):
    def __init__(self, name: str):
        super().__init__(name)
        self.subscribed_channel = None

    def post(self, message: str):
        """Post a message"""
        self.subscribed_channel.broadcast_post(sender=self, message=message)

    def receive(self, sender_name: str, message: str):
        """Receive a message"""
        print(f"{sender_name} sent a message to {self.name}: {message}")


class Channel(ABC):
    def __init__(self, name: str):
        self.name = name
        self.subscribers = []

    def add_subscriber(self, subscriber: Subscriber):
        subscriber.subscribed_channel = self
        self.subscribers.append(subscriber)

    def broadcast_post(self, sender: Subscriber, message: str):
        for subscriber in self.subscribers:
            if subscriber != sender:
                subscriber.receive(sender_name=sender.name, message=message)


channel_1 = Channel(name="Tech Team")

abed = Subscriber(name="Abed")
sayad = Subscriber(name="Sayad")
rfl = Subscriber(name="Raphael")
james = Subscriber(name="James")
navid = Subscriber(name="Navid")
minhaz = Subscriber(name="Minhaz")

channel_1.add_subscriber(subscriber=abed)
channel_1.add_subscriber(subscriber=sayad)
channel_1.add_subscriber(subscriber=rfl)
channel_1.add_subscriber(subscriber=james)
channel_1.add_subscriber(subscriber=navid)
# channel_1.add_subscriber(subscriber=minhaz)

abed.post(message="I will be on a leave today. Thank you.")
rfl.post(message="Approved. Well deserved!")
