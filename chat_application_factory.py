from abc import ABC, abstractmethod

"""
Design a chat application with support for different message types (text, images, files) and real-time updates.
Apply design patterns to manage message handling, user notifications, and message storage.
"""

conversation = []  # storage

class Message(ABC):
    @abstractmethod
    def get_content(self):
        """
        This method will parse the content.
        """

    def get_data(self) -> None:
        # we could return by id
        print(self.content)

    def store_message(self):
        conversation.append({"type": self.type, "content": self.content})
        print(f"{self.type} stored successfully")


class TextFormatter(Message):
    def __init__(self, type: str, content: str):
        # id
        self.type = type
        self.content = self.get_content(content=content)

    def get_content(self, content: str) -> str:
        text = f"Text: {content}"
        return text


class FileFormatter(Message):
    def __init__(self, type: str, content: str):
        self.type = type
        self.content = self.get_content(content=content)

    def get_content(self, content: str) -> str:
        text = f"File: {content}"
        return text


class ImageFormatter(Message):
    def __init__(self, type: str, content: str):
        self.type = type
        self.content = self.get_content(content=content)

    def get_content(self, content: str) -> str:
        text = f"Image: {content}"
        return text


class Creator:
    # Factory Class
    @staticmethod
    def handle_message(type: str, content: str):
        if type == 'text':
            data_obj = TextFormatter(type=type, content=content)
            data_obj.get_data()
            data_obj.store_message()
            # broadcast message to subscriber
        elif type == 'image':
            data_obj = ImageFormatter(type=type, content=content)
            data_obj.get_data()
            data_obj.store_message()
            # broadcast message to subscriber
        elif type == 'file':
            data_obj = FileFormatter(type=type, content=content)
            data_obj.get_data()
            data_obj.store_message()
            # broadcast message to subscriber
        else:
            print("Data Type not Supported")


creator_obj = Creator()
creator_obj.handle_message(type="text", content="Wazaaaa!")
creator_obj.handle_message(type="image", content="Image.png")
creator_obj.handle_message(type="file", content="File.pdf")
creator_obj.handle_message(type="video", content="video.mp4")

print("stored data: ", conversation)
