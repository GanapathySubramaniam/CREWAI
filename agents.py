from crewai import Agent
from tools import tool
from LLMS.CHATGPT import chatgpt

class agents:
    def __init__(self):
        self.llm = chatgpt
        

    def trend_analyzer(self):
        return Agent(
            role="Trend Analyst",
            goal="Analyze the latest trends in {topic}",
            verbose=True,
            memory=True,
            backstory=(
                "You're a trendsetter, always ahead of the curve, analyzing"
                "the latest developments in {topic} to predict what's next."
            ),
            tools=[tool],
            llm=self.llm,
            allow_delegation=True
        )
    
    def market_analyst(self):
        return Agent(
            role="Market Analyst",
            goal="Analyze the market for {topic}",
            verbose=True,
            memory=True,
            backstory=(
                "With a keen eye for detail, you analyze market trends and"
                "consumer behavior to identify opportunities in {topic}."
            ),
            tools=[tool],
            llm=self.llm,
            allow_delegation=True
        )
    
    def product_manager(self):
        return Agent(
            role="Product Manager",
            goal="Develop a new product for {topic}",
            verbose=True,
            memory=True,
            backstory=(
                "As a product manager, you're responsible for developing new"
                "products that meet the needs of customers in {topic}."
            ),
            tools=[tool],
            llm=self.llm,
            allow_delegation=True
        )




