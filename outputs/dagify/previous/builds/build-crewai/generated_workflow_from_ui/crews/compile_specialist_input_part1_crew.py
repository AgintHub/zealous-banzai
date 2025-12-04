from typing import Dict, Any, List, Optional
from crewai import Agent, Task, Crew
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class compile_specialist_input_part1_crew:
    """Crew for compile_specialist_input_part1 operations."""


    @agent
    def compile_specialist_input_part1_agent(self):
        return Agent(
            role="Compile Specialist Input Part1 Specialist",
            goal="Execute compile_specialist_input_part1 task accurately",
            backstory="You are a specialized worker focused on Structural input synthesis",
            verbose=True
        )



    @task
    def compile_specialist_input_part1_task(self):
        """Task for compile_specialist_input_part1."""
        agent = self.compile_specialist_input_part1_agent()
        return Task(
            description="""Using {prepare_specialist_referrals_part2_output}, Structural input synthesis""",
            agent=agent,
            expected_output="Provide output that best addresses the task requirements",
            verbose=True
        )


    @crew
    # @traceable
    def crew(self):
        """Create the crew instance."""
        return Crew(
            agents=[self.compile_specialist_input_part1_agent()],
            tasks=[self.compile_specialist_input_part1_task()],
            verbose=True
        )
