from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain

from user import UserProfile
from dietary_guidelines import DietaryGuidelines

class MealPlanGenerator:
    def __init__(self, dietary_guidelines: DietaryGuidelines, llm):
        self.dietary_guidelines = dietary_guidelines
        self.llm = llm
        self.prompt_template = """
        You are a nutrition assistant with access to the following dietary guidelines:

        {guidelines}

        Based on these guidelines, create a weekly meal plan for a user with the following details:
        - Goal: {goal}
        - Dietary Preferences: {preferences}
        - Allergies: {allergies}

        Provide a daily breakdown, including meal names and basic nutritional information.
        """
        self.prompt = PromptTemplate(template=self.prompt_template,
                                     input_variables=["guidelines", "goal", "preferences", "allergies"])

    def generate_meal_plan(self, user_profile: UserProfile) -> str:
        chain = LLMChain(prompt=self.prompt, llm=self.llm)
        inputs = {
            "guidelines": self.dietary_guidelines.content,
            "goal": user_profile.goal,
            "preferences": user_profile.preferences,
            "allergies": user_profile.allergies
        }
        return chain.run(inputs)