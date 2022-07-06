class Bird:
    """Un oiseau. 🐦"""

    def __init__(self):
        """Les attributs définis ici sont des attributs d'instance."""
        self.wings = 2

    def fly(self):
        """Cette méthode est une méthode d'instance."""
        print("Je vole !")


bird = Bird()  # obligation d'instancier un oiseau pour utiliser ses attributs
bird.wings
bird.fly()