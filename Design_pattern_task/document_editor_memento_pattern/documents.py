from abc import ABC, abstractmethod


class Document(ABC):
    @abstractmethod
    def get_content(self):
        pass

    @abstractmethod
    def set_content(self, content: str):
        pass

    @abstractmethod
    def format_content(self, content: str):
        pass


# Concrete Products: Different document types
class TextDocument(Document):
    def __init__(self):
        self._content = ""

    def get_content(self):
        return self._content

    def set_content(self, content: str):
        self._content = content

    def format_content(self, format_type: str):
        if format_type == "uppercase":
            self._content = self._content.upper()
        elif format_type == "lowercase":
            self._content = self._content.lower()
        elif format_type == "capitalize":
            self._content = self._content.capitalize()


class HTMLDocument(Document):
    def __init__(self):
        self._content = ""

    def get_content(self):
        return self._content

    def set_content(self, content: str):
        self._content = content

    def format_content(self, format_type: str):
        if format_type == "bold":
            self._content = f"<b>{self._content}</b>"
        elif format_type == "italic":
            self._content = f"<i>{self._content}</i>"
        elif format_type == "strikthrough":
            self._content = f"<s>{self._content}</s>"
