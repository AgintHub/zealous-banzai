from typing import Dict, Any, List, Optional
from crewai import Agent, Task, Crew
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class prepare_specialist_referrals_part2_crew:
    """Crew for prepare_specialist_referrals_part2 operations."""


    @agent
    def prepare_specialist_referrals_part2_agent(self):
        return Agent(
            role="Prepare Specialist Referrals Part2 Specialist",
            goal="Execute prepare_specialist_referrals_part2 task accurately",
            backstory="You are a specialized worker focused on Referral timing optimization",
            verbose=True
        )



    @task
    def prepare_specialist_referrals_part2_task(self):
        """Task for prepare_specialist_referrals_part2."""
        agent = self.prepare_specialist_referrals_part2_agent()
        return Task(
            description="""Using {prioritize_diagnostic_tests_part2_output}, Referral timing optimization""",
            agent=agent,
            expected_output="Provide output that best addresses the task requirements",
            verbose=True
        )


    @crew
    # @traceable
    def crew(self):
        """Create the crew instance."""
        return Crew(
            agents=[self.prepare_specialist_referrals_part2_agent()],
            tasks=[self.prepare_specialist_referrals_part2_task()],
            verbose=True
        )
