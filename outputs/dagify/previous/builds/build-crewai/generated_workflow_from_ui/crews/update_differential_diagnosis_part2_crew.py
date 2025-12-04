from typing import Dict, Any, List, Optional
from crewai import Agent, Task, Crew
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class update_differential_diagnosis_part2_crew:
    """Crew for update_differential_diagnosis_part2 operations."""


    @agent
    def update_differential_diagnosis_part2_agent(self):
        return Agent(
            role="Update Differential Diagnosis Part2 Specialist",
            goal="Execute update_differential_diagnosis_part2 task accurately",
            backstory="You are a specialized worker focused on Differential decision validation",
            verbose=True
        )



    @task
    def update_differential_diagnosis_part2_task(self):
        """Task for update_differential_diagnosis_part2."""
        agent = self.update_differential_diagnosis_part2_agent()
        return Task(
            description="""Using {analyze_laboratory_results_part2_output}, {review_imaging_findings_part2_output}, {compile_specialist_input_part2_output}, Differential decision validation""",
            agent=agent,
            expected_output="Provide output that best addresses the task requirements",
            verbose=True
        )


    @crew
    # @traceable
    def crew(self):
        """Create the crew instance."""
        return Crew(
            agents=[self.update_differential_diagnosis_part2_agent()],
            tasks=[self.update_differential_diagnosis_part2_task()],
            verbose=True
        )
