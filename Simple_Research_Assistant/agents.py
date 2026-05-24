from crewai import Agent,Task,LLM
from crewai_tools import SerperDevTool

import os
from dotenv import load_dotenv
load_dotenv()

# 1. APPLY THE BUGFIX PATCH IMMEDIATELY HERE
import crewai.llms.cache as _crewai_cache
_crewai_cache.mark_cache_breakpoint = lambda msg: msg


api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY is missing! Check your .env file.")

# 3. Setup LLM
llm = LLM(
    model="groq/llama-3.3-70b-versatile",
    temperature=0.2,
    api_key=api_key
)
# Tool
search_tool = SerperDevTool(n=1)


# Agent 1
senior_research_analyst = Agent(
    role = "Senior Research Analyst",
    goal= f"Research, analyze, and synthesize comprehensive information on the given from reliable web sources",
    backstory="You're an expert research analyst with advanced web research skills. "
                    "You excel at finding, analyzing, and synthesizing information from "
                    "across the internet using search tools. You're skilled at "
                    "distinguishing reliable sources from unreliable ones, "
                    "fact-checking, cross-referencing information, and "
                    "identifying key patterns and insights. You provide "
                    "well-organized research briefs with proper citations "
                    "and source verification. Your analysis includes both "
                    "raw data and interpreted insights, making complex "
                    "information accessible and actionable.",

    verbose = True,
    tools=[search_tool],
    llm=llm,
    max_iter=1
)

#Agent 2
content_writer = Agent(
    role="Content Writer",
    goal="Transform research findings into engaging blog posts while maintaining accuracy",
    backstory="You're a skilled content writer specialized in creating "
                    "engaging, accessible content from technical research. "
                    "You work closely with the Senior Research Analyst and excel at maintaining the perfect "
                    "balance between informative and entertaining writing, "
                    "while ensuring all facts and citations from the research "
                    "are properly incorporated. You have a talent for making "
                    "complex topics approachable without oversimplifying them.",
    verbose=True,
    allow_delegation=False,
    llm = llm,
    max_iter=1
)


# Agent 3

reviewer = Agent(
    role="Content Reviewer",

    goal="Review content for accuracy, clarity, grammar, and factual consistency",

    backstory="""
    Experienced editor skilled at proofreading, fact-checking,
    and improving content quality. Ensures the final content is
    clear, accurate, well-structured, and free from misleading claims.
    """,

    verbose=True,
    llm=llm,
    max_iter=1
)

