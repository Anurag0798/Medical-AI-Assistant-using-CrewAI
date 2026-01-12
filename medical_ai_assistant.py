from crewai import Agent, Task, Crew 
from crewai_tools.tools import tool
from euri_llm_crewai import EuriLLM

# Tools
@tool("Symptoms checker tool")
def symptom_checker_tool(symptoms_text):
    """This tool analyzes the patient symptoms and provide a diagnosis in details"""
    
    if "thirst" in symptoms_text and "fatigue" in symptoms_text:
        return "Possible condition: Type 2 Diabetes. Consider blood suger evaluation"
    elif "headache" in symptoms_text:
        return "Possible condition: Migrain or Hypertension. Need clinical confirmation" 
    else:
        return "General fatigue. Could be related to stress or poor sleep"

@tool("Health advice tool")
def health_advice_tool():
    """Provides basic wellness suggestion based on symptoms and history"""
    
    return "Maintain a low-sugar diet, hydrate well, and schedule a doctor visit for further advice"

# Generic class for Agents
class MedicalAgent:
    def __init__(self, role, goal, backstory, tools=[]):
        self.agent = Agent(
            role = role,
            goal = goal,
            backstory = backstory,
            verbose = True , 
            allow_deligation = False ,
            llm = EuriLLM(),
            tools = tools
        )

    def get_agent(self):
        return self.agent

# Agents
diagnosis_agent = MedicalAgent(
        role="AI Medical Diagnostician",
        goal="Analyze symptoms and provide possible cure",
        backstory= "Expert in identifying potential health condition based on the symptoms cluster and identification",
        tools=[symptom_checker_tool]
    ).get_agent()

advice_agent = MedicalAgent(
        role="AI Healthcare Adviser",
        goal="Offer a safe and respoinsible lifestyle suggestion based on the user profile",
        backstory="A virtual assistant trained to give personalized wellness and precautionary advice",
        tools=[health_advice_tool]
    ).get_agent()

user_input = {
    "name": "Anurag Singh",
    "age": 27,
    "gender": "Male",
    "symptoms": ["frequent headache", "blurred vision", "fatigue", "increased thirst"],
    "medical history": "Family history of diabetese and hypertension"
}

symptoms_text = f"""    
        name: {user_input['name']}  
        age: {user_input['age']}    
        gender: {user_input['gender']}  
        symptoms: {user_input['symptoms']}   
        medical history: {user_input['medical history']}
    """

# Tasks for each Agent
tasks = [
    Task(
        description=f"Analyze the following user's symptoms using tools and provide a possible cause:\n{symptoms_text}",
        expected_output="Top 3 possible conditions with a brief explanation for each listed condition",
        agent=diagnosis_agent
    ),
    Task(
        description=f"Based on the user's profile and symptoms, provide lifestyle and medical advice:\n{symptoms_text}",
        expected_output="Actionable advice, dietary tips, and when to seek or visit a doctor",
        agent=advice_agent
    ),
]

# Crew = Group of Agents
crew = Crew(
        agents = [diagnosis_agent, advice_agent],
        tasks = tasks,
        verbose = True
    )

result  = crew.kickoff()

print("Personalized medical report", result)