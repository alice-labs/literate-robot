from typing import Optional
from factory import AbstractFactory, TextDocumentFactory, HTMLDocumentFactory


class DocumentFactory:
    def __new__(cls, document_type: str) -> Optional[AbstractFactory]:
        if document_type == "text":
            return TextDocumentFactory()
        elif document_type == "html":
            return HTMLDocumentFactory()
