from typing import Dict, Any, List, Optional
from crewai import Agent, Task, Crew
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class request_confirmatory_testing_part1_crew:
    """Crew for request_confirmatory_testing_part1 operations."""


    @agent
    def request_confirmatory_testing_part1_agent(self):
        return Agent(
            role="Request Confirmatory Testing Part1 Specialist",
            goal="Execute request_confirmatory_testing_part1 task accurately",
            backstory="You are a specialized worker focused on Primary confirmation strategy",
            verbose=True
        )



    @task
    def request_confirmatory_testing_part1_task(self):
        """Task for request_confirmatory_testing_part1."""
        agent = self.request_confirmatory_testing_part1_agent()
        return Task(
            description="""Using {generate_diagnostic_summary_part2_output}, Primary confirmation strategy""",
            agent=agent,
            expected_output="Provide output that best addresses the task requirements",
            verbose=True
        )


    @crew
    # @traceable
    def crew(self):
        """Create the crew instance."""
        return Crew(
            agents=[self.request_confirmatory_testing_part1_agent()],
            tasks=[self.request_confirmatory_testing_part1_task()],
            verbose=True
        )
