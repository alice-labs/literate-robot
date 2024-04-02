from copy import deepcopy

from parent import DocumentFactory
from documents import Document


# Memento: Represents the state of the document at a specific point in time
class DocumentMemento:
    def __init__(self, content: str):
        self._content = content

    def get_content(self):
        return self._content


# Originator: Creates and restores mementos
class DocumentEditor:
    def __init__(self, document: Document):
        self._document = document
        self._history = []
        self._index = -1

    def create_memento(self):
        return DocumentMemento(deepcopy(self._document))

    def restore_from_memento(self, memento: DocumentMemento):
        self._document = memento.get_content()

    def get_content(self):
        return self._document.get_content()

    def set_content(self, content: str):
        self._document.set_content(content)

    def format_document(self, format_type: str):
        self._document.format_content(format_type)

    def save_to_history(self):
        self._history = self._history[:self._index + 1]
        self._history.append(self.create_memento())
        self._index += 1

    def undo(self):
        if self._index > 0:
            self._index -= 1
            self.restore_from_memento(self._history[self._index])

    def redo(self):
        if self._index < len(self._history) - 1:
            self._index += 1
            self.restore_from_memento(self._history[self._index])


# Caretaker: Manages the history of the document
class DocumentHistory:
    def __init__(self, editor: DocumentEditor):
        self._editor = editor

    def save(self):
        self._editor.save_to_history()

    def undo(self):
        self._editor.undo()

    def redo(self):
        self._editor.redo()
