from crewai import Crew

from agents import (
    senior_research_analyst,
    content_writer,
    reviewer
)

from tasks import (
    research_task,
    writing_task,
    review_task
)

topic = input("Enter topic: ")

crew = Crew(
    agents=[
        senior_research_analyst,
        content_writer,
        reviewer
    ],

    tasks=[
        research_task,
        writing_task,
        review_task
    ],

    verbose=True
)

result = crew.kickoff(
    inputs={"topic": topic}
)
with open("final_report.md", "w") as f:
    f.write(result.raw)