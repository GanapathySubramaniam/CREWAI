from crewai import Task
from tools import tool
from agents import agents

class tasks:
    def __init__(self):
        self.agents = agents()

    def analyze_trend(self):
        return Task(
            description=(
                "Analyze the latest trends in {topic}."
                "Focus on identifying key patterns and potential opportunities."
                "Your analysis should be data-driven and forward-looking."
            ),
            expected_output="A detailed report on the latest trends in {topic}.",
            tools=[tool],
            agent=self.agents.trend_analyzer()
        )
    
    def analyze_market(self):
        return Task(
            description=(
                "Analyze the market for {topic}."
                "Identify key market segments, competitors, and growth opportunities."
                "Your analysis should provide actionable insights for decision-making."
            ),
            expected_output="A comprehensive market analysis report for {topic}.",
            tools=[tool],
            agent=self.agents.market_analyst()
        )
    
    def develop_product(self):
        return Task(
            description=(
                "Develop a new product for {topic}."
                "Identify customer needs, define product features, and create a roadmap."
                "Your product should be innovative and address a gap in the market."
            ),
            expected_output="A product proposal document for a new {topic} product.",
            tools=[tool],
            agent=self.agents.product_manager(),
            output_file='Proposal.md'
        )
