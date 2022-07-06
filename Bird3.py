class Bird:
    """Un oiseau. 🐦"""

    @staticmethod
    def get_definition():
        """Donne la définition d'un oiseau."""
        return (
        "Animal (vertébré à sang chaud) au corps recouvert de plumes, "
        "dont les membres antérieurs sont des ailes et qui a un bec."
        )

print(Bird.get_definition())