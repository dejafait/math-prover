from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from dotenv import load_dotenv
import os

load_dotenv()

pro_llm = LLM(
    model="openai/gpt-5.4-pro",
    api_key=os.getenv("OPENAI_API_KEY"),
    api="responses",  # Required for Pro / deep thinking models
    reasoning_effort="medium",  # low medium high xhigh
    store=True,
    auto_chain=True,
)

local_llm = LLM(
    model="ollama/gemma4:e4b",
    base_url="http://localhost:11434/v1",
    api_key="ollama",
)

current_llm = pro_llm

# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators
@CrewBase
class MathProverCrew():
    """MathProverCrew crew"""

    agents: list[BaseAgent]
    tasks: list[Task]

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
   
    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools

    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['researcher'], # type: ignore[index]
            llm=current_llm,
            verbose=True
        )

    @agent
    def conjecturer(self) -> Agent:
        return Agent(
            config=self.agents_config['conjecturer'], # type: ignore[index]
            llm=current_llm,
            verbose=True
        )

    @agent
    def tester(self) -> Agent:
        return Agent(
            config=self.agents_config['tester'], # type: ignore[index]
            llm=current_llm,                        # GPT-5.5 Pro + xhigh deep thinking
            verbose=True
        )

    @agent
    def critic(self) -> Agent:
        return Agent(
            config=self.agents_config['critic'], # type: ignore[index]
            llm=current_llm,                        # GPT-5.5 Pro + xhigh deep thinking
            verbose=True
        )

    @agent
    def reporting_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['reporting_analyst'], # type: ignore[index]
            llm=current_llm,
            verbose=True
        )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task

    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_task'], # type: ignore[index]
            output_file='report_task1_research.md',
        )

    @task
    def conjecture_task(self) -> Task:
        return Task(
            config=self.tasks_config['conjecture_task'], # type: ignore[index]
            output_file='report_task2_conjecture.md',
        )

    @task
    def testing_task(self) -> Task:
        return Task(
            config=self.tasks_config['testing_task'], # type: ignore[index]
            output_file='report_task3_testing.md',
        )

    @task
    def critic_task(self) -> Task:
        return Task(
            config=self.tasks_config['critic_task'], # type: ignore[index]
            output_file='report_task4_critic.md',
        )

    @task
    def reporting_task(self) -> Task:
        return Task(
            config=self.tasks_config['reporting_task'], # type: ignore[index]
            output_file='report_task5_reporting.md',
        )

    @crew
    def crew(self) -> Crew:
        """Creates the MathProverCrew crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )