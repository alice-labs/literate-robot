
from factory import TextDocumentFactory
from memento import DocumentEditor, DocumentHistory
from parent import DocumentFactory
import unittest

class TestDocumentEditor(unittest.TestCase):
    def setUp(self):
        # Create a document factory
        self.text_document_factory = DocumentFactory("text")
        self.html_document_factory = DocumentFactory("html")

        # Create a document editor
        self.text_editor = DocumentEditor(self.text_document_factory.create_document())
        self.html_editor = DocumentEditor(self.html_document_factory.create_document())

        # Create a caretaker to manage the history
        self.text_history = DocumentHistory(self.text_editor)
        self.html_history = DocumentHistory(self.html_editor)

    def test_undo_redo_text_document(self):
        # Initial content
        self.text_editor.set_content("Hello, Text Document!")

        # Save initial state
        self.text_history.save() # 0

        # Modify content
        self.text_editor.set_content("Hello, Updated Text Document!")

        # Save modified state
        self.text_history.save() # 1

        # Undo
        self.text_history.undo()
        self.assertEqual(self.text_editor.get_content(), "Hello, Text Document!")

        # Redo
        self.text_history.redo()
        self.assertEqual(self.text_editor.get_content(), "Hello, Updated Text Document!")


    def test_text_document_formatting(self):
        # format - bold
        self.text_editor.set_content("Hello, Text Document!")

        # Save initial state
        self.text_history.save() # 0

        self.text_editor.format_document("uppercase")
        self.text_history.save() # 1

        # Undo
        self.text_history.undo()
        self.assertEqual(self.text_editor.get_content(), "Hello, Text Document!")

        # Redo
        self.text_history.redo()
        self.assertEqual(self.text_editor.get_content(), "HELLO, TEXT DOCUMENT!")


    def test_html_document_formatting(self):
        # format - bold
        self.html_editor.set_content("<h1>Hello, HTML Document!</h1>")

        # Save initial state
        self.html_history.save() # 0

        self.html_editor.format_document("bold")
        self.html_history.save() # 1

        # Undo
        self.html_history.undo()
        self.assertEqual(self.html_editor.get_content(), "<h1>Hello, HTML Document!</h1>")

        # Redo
        self.html_history.redo()
        self.assertEqual(self.html_editor.get_content(), "<b><h1>Hello, HTML Document!</h1></b>")


    def test_undo_redo_html_document(self):
        # Initial content
        self.html_editor.set_content("<h1>Hello, HTML Document!</h1>")

        # Save initial state
        self.html_history.save()

        # Modify content
        self.html_editor.set_content("<h1>Hello, Updated HTML Document!</h1>")

        # Save modified state
        self.html_history.save()

        # Undo
        self.html_history.undo()
        self.assertEqual(self.html_editor.get_content(), "<h1>Hello, HTML Document!</h1>")

        # Redo
        self.html_history.redo()
        self.assertEqual(self.html_editor.get_content(), "<h1>Hello, Updated HTML Document!</h1>")


if __name__ == "__main__":
    unittest.main()
