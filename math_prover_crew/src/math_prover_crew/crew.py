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

current_llm = local_llm
# current_llm = pro_llm

verbose_agent = True
verbose_task = True
verbose_crew = True

@CrewBase
class MathProverCrew():
    """MathProverCrew crew"""

    agents: list[BaseAgent]
    tasks: list[Task]

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
   
    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['researcher'],
            llm=current_llm,
            verbose=verbose_agent,
        )

    @agent
    def conjecturer(self) -> Agent:
        return Agent(
            config=self.agents_config['conjecturer'],
            llm=current_llm,
            verbose=verbose_agent,
        )

    @agent
    def tester(self) -> Agent:
        return Agent(
            config=self.agents_config['tester'],
            llm=current_llm,
            verbose=verbose_agent,
        )

    @agent
    def critic(self) -> Agent:
        return Agent(
            config=self.agents_config['critic'],
            llm=current_llm,
            verbose=verbose_agent,
        )

    @agent
    def reporting_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['reporting_analyst'],
            llm=current_llm,
            verbose=verbose_agent,
        )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task

    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_task'],
            output_file='report_task1_research.md',
            verbose=verbose_task,
        )

    @task
    def conjecture_task(self) -> Task:
        return Task(
            config=self.tasks_config['conjecture_task'],
            output_file='report_task2_conjecture.md',
            verbose=verbose_task,
        )

    @task
    def testing_task(self) -> Task:
        return Task(
            config=self.tasks_config['testing_task'],
            output_file='report_task3_testing.md',
            verbose=verbose_task,
        )

    @task
    def critic_task(self) -> Task:
        return Task(
            config=self.tasks_config['critic_task'],
            output_file='report_task4_critic.md',
            verbose=verbose_task,
        )

    @task
    def reporting_task(self) -> Task:
        return Task(
            config=self.tasks_config['reporting_task'],
            output_file='report_task5_reporting.md',
            verbose=verbose_task,
        )

    @crew
    def crew(self) -> Crew:
        """Creates the MathProverCrew crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=verbose_crew,
            # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
            # process=Process.hierarchical,
        )