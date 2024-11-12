from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain

class GroceryListGenerator:
    def __init__(self, llm):
        self.llm = llm
        self.grocery_list_prompt = """
        Based on the following meal plan:

        {meal_plan}

        Generate a comprehensive grocery list, organized by food category (e.g., produce, grains, proteins).
        """

    def generate_grocery_list(self, meal_plan: str) -> str:
        prompt = PromptTemplate(template=self.grocery_list_prompt, input_variables=["meal_plan"])
        chain = LLMChain(prompt=prompt, llm=self.llm)
        return chain.run({"meal_plan": meal_plan})