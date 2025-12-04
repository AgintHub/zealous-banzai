from typing import Dict, Any, List, Optional
from crewai import Agent, Task, Crew
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class generate_diagnostic_summary_part1_crew:
    """Crew for generate_diagnostic_summary_part1 operations."""


    @agent
    def generate_diagnostic_summary_part1_agent(self):
        return Agent(
            role="Generate Diagnostic Summary Part1 Specialist",
            goal="Execute generate_diagnostic_summary_part1 task accurately",
            backstory="You are a specialized worker focused on Primary conclusion framework",
            verbose=True
        )



    @task
    def generate_diagnostic_summary_part1_task(self):
        """Task for generate_diagnostic_summary_part1."""
        agent = self.generate_diagnostic_summary_part1_agent()
        return Task(
            description="""Using {update_differential_diagnosis_part2_output}, {categorize_diagnostic_pathway_part1_output}, Primary conclusion framework""",
            agent=agent,
            expected_output="Provide output that best addresses the task requirements",
            verbose=True
        )


    @crew
    # @traceable
    def crew(self):
        """Create the crew instance."""
        return Crew(
            agents=[self.generate_diagnostic_summary_part1_agent()],
            tasks=[self.generate_diagnostic_summary_part1_task()],
            verbose=True
        )
