from crewai import Crew, Process
from tasks import tasks
from agents import agents

agents = agents()
tasks = tasks()

crew= Crew(
    agents=[agents.trend_analyzer(), agents.market_analyst(), agents.product_manager()],
    tasks=[tasks.analyze_trend(), tasks.analyze_market(), tasks.develop_product()],
    process=Process.sequential
)



