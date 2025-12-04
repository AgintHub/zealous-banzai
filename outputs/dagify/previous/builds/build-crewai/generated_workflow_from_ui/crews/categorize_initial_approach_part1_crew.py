from typing import Dict, Any, List, Optional
from crewai import Agent, Task, Crew
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class categorize_initial_approach_part1_crew:
    """Crew for categorize_initial_approach_part1 operations."""


    @agent
    def categorize_initial_approach_part1_agent(self):
        return Agent(
            role="Categorize Initial Approach Part1 Specialist",
            goal="Execute categorize_initial_approach_part1 task accurately",
            backstory="You are a specialized worker focused on Define core approach classification",
            verbose=True
        )



    @task
    def categorize_initial_approach_part1_task(self):
        """Task for categorize_initial_approach_part1."""
        agent = self.categorize_initial_approach_part1_agent()
        return Task(
            description="""Using {merge_initial_hypotheses_part2_output}, Define core approach classification""",
            agent=agent,
            expected_output="Provide output that best addresses the task requirements",
            verbose=True
        )


    @crew
    # @traceable
    def crew(self):
        """Create the crew instance."""
        return Crew(
            agents=[self.categorize_initial_approach_part1_agent()],
            tasks=[self.categorize_initial_approach_part1_task()],
            verbose=True
        )
