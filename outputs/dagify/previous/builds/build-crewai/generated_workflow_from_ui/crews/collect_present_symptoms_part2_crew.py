from typing import Dict, Any, List, Optional
from crewai import Agent, Task, Crew
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class collect_present_symptoms_part2_crew:
    """Crew for collect_present_symptoms_part2 operations."""


    @agent
    def collect_present_symptoms_part2_agent(self):
        return Agent(
            role="Collect Present Symptoms Part2 Specialist",
            goal="Execute collect_present_symptoms_part2 task accurately",
            backstory="You are a specialized worker focused on Symptom system mapping",
            verbose=True
        )



    @task
    def collect_present_symptoms_part2_task(self):
        """Task for collect_present_symptoms_part2."""
        agent = self.collect_present_symptoms_part2_agent()
        return Task(
            description="""Using {input}, Symptom system mapping""",
            agent=agent,
            expected_output="Provide output that best addresses the task requirements",
            verbose=True
        )


    @crew
    # @traceable
    def crew(self):
        """Create the crew instance."""
        return Crew(
            agents=[self.collect_present_symptoms_part2_agent()],
            tasks=[self.collect_present_symptoms_part2_task()],
            verbose=True
        )
