from abc import ABC, abstractmethod
from documents import Document, HTMLDocument, TextDocument


class AbstractFactory(ABC):
    @abstractmethod
    def create_document(self) -> Document:
        pass


class TextDocumentFactory(AbstractFactory):
    def create_document(self) -> Document:
        return TextDocument()


class HTMLDocumentFactory(AbstractFactory):
    def create_document(self) -> Document:
        return HTMLDocument()
