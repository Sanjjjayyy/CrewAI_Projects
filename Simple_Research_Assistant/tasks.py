from crewai import Task

from agents import (
    senior_research_analyst,
    content_writer,
    reviewer
)

research_task= Task(
    description=("""
            Research Topic: {topic}
            
            1. Conduct comprehensive research on {topic} including:
                - Recent developments, news, and key trends in {topic}
                - Relevant statistics, data, and expert opinions
                - Current state of the field and future implications
            2. Evaluate source credibility and fact-check all information
            3. Organize findings into a structured research brief
            4. Include all relevant citations and sources with URLs
        """),
    expected_output = """A detailed research report on {topic} containing:
            - Executive summary of key findings
            - Comprehensive analysis of current trends and developments
            - List of verified facts and statistics
            - All citations and links to original sources
            - Clear categorization of main themes and patterns
            Please format with clear sections and bullet points for easy reference.""",
    agent = senior_research_analyst)



# Content Writer Task
# Task 2 Content Writing
writing_task = Task(
        description=("""
            Topic: {topic}
            
            Using the research brief provided above, create an engaging blog post on {topic} that:
            1. Transforms technical information into accessible content
            2. Maintains all factual accuracy and citations from the research
            3. Includes:
                - Attention-grabbing introduction about {topic}
                - Well-structured body sections with clear headings
                - Compelling conclusion summarizing key insights about {topic}
            4. Preserves all source citations in [Source: URL] format
            5. Includes a References section at the end
        """),
        expected_output = """A polished blog post on {topic} in markdown format that:
            - Engages readers while maintaining accuracy about {topic}
            - Contains properly structured sections
            - Includes inline citations hyperlinked to the original source URLs
            - Presents information in an accessible yet informative way
            - Follows proper markdown formatting, use H1 for the title and H3 for the sub-sections
            - Title should be about {topic}""",
        agent = content_writer)


#Reviewing Task
# Task 3
review_task = Task(
    description="""
    Topic: {topic}
    
    Review the generated blog post about {topic} for:

    - Factual accuracy about {topic}
    - Grammar and spelling
    - Clarity and readability
    - Logical flow and structure
    - Consistency with the original research on {topic}
    - Proper citation formatting
    - Relevance and completeness of information about {topic}

    Identify any misleading claims, unsupported statements,
    or missing references related to {topic}.

    Improve the content where necessary while preserving
    the original meaning and writing quality.
    """,

    expected_output="""
    A final polished markdown blog post about {topic} that:
    - is factually accurate regarding {topic}
    - is grammatically correct
    - has clear structure and readability
    - includes properly formatted citations
    - maintains consistency with the research report on {topic}
    - comprehensively covers {topic}
    - is ready for publication
    """,

    context=[research_task, writing_task],

    agent=reviewer
)