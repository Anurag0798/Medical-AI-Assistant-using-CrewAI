# Medical AI Assistant using CrewAI

This project is a simple, practical example of a **medical-style AI assistant** built with **CrewAI** and **Euri LLM**. It shows how to combine:

- Multiple agents with different roles
- Custom tools (Python functions)
- A crew that coordinates tasks between agents

The assistant takes a user’s basic profile and symptoms, then:

1. Suggests possible medical conditions (non-diagnostic).
2. Provides generic lifestyle and wellness advice.

## Project Overview

The core ideas demonstrated in this project:

- How to define **tools** that agents can call.
- How to wrap an LLM (Euri) in agents using a small utility class (`MedicalAgent`).
- How to define **tasks** for each agent.
- How to group everything into a **Crew** and run it via `crew.kickoff()`.

## Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/Anurag0798/Medical-AI-Assistant-using-CrewAI.git

   cd Medical-AI-Assistant-using-CrewAI
   ```

2. Create and activate a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv

   # Linux / macOS
   source .venv/bin/activate

   # Windows
   .venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the script:

   ```bash
   python <filename>.py
   ```

## Limitations and Disclaimer

- This example uses **very simple logic** in tools and relies on an LLM for reasoning.
- It is not validated for medical safety or accuracy.
- It must not be used in real clinical workflows.

## Contributing

If you want to extend this project:

- Add more realistic tools (e.g., lookups, guidelines).
- Improve prompts and roles for agents.
- Add a UI (Streamlit, Gradio) to input patient data.
- Add logging and evaluation for agent outputs.

Contributions are welcome via pull requests to the original repository.

## License

Refer to the `LICENSE` file in the repository for licensing details.