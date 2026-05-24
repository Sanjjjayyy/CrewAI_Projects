# Simple Research Assistant

A project that uses the CrewAI framework to orchestrate a small team of AI agents for research, writing, and review.

## Overview

This repository showcases a multi-agent workflow with three specialized agents:

- **Senior Research Analyst**: performs web research, evaluates sources, and produces a structured research brief.
- **Content Writer**: converts the research brief into an engaging markdown blog post with citations.
- **Content Reviewer**: checks the final blog post for accuracy, clarity, grammar, and citation consistency.

The project uses `crewai` and a search tool integration to fetch information from the web and generate publishable content.

## Project Structure

- `main.py`: application entry point. Prompts for a topic, runs the CrewAI workflow, and writes output to `final_report.md`.
- `agents.py`: defines the three AI agents, their roles, goals, backstories, and LLM configuration.
- `tasks.py`: defines the three sequential tasks for research, writing, and review.
- `final_report.md`: generated output file containing the final markdown blog post.
- `.env`: stores API keys for the language model and search tool.

## Tech Stack

- CrewAI
- Valid API keys for:
  - `GROQ API KEY` (used by the configured LLM)
  - `SERPER_API_KEY` (used by the search tool)

## Setup

1. Create a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Install required packages.

```bash
pip install crewai crewai-tools
```

3. Create a `.env` file with your API keys:

```text
GROQ_API_KEY=your_groq_api_key
SERPER_API_KEY=your_serper_api_key
```

## Usage

Run the demo:

```bash
python main.py
```

Enter a topic when prompted. The script will:

1. run research on the topic
2. generate a post draft
3. review and polish the output
4. save the result to `final_report.md`

## Example

```bash
Enter topic: quantum computing
```

```bash
# Quantum Computing: The Future of Technology
Quantum computing is a rapidly evolving field that has the potential to revolutionize various industries and aspects of our lives [1]. With recent developments, news, and trends in quantum computing showing significant progress, it is essential to evaluate the credibility of sources and fact-check information to ensure accuracy and reliability [2]. In this blog post, we will explore the current trends and developments in quantum computing, verified facts and statistics, and the importance of evaluating the credibility of sources and fact-checking information.

### Current Trends and Developments
Some of the current trends and developments in quantum computing include improving the reliability of circuits for quantum computers, developing new algorithms and hardware designs to accelerate progress, and exploring the potential of quantum computing in various fields, such as medicine, finance, and climate modeling [3]. Additionally, many organizations, including Google, IBM, and Microsoft, are investing in quantum computing research and development [4].

### Verified Facts and Statistics
Some verified facts and statistics about quantum computing include the potential of quantum computers to solve complex problems that are currently unsolvable with traditional computers [5]. The number of qubits (quantum bits) in a quantum computer determines its processing power, and quantum computing has the potential to revolutionize fields such as medicine, finance, and climate modeling [1]. Many organizations are also investing in quantum computing research and development, with IBM being a leading player in the field [4].

### Evaluating the Credibility of Sources
Evaluating the credibility of sources is crucial when researching quantum computing [2]. Some credible sources include peer-reviewed academic journals and articles, official websites and publications of reputable organizations, such as IBM and Google, and news articles from established and reputable news outlets [3]. It is essential to verify information through multiple sources, evaluate the credibility of sources, and be cautious of biased or misleading information [5].

### Fact-Checking and Main Themes
Fact-checking is essential when researching quantum computing to ensure accuracy and reliability [1]. Some main themes and patterns in quantum computing research include the potential of quantum computing to revolutionize various industries and aspects of our lives, the importance of evaluating the credibility of sources and fact-checking information, and the need for continued investment in quantum computing research and development [2].

### Conclusion
Quantum computing is a rapidly evolving field with significant potential to revolutionize various industries and aspects of our lives [3]. By understanding the current trends and developments, verified facts and statistics, and main themes and patterns in quantum computing research, we can better appreciate the potential of this technology and its potential impact on our world [4]. It is essential to continue evaluating the credibility of sources and fact-checking information to ensure accuracy and reliability in the field of quantum computing.

### References
[1] The Quantum Insider: Quantum Computing News & Top Stories. https://thequantuminsider.com/
[2] Quantum Computing Report. https://quantumcomputingreport.com/
[3] MIT Sloan: Quantum computing: What leaders need to know now. https://mitsloan.mit.edu/ideas-made-to-matter/quantum-computing-what-leaders-need-to-know-now
[4] IBM: What Is Quantum Computing? https://www.ibm.com/think/topics/quantum-computing
[5] IEEE Spectrum: The Case Against Quantum Computing. https://spectrum.ieee.org/the-case-against-quantum-computing

Note: I made the following changes to improve the content:
- Reorganized the references to use a numbered format for easier citation.
- Added citations to the text to support the claims made and to provide credibility to the information presented.
- Made minor changes to the wording and sentence structure to improve clarity and readability.
- Removed redundant information and condensed the text to make it more concise.
- Emphasized the importance of evaluating the credibility of sources and fact-checking information in the field of quantum computing.
```