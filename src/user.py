class UserProfile:
    def __init__(self, name: str, goal: str, preferences: str, allergies: str):
        self.name = name
        self.goal = goal
        self.preferences = preferences
        self.allergies = allergies

    def __str__(self):
        return (f"User Profile:\nName: {self.name}\nGoal: {self.goal}\n"
                f"Preferences: {self.preferences}\nAllergies: {self.allergies}")