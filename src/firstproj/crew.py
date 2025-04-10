from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class StockMarketAnalysisCrew:
    """Crew AI setup for Indian Stock Market Analysis"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def stock_market_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['stock_market_analyst'],
            verbose=True
        )

    @agent
    def reporting_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['reporting_analyst'],
            verbose=True
        )

    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_task']
        )

    @task
    def reporting_task(self) -> Task:
        return Task(
            config=self.tasks_config['reporting_task'],
            output_file='outputs/market_report.md'
        )

    @task
    def stock_recommendation_task(self) -> Task:
        return Task(
            config=self.tasks_config['stock_recommendation_task'],
            output_file='outputs/stock_recommendations.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Indian Stock Market Analysis crew"""

        return Crew(
            agents=self.agents,  # list of all agent functions marked with @agent
            tasks=self.tasks,    # list of all task functions marked with @task
            process=Process.sequential,  # can also use .hierarchical
            verbose=True
        )
