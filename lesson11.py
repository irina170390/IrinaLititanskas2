from abc import ABC, abstractmethod
class Museum(ABC):

    def __init__(self,name, painting: int, sculpture: int, installation: int):
        self.__name = name
        self.painting = painting
        self.sculpture = sculpture
        self.installation = installation

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):

     @abstractmethod
     def add_painting(self):
         pass

     @staticmethod
     def painting_between_sculpture(painting, sculpture):
         new_painting = painting / sculpture
         return new_painting


class Artwork:

    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

    def display(self):
        print(f"Displaying {self.title} by {self.artist}")

    def clean(self):
        print(f"Cleaning {self.title} by {self.artist}")

    def protect(self):
        print(f"Protecting {self.title} by {self.artist}")

    def maintain(self):
        print(f"Maintaining {self.title} by {self.artist}")


    class IArtwork(ABC):
        """interface of artwork"""

        @abstractmethod
        def display(self):
            """"""

        @abstractmethod
        def accept(self, visitor):
            """"""

class Painting(Artwork):

    def __init__(self, title, artist):
        super().__init__(title, artist)

    def protect(self):
        print(f"Protecting {self.title} by {self.artist}")


class Sculpture(Artwork):

    def __init__(self, title, artist):
        super().__init__(title, artist)

    def clean(self):
        print(f"Cleaning {self.title} by {self.artist}")


class Installation(Artwork):

    def __init__(self, title, artist):
        super().__init__(title, artist)

    def maintain(self):
        print(f"Maintaining {self.title} by {self.artist}")


class Museum:
    """object structure"""

    def __init__(self):
        self.artworks = []

    def add_artwork(self, artwork: Artwork):
        """adds artworks to its list"""
        self.artworks.append(artwork)

    def get_artworks(self):
        """get function of artwork list"""
        return self.artworks

    def accept(self):
        """accepts a visitor and passes it to each artwork object"""
        for artwork in self.artworks:
            artwork.accept()

def run_a_museum():
    # create objects
    painting = Painting("No1","Mark Rothko")
    sculpture = Sculpture("David", "Michelangelo")
    installation = Installation("La Menesunda","Marta Minujín")
    # create museum
    museum = Museum()
    museum.add_artwork(painting)
    museum.add_artwork(sculpture)
    museum.add_artwork(installation)

    arts = Museum.get_artworks()
    for art in arts:
         art.display()
    if isinstance(art, Painting):
         art.protect()
    elif isinstance(art, Sculpture):
         art.clean()
    elif isinstance(art, Installation):
         art.maintain()
         run_a_museum()





