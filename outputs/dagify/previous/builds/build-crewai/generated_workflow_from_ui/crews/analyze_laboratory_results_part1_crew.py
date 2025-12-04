from typing import Dict, Any, List, Optional
from crewai import Agent, Task, Crew
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class analyze_laboratory_results_part1_crew:
    """Crew for analyze_laboratory_results_part1 operations."""


    @agent
    def analyze_laboratory_results_part1_agent(self):
        return Agent(
            role="Analyze Laboratory Results Part1 Specialist",
            goal="Execute analyze_laboratory_results_part1 task accurately",
            backstory="You are a specialized worker focused on Create baseline lab analysis framework",
            verbose=True
        )



    @task
    def analyze_laboratory_results_part1_task(self):
        """Task for analyze_laboratory_results_part1."""
        agent = self.analyze_laboratory_results_part1_agent()
        return Task(
            description="""Using {input}, Create baseline lab analysis framework""",
            agent=agent,
            expected_output="Provide output that best addresses the task requirements",
            verbose=True
        )


    @crew
    # @traceable
    def crew(self):
        """Create the crew instance."""
        return Crew(
            agents=[self.analyze_laboratory_results_part1_agent()],
            tasks=[self.analyze_laboratory_results_part1_task()],
            verbose=True
        )
