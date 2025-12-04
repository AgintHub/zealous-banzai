from typing import Dict, Any, List, Optional
from crewai import Agent, Task, Crew
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class request_confirmatory_testing_part2_crew:
    """Crew for request_confirmatory_testing_part2 operations."""


    @agent
    def request_confirmatory_testing_part2_agent(self):
        return Agent(
            role="Request Confirmatory Testing Part2 Specialist",
            goal="Execute request_confirmatory_testing_part2 task accurately",
            backstory="You are a specialized worker focused on Test validation framework",
            verbose=True
        )



    @task
    def request_confirmatory_testing_part2_task(self):
        """Task for request_confirmatory_testing_part2."""
        agent = self.request_confirmatory_testing_part2_agent()
        return Task(
            description="""Using {generate_diagnostic_summary_part2_output}, Test validation framework""",
            agent=agent,
            expected_output="Provide output that best addresses the task requirements",
            verbose=True
        )


    @crew
    # @traceable
    def crew(self):
        """Create the crew instance."""
        return Crew(
            agents=[self.request_confirmatory_testing_part2_agent()],
            tasks=[self.request_confirmatory_testing_part2_task()],
            verbose=True
        )
