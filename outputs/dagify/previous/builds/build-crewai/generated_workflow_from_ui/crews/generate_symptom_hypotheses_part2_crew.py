from typing import Dict, Any, List, Optional
from crewai import Agent, Task, Crew
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class generate_symptom_hypotheses_part2_crew:
    """Crew for generate_symptom_hypotheses_part2 operations."""


    @agent
    def generate_symptom_hypotheses_part2_agent(self):
        return Agent(
            role="Generate Symptom Hypotheses Part2 Specialist",
            goal="Execute generate_symptom_hypotheses_part2 task accurately",
            backstory="You are a specialized worker focused on Symptom pattern validation",
            verbose=True
        )



    @task
    def generate_symptom_hypotheses_part2_task(self):
        """Task for generate_symptom_hypotheses_part2."""
        agent = self.generate_symptom_hypotheses_part2_agent()
        return Task(
            description="""Using {collect_present_symptoms_part2_output}, Symptom pattern validation""",
            agent=agent,
            expected_output="Provide output that best addresses the task requirements",
            verbose=True
        )


    @crew
    # @traceable
    def crew(self):
        """Create the crew instance."""
        return Crew(
            agents=[self.generate_symptom_hypotheses_part2_agent()],
            tasks=[self.generate_symptom_hypotheses_part2_task()],
            verbose=True
        )
