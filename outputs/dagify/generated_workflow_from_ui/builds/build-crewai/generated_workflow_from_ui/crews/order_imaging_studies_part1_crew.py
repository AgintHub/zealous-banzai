from typing import Dict, Any, List, Optional
from crewai import Agent, Task, Crew
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class order_imaging_studies_part1_crew:
    """Crew for order_imaging_studies_part1 operations."""


    @agent
    def order_imaging_studies_part1_agent(self):
        return Agent(
            role="Order Imaging Studies Part1 Specialist",
            goal="Execute order_imaging_studies_part1 task accurately",
            backstory="You are a specialized worker focused on Primary imaging protocol selection",
            verbose=True
        )



    @task
    def order_imaging_studies_part1_task(self):
        """Task for order_imaging_studies_part1."""
        agent = self.order_imaging_studies_part1_agent()
        return Task(
            description="""Using {prioritize_diagnostic_tests_part2_output}, Primary imaging protocol selection""",
            agent=agent,
            expected_output="Provide output that best addresses the task requirements",
            verbose=True
        )


    @crew
    # @traceable
    def crew(self):
        """Create the crew instance."""
        return Crew(
            agents=[self.order_imaging_studies_part1_agent()],
            tasks=[self.order_imaging_studies_part1_task()],
            verbose=True
        )
