from typing import Dict, Any, List, Optional
from crewai import Agent, Task, Crew
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class prioritize_diagnostic_tests_part1_crew:
    """Crew for prioritize_diagnostic_tests_part1 operations."""


    @agent
    def prioritize_diagnostic_tests_part1_agent(self):
        return Agent(
            role="Prioritize Diagnostic Tests Part1 Specialist",
            goal="Execute prioritize_diagnostic_tests_part1 task accurately",
            backstory="You are a specialized worker focused on Core test hierarchy creation",
            verbose=True
        )



    @task
    def prioritize_diagnostic_tests_part1_task(self):
        """Task for prioritize_diagnostic_tests_part1."""
        agent = self.prioritize_diagnostic_tests_part1_agent()
        return Task(
            description="""Using {merge_initial_hypotheses_part2_output}, Core test hierarchy creation""",
            agent=agent,
            expected_output="Provide output that best addresses the task requirements",
            verbose=True
        )


    @crew
    # @traceable
    def crew(self):
        """Create the crew instance."""
        return Crew(
            agents=[self.prioritize_diagnostic_tests_part1_agent()],
            tasks=[self.prioritize_diagnostic_tests_part1_task()],
            verbose=True
        )
