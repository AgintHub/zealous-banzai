from typing import Dict, Any, List, Optional
from crewai import Agent, Task, Crew
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class analyze_laboratory_results_part2_crew:
    """Crew for analyze_laboratory_results_part2 operations."""


    @agent
    def analyze_laboratory_results_part2_agent(self):
        return Agent(
            role="Analyze Laboratory Results Part2 Specialist",
            goal="Execute analyze_laboratory_results_part2 task accurately",
            backstory="You are a specialized worker focused on Generate hypothesis correlation from lab data",
            verbose=True
        )



    @task
    def analyze_laboratory_results_part2_task(self):
        """Task for analyze_laboratory_results_part2."""
        agent = self.analyze_laboratory_results_part2_agent()
        return Task(
            description="""Using {input}, Generate hypothesis correlation from lab data""",
            agent=agent,
            expected_output="Provide output that best addresses the task requirements",
            verbose=True
        )


    @crew
    # @traceable
    def crew(self):
        """Create the crew instance."""
        return Crew(
            agents=[self.analyze_laboratory_results_part2_agent()],
            tasks=[self.analyze_laboratory_results_part2_task()],
            verbose=True
        )
