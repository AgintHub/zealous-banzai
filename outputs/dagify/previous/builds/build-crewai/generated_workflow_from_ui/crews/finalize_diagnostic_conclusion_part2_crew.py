from typing import Dict, Any, List, Optional
from crewai import Agent, Task, Crew
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class finalize_diagnostic_conclusion_part2_crew:
    """Crew for finalize_diagnostic_conclusion_part2 operations."""


    @agent
    def finalize_diagnostic_conclusion_part2_agent(self):
        return Agent(
            role="Finalize Diagnostic Conclusion Part2 Specialist",
            goal="Execute finalize_diagnostic_conclusion_part2 task accurately",
            backstory="You are a specialized worker focused on Diagnostic path validation",
            verbose=True
        )



    @task
    def finalize_diagnostic_conclusion_part2_task(self):
        """Task for finalize_diagnostic_conclusion_part2."""
        agent = self.finalize_diagnostic_conclusion_part2_agent()
        return Task(
            description="""Using {generate_diagnostic_summary_part2_output}, {request_confirmatory_testing_part2_output}, Diagnostic path validation""",
            agent=agent,
            expected_output="Provide output that best addresses the task requirements",
            verbose=True
        )


    @crew
    # @traceable
    def crew(self):
        """Create the crew instance."""
        return Crew(
            agents=[self.finalize_diagnostic_conclusion_part2_agent()],
            tasks=[self.finalize_diagnostic_conclusion_part2_task()],
            verbose=True
        )
