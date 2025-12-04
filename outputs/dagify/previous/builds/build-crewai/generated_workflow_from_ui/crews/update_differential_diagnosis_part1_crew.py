from typing import Dict, Any, List, Optional
from crewai import Agent, Task, Crew
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class update_differential_diagnosis_part1_crew:
    """Crew for update_differential_diagnosis_part1 operations."""


    @agent
    def update_differential_diagnosis_part1_agent(self):
        return Agent(
            role="Update Differential Diagnosis Part1 Specialist",
            goal="Execute update_differential_diagnosis_part1 task accurately",
            backstory="You are a specialized worker focused on Primary differential refinement",
            verbose=True
        )



    @task
    def update_differential_diagnosis_part1_task(self):
        """Task for update_differential_diagnosis_part1."""
        agent = self.update_differential_diagnosis_part1_agent()
        return Task(
            description="""Using {analyze_laboratory_results_part1_output}, {review_imaging_findings_part1_output}, {compile_specialist_input_part1_output}, Primary differential refinement""",
            agent=agent,
            expected_output="Provide output that best addresses the task requirements",
            verbose=True
        )


    @crew
    # @traceable
    def crew(self):
        """Create the crew instance."""
        return Crew(
            agents=[self.update_differential_diagnosis_part1_agent()],
            tasks=[self.update_differential_diagnosis_part1_task()],
            verbose=True
        )
