from abc import ABC, abstractmethod

"""
    A File Structure that can consist of Folders and Files
    Each Folder can consist of Files and more Folders
    Folders and Files both share the same operation read().
    Solution: Create a Composite class (Folder) and Base Class (File)
    Both Classes must implement the File interface containing the read() method.
"""


class File(ABC):
    @abstractmethod
    def read(self):
        """File Name"""


class TextFile(File):
    def __init__(self, name: str):
        self.name = name

    def read(self):
        print(f"Text File: {self.name}")


class ImageFile(File):
    def __init__(self, name: str):
        self.name = name

    def read(self):
        print(f"Image File: {self.name}")


class Folder(File):
    def __init__(self, name):
        self.name = name
        self.files = []

    def add_file(self, file):
        self.files.append(file)

    def read(self):
        print("folder name: ", self.name)
        for file in self.files:
            file.read()


text1 = TextFile("text1.txt")
img1 = ImageFile("img1.png")
text2 = TextFile("text2.txt")

folder1 = Folder("f1")
folder1.add_file(text1)
folder1.add_file(img1)

# folder1.read()

folder2 = Folder("f2")
folder2.add_file(folder1)
folder2.add_file(text2)

folder2.read()
