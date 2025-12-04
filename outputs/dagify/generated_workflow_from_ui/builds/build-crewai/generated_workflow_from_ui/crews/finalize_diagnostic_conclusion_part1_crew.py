from typing import Dict, Any, List, Optional
from crewai import Agent, Task, Crew
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class finalize_diagnostic_conclusion_part1_crew:
    """Crew for finalize_diagnostic_conclusion_part1 operations."""


    @agent
    def finalize_diagnostic_conclusion_part1_agent(self):
        return Agent(
            role="Finalize Diagnostic Conclusion Part1 Specialist",
            goal="Execute finalize_diagnostic_conclusion_part1 task accurately",
            backstory="You are a specialized worker focused on Core conclusion documentation",
            verbose=True
        )



    @task
    def finalize_diagnostic_conclusion_part1_task(self):
        """Task for finalize_diagnostic_conclusion_part1."""
        agent = self.finalize_diagnostic_conclusion_part1_agent()
        return Task(
            description="""Using {generate_diagnostic_summary_part2_output}, {request_confirmatory_testing_part2_output}, Core conclusion documentation""",
            agent=agent,
            expected_output="Provide output that best addresses the task requirements",
            verbose=True
        )


    @crew
    # @traceable
    def crew(self):
        """Create the crew instance."""
        return Crew(
            agents=[self.finalize_diagnostic_conclusion_part1_agent()],
            tasks=[self.finalize_diagnostic_conclusion_part1_task()],
            verbose=True
        )
