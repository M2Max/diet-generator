# DietaryGuidelines Class
class DietaryGuidelines:
    def __init__(self, content: str):
        self.content = content

    def __str__(self):
        return f"Dietary Guidelines:\n{self.content[:500]}..."  # Preview of the content
