from typing import Dict, Any, List, Optional
from crewai import Agent, Task, Crew
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class gather_patient_history_part2_crew:
    """Crew for gather_patient_history_part2 operations."""


    @agent
    def gather_patient_history_part2_agent(self):
        return Agent(
            role="Gather Patient History Part2 Specialist",
            goal="Execute gather_patient_history_part2 task accurately",
            backstory="You are a specialized worker focused on History pattern recognition",
            verbose=True
        )



    @task
    def gather_patient_history_part2_task(self):
        """Task for gather_patient_history_part2."""
        agent = self.gather_patient_history_part2_agent()
        return Task(
            description="""Using {input}, History pattern recognition""",
            agent=agent,
            expected_output="Provide output that best addresses the task requirements",
            verbose=True
        )


    @crew
    # @traceable
    def crew(self):
        """Create the crew instance."""
        return Crew(
            agents=[self.gather_patient_history_part2_agent()],
            tasks=[self.gather_patient_history_part2_task()],
            verbose=True
        )
