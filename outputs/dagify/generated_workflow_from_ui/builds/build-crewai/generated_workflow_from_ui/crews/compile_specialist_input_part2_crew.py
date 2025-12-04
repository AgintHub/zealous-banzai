from typing import Dict, Any, List, Optional
from crewai import Agent, Task, Crew
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class compile_specialist_input_part2_crew:
    """Crew for compile_specialist_input_part2 operations."""


    @agent
    def compile_specialist_input_part2_agent(self):
        return Agent(
            role="Compile Specialist Input Part2 Specialist",
            goal="Execute compile_specialist_input_part2 task accurately",
            backstory="You are a specialized worker focused on Input validation reconciliation",
            verbose=True
        )



    @task
    def compile_specialist_input_part2_task(self):
        """Task for compile_specialist_input_part2."""
        agent = self.compile_specialist_input_part2_agent()
        return Task(
            description="""Using {prepare_specialist_referrals_part2_output}, Input validation reconciliation""",
            agent=agent,
            expected_output="Provide output that best addresses the task requirements",
            verbose=True
        )


    @crew
    # @traceable
    def crew(self):
        """Create the crew instance."""
        return Crew(
            agents=[self.compile_specialist_input_part2_agent()],
            tasks=[self.compile_specialist_input_part2_task()],
            verbose=True
        )
