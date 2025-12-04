from typing import Dict, Any, List, Optional
from crewai import Agent, Task, Crew
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class prepare_specialist_referrals_part1_crew:
    """Crew for prepare_specialist_referrals_part1 operations."""


    @agent
    def prepare_specialist_referrals_part1_agent(self):
        return Agent(
            role="Prepare Specialist Referrals Part1 Specialist",
            goal="Execute prepare_specialist_referrals_part1 task accurately",
            backstory="You are a specialized worker focused on Core referral framework",
            verbose=True
        )



    @task
    def prepare_specialist_referrals_part1_task(self):
        """Task for prepare_specialist_referrals_part1."""
        agent = self.prepare_specialist_referrals_part1_agent()
        return Task(
            description="""Using {prioritize_diagnostic_tests_part2_output}, Core referral framework""",
            agent=agent,
            expected_output="Provide output that best addresses the task requirements",
            verbose=True
        )


    @crew
    # @traceable
    def crew(self):
        """Create the crew instance."""
        return Crew(
            agents=[self.prepare_specialist_referrals_part1_agent()],
            tasks=[self.prepare_specialist_referrals_part1_task()],
            verbose=True
        )
