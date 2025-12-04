from typing import Dict, Any, List, Optional
from crewai import Agent, Task, Crew
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class merge_initial_hypotheses_part1_crew:
    """Crew for merge_initial_hypotheses_part1 operations."""


    @agent
    def merge_initial_hypotheses_part1_agent(self):
        return Agent(
            role="Merge Initial Hypotheses Part1 Specialist",
            goal="Execute merge_initial_hypotheses_part1 task accurately",
            backstory="You are a specialized worker focused on Baseline hypothesis consolidation",
            verbose=True
        )



    @task
    def merge_initial_hypotheses_part1_task(self):
        """Task for merge_initial_hypotheses_part1."""
        agent = self.merge_initial_hypotheses_part1_agent()
        return Task(
            description="""Using {generate_symptom_hypotheses_part2_output}, {generate_history_hypotheses_part1_output}, Baseline hypothesis consolidation""",
            agent=agent,
            expected_output="Provide output that best addresses the task requirements",
            verbose=True
        )


    @crew
    # @traceable
    def crew(self):
        """Create the crew instance."""
        return Crew(
            agents=[self.merge_initial_hypotheses_part1_agent()],
            tasks=[self.merge_initial_hypotheses_part1_task()],
            verbose=True
        )
