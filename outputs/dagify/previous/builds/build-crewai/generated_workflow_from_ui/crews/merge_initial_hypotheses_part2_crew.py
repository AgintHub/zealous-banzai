from typing import Dict, Any, List, Optional
from crewai import Agent, Task, Crew
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class merge_initial_hypotheses_part2_crew:
    """Crew for merge_initial_hypotheses_part2 operations."""


    @agent
    def merge_initial_hypotheses_part2_agent(self):
        return Agent(
            role="Merge Initial Hypotheses Part2 Specialist",
            goal="Execute merge_initial_hypotheses_part2 task accurately",
            backstory="You are a specialized worker focused on Hypothesis decision validation",
            verbose=True
        )



    @task
    def merge_initial_hypotheses_part2_task(self):
        """Task for merge_initial_hypotheses_part2."""
        agent = self.merge_initial_hypotheses_part2_agent()
        return Task(
            description="""Using {generate_symptom_hypotheses_part2_output}, {generate_history_hypotheses_part1_output}, Hypothesis decision validation""",
            agent=agent,
            expected_output="Provide output that best addresses the task requirements",
            verbose=True
        )


    @crew
    # @traceable
    def crew(self):
        """Create the crew instance."""
        return Crew(
            agents=[self.merge_initial_hypotheses_part2_agent()],
            tasks=[self.merge_initial_hypotheses_part2_task()],
            verbose=True
        )
