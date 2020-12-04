class Workout:
    def __init__(self, _id: str, creator_id: str, name: str, difficulty: str = "novice", about: str = None, exp: int = 0):
        """Constructor for Workout class."""
        self._id = _id
        self.creator_id = creator_id
        self.name = name
        self.difficulty = difficulty
        self.about = about
        self.exp = exp

    def __repr__(self):
        """Returns all attributes of the Workout class as a dictionary."""
        return f'Workout({self._id}, {self.creator_id}, {self.name}, {self.difficulty}, {self.about}, {self.exp})'

    def as_dict(self):
        """Returns all attributes of the Workout class as a dictionary."""
        return dict(self.__dict__)
