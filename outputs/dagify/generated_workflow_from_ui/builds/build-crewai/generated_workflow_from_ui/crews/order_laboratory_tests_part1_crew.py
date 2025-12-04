from typing import Dict, Any, List, Optional
from crewai import Agent, Task, Crew
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class order_laboratory_tests_part1_crew:
    """Crew for order_laboratory_tests_part1 operations."""


    @agent
    def order_laboratory_tests_part1_agent(self):
        return Agent(
            role="Order Laboratory Tests Part1 Specialist",
            goal="Execute order_laboratory_tests_part1 task accurately",
            backstory="You are a specialized worker focused on Core lab test protocol design",
            verbose=True
        )



    @task
    def order_laboratory_tests_part1_task(self):
        """Task for order_laboratory_tests_part1."""
        agent = self.order_laboratory_tests_part1_agent()
        return Task(
            description="""Using {prioritize_diagnostic_tests_part2_output}, Core lab test protocol design""",
            agent=agent,
            expected_output="Provide output that best addresses the task requirements",
            verbose=True
        )


    @crew
    # @traceable
    def crew(self):
        """Create the crew instance."""
        return Crew(
            agents=[self.order_laboratory_tests_part1_agent()],
            tasks=[self.order_laboratory_tests_part1_task()],
            verbose=True
        )
