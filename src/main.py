from dietary_guidelines import DietaryGuidelines
from grocey_gen import GroceryListGenerator
from user import UserProfile
from pdf_extractor import PDFExtractor
from meal_gen import MealPlanGenerator
from langchain_community.llms import GPT4All

class MealPlannerApp:
    def __init__(self, pdf_path: str, llm_model="Nous-Hermes-2-Mistral-7B-DPO.Q4_0.gguf"):
        # Initialize components
        self.pdf_extractor = PDFExtractor(pdf_path)
        self.dietary_guidelines = None
        self.user_profile = None
        self.llm = GPT4All(model=llm_model, streaming=True)
        self.meal_plan_generator = None
        self.grocery_list_generator = GroceryListGenerator(self.llm)

    def load_guidelines(self):
        guidelines_text = self.pdf_extractor.extract_text()
        self.dietary_guidelines = DietaryGuidelines(guidelines_text)
        self.meal_plan_generator = MealPlanGenerator(self.dietary_guidelines, self.llm)

    def set_user_profile(self, name: str, goal: str, preferences: str, allergies: str):
        self.user_profile = UserProfile(name, goal, preferences, allergies)

    def create_meal_plan(self):
        if self.user_profile and self.meal_plan_generator:
            return self.meal_plan_generator.generate_meal_plan(self.user_profile)
        else:
            raise Exception("User profile or dietary guidelines are not set.")

    def create_grocery_list(self, meal_plan: str):
        return self.grocery_list_generator.generate_grocery_list(meal_plan)

    def run(self, name: str, goal: str, preferences: str, allergies: str):
        # Load guidelines
        print("Loading dietary guidelines...")
        self.load_guidelines()
        print("Guidelines loaded successfully.")

        # Set user profile
        print("Setting user profile...")
        self.set_user_profile(name, goal, preferences, allergies)
        print("User profile set.")

        # Generate meal plan
        print("Generating meal plan...")
        meal_plan = self.create_meal_plan()
        print("Meal Plan:\n", meal_plan)

        # Generate grocery list
        print("Generating grocery list...")
        grocery_list = self.create_grocery_list(meal_plan)
        print("Grocery List:\n", grocery_list)


# Example Usage
if __name__ == "__main__":
    # Initialize app with path to dietary guidelines PDF
    pdf_path = "resources\Dieta antiossidanteipo.pdf"
    app = MealPlannerApp(pdf_path)

    # Run app with user input
    app.run(
        name="Maximiliano",
        goal="Weight loss",
        preferences="high protein, low carb",
        allergies=""
    )