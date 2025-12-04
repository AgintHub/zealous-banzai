from typing import Dict, Any, List, Optional
from crewai import Agent, Task, Crew
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class review_imaging_findings_part1_crew:
    """Crew for review_imaging_findings_part1 operations."""


    @agent
    def review_imaging_findings_part1_agent(self):
        return Agent(
            role="Review Imaging Findings Part1 Specialist",
            goal="Execute review_imaging_findings_part1 task accurately",
            backstory="You are a specialized worker focused on Primary imaging analysis",
            verbose=True
        )



    @task
    def review_imaging_findings_part1_task(self):
        """Task for review_imaging_findings_part1."""
        agent = self.review_imaging_findings_part1_agent()
        return Task(
            description="""Using {order_imaging_studies_part2_output}, Primary imaging analysis""",
            agent=agent,
            expected_output="Provide output that best addresses the task requirements",
            verbose=True
        )


    @crew
    # @traceable
    def crew(self):
        """Create the crew instance."""
        return Crew(
            agents=[self.review_imaging_findings_part1_agent()],
            tasks=[self.review_imaging_findings_part1_task()],
            verbose=True
        )
