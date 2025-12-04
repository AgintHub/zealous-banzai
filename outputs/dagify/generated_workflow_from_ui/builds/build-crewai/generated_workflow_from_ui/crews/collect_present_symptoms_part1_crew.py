from typing import Dict, Any, List, Optional
from crewai import Agent, Task, Crew
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class collect_present_symptoms_part1_crew:
    """Crew for collect_present_symptoms_part1 operations."""


    @agent
    def collect_present_symptoms_part1_agent(self):
        return Agent(
            role="Collect Present Symptoms Part1 Specialist",
            goal="Execute collect_present_symptoms_part1 task accurately",
            backstory="You are a specialized worker focused on Systemic symptom inventory",
            verbose=True
        )



    @task
    def collect_present_symptoms_part1_task(self):
        """Task for collect_present_symptoms_part1."""
        agent = self.collect_present_symptoms_part1_agent()
        return Task(
            description="""Using {input}, Systemic symptom inventory""",
            agent=agent,
            expected_output="Provide output that best addresses the task requirements",
            verbose=True
        )


    @crew
    # @traceable
    def crew(self):
        """Create the crew instance."""
        return Crew(
            agents=[self.collect_present_symptoms_part1_agent()],
            tasks=[self.collect_present_symptoms_part1_task()],
            verbose=True
        )
