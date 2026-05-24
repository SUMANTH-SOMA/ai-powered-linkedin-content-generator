import os

from crewai import LLM
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import (
	SerperDevTool
)






@CrewBase
class AiPoweredLinkedinContentGeneratorCrew:
    """AiPoweredLinkedinContentGenerator crew"""

    
    @agent
    def linkedin_trend_research_analyst(self) -> Agent:
        
        
        return Agent(
            config=self.agents_config["linkedin_trend_research_analyst"],
            
            
            tools=[				SerperDevTool()],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            
            max_execution_time=None,
            llm=LLM(
                model="openai/gpt-4o-mini",
                
                
            ),
            
        )
        
    
    @agent
    def linkedin_content_strategist(self) -> Agent:
        
        
        return Agent(
            config=self.agents_config["linkedin_content_strategist"],
            
            
            tools=[],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            
            max_execution_time=None,
            llm=LLM(
                model="openai/gpt-4o-mini",
                
                
            ),
            
        )
        
    

    
    @task
    def research_industry_trends(self) -> Task:
        return Task(
            config=self.tasks_config["research_industry_trends"],
            markdown=False,
            
            
        )
    
    @task
    def generate_professional_linkedin_content(self) -> Task:
        return Task(
            config=self.tasks_config["generate_professional_linkedin_content"],
            markdown=False,
            
            
        )
    

    @crew
    def crew(self) -> Crew:
        """Creates the AiPoweredLinkedinContentGenerator crew"""

        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,

            chat_llm=LLM(model="openai/gpt-4o-mini"),
        )


