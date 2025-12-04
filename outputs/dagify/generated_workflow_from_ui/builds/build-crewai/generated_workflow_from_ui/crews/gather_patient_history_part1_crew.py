from typing import Dict, Any, List, Optional
from crewai import Agent, Task, Crew
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class gather_patient_history_part1_crew:
    """Crew for gather_patient_history_part1 operations."""


    @agent
    def gather_patient_history_part1_agent(self):
        return Agent(
            role="Gather Patient History Part1 Specialist",
            goal="Execute gather_patient_history_part1 task accurately",
            backstory="You are a specialized worker focused on Primary history compilation",
            verbose=True
        )



    @task
    def gather_patient_history_part1_task(self):
        """Task for gather_patient_history_part1."""
        agent = self.gather_patient_history_part1_agent()
        return Task(
            description="""Using {input}, Primary history compilation""",
            agent=agent,
            expected_output="Provide output that best addresses the task requirements",
            verbose=True
        )


    @crew
    # @traceable
    def crew(self):
        """Create the crew instance."""
        return Crew(
            agents=[self.gather_patient_history_part1_agent()],
            tasks=[self.gather_patient_history_part1_task()],
            verbose=True
        )
