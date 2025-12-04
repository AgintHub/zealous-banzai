from typing import Dict, Any, List, Optional
from crewai import Agent, Task, Crew
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class categorize_diagnostic_pathway_part2_crew:
    """Crew for categorize_diagnostic_pathway_part2 operations."""


    @agent
    def categorize_diagnostic_pathway_part2_agent(self):
        return Agent(
            role="Categorize Diagnostic Pathway Part2 Specialist",
            goal="Execute categorize_diagnostic_pathway_part2 task accurately",
            backstory="You are a specialized worker focused on Quantify pathway validation parameters",
            verbose=True
        )



    @task
    def categorize_diagnostic_pathway_part2_task(self):
        """Task for categorize_diagnostic_pathway_part2."""
        agent = self.categorize_diagnostic_pathway_part2_agent()
        return Task(
            description="""Using {update_differential_diagnosis_part2_output}, Quantify pathway validation parameters""",
            agent=agent,
            expected_output="Provide output that best addresses the task requirements",
            verbose=True
        )


    @crew
    # @traceable
    def crew(self):
        """Create the crew instance."""
        return Crew(
            agents=[self.categorize_diagnostic_pathway_part2_agent()],
            tasks=[self.categorize_diagnostic_pathway_part2_task()],
            verbose=True
        )
