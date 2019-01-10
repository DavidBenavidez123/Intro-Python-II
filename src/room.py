# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, title, description):
        self.title = title
        self.description = description
    def __repr__(self):
        return f"\n{self.title}: {self.description}"