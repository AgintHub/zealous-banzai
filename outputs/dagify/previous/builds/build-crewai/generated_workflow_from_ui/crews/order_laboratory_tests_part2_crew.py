from typing import Dict, Any, List, Optional
from crewai import Agent, Task, Crew
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class order_laboratory_tests_part2_crew:
    """Crew for order_laboratory_tests_part2 operations."""


    @agent
    def order_laboratory_tests_part2_agent(self):
        return Agent(
            role="Order Laboratory Tests Part2 Specialist",
            goal="Execute order_laboratory_tests_part2 task accurately",
            backstory="You are a specialized worker focused on Lab protocol validation",
            verbose=True
        )



    @task
    def order_laboratory_tests_part2_task(self):
        """Task for order_laboratory_tests_part2."""
        agent = self.order_laboratory_tests_part2_agent()
        return Task(
            description="""Using {prioritize_diagnostic_tests_part2_output}, Lab protocol validation""",
            agent=agent,
            expected_output="Provide output that best addresses the task requirements",
            verbose=True
        )


    @crew
    # @traceable
    def crew(self):
        """Create the crew instance."""
        return Crew(
            agents=[self.order_laboratory_tests_part2_agent()],
            tasks=[self.order_laboratory_tests_part2_task()],
            verbose=True
        )
