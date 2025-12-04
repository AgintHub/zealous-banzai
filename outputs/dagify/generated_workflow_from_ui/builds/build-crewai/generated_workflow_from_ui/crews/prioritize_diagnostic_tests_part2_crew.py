from typing import Dict, Any, List, Optional
from crewai import Agent, Task, Crew
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class prioritize_diagnostic_tests_part2_crew:
    """Crew for prioritize_diagnostic_tests_part2 operations."""


    @agent
    def prioritize_diagnostic_tests_part2_agent(self):
        return Agent(
            role="Prioritize Diagnostic Tests Part2 Specialist",
            goal="Execute prioritize_diagnostic_tests_part2 task accurately",
            backstory="You are a specialized worker focused on Test cost-effectiveness optimization",
            verbose=True
        )



    @task
    def prioritize_diagnostic_tests_part2_task(self):
        """Task for prioritize_diagnostic_tests_part2."""
        agent = self.prioritize_diagnostic_tests_part2_agent()
        return Task(
            description="""Using {merge_initial_hypotheses_part2_output}, Test cost-effectiveness optimization""",
            agent=agent,
            expected_output="Provide output that best addresses the task requirements",
            verbose=True
        )


    @crew
    # @traceable
    def crew(self):
        """Create the crew instance."""
        return Crew(
            agents=[self.prioritize_diagnostic_tests_part2_agent()],
            tasks=[self.prioritize_diagnostic_tests_part2_task()],
            verbose=True
        )
