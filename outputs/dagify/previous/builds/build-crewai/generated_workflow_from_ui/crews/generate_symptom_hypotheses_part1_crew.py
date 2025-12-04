from typing import Dict, Any, List, Optional
from crewai import Agent, Task, Crew
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class generate_symptom_hypotheses_part1_crew:
    """Crew for generate_symptom_hypotheses_part1 operations."""


    @agent
    def generate_symptom_hypotheses_part1_agent(self):
        return Agent(
            role="Generate Symptom Hypotheses Part1 Specialist",
            goal="Execute generate_symptom_hypotheses_part1 task accurately",
            backstory="You are a specialized worker focused on Symptom differential framework",
            verbose=True
        )



    @task
    def generate_symptom_hypotheses_part1_task(self):
        """Task for generate_symptom_hypotheses_part1."""
        agent = self.generate_symptom_hypotheses_part1_agent()
        return Task(
            description="""Using {collect_present_symptoms_part2_output}, Symptom differential framework""",
            agent=agent,
            expected_output="Provide output that best addresses the task requirements",
            verbose=True
        )


    @crew
    # @traceable
    def crew(self):
        """Create the crew instance."""
        return Crew(
            agents=[self.generate_symptom_hypotheses_part1_agent()],
            tasks=[self.generate_symptom_hypotheses_part1_task()],
            verbose=True
        )
