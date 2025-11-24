from openai import OpenAI
import os
from foods import today_calories, list_foods
from goals import list_goals

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
client = OpenAI(api_key=OPENAI_API_KEY) if OPENAI_API_KEY else None

def gpt(prompt):
    if not client:
        return "OpenAI API key not set. Set OPENAI_API_KEY environment variable."
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

def get_active_goals():
    from storage import load_json
    goals = load_json("goals.json")
    if not goals:
        return None
    active_goals = [goal["description"] for goal in goals if not goal.get("completed", False)]
    return active_goals if active_goals else None

def recommend():
    today = today_calories()
    if today.startswith("No foods"):
        return "Log some foods first to get recommendations."
    
    active_goals = get_active_goals()
    goal = 2000
    
    prompt = f"Today's calorie intake:\n{today}\n\nDaily calorie goal: {goal} calories."
    
    if active_goals:
        goals_text = "\n".join([f"- {goal}" for goal in active_goals])
        prompt += f"\n\nActive fitness goals:\n{goals_text}\n\nGive personalized recommendations that align with these fitness goals."
    else:
        prompt += "\n\nGive brief calorie and nutrition recommendations."
    
    return gpt(prompt)

def analyze_foods():
    foods = list_foods()
    if foods.startswith("No foods"):
        return "No foods logged yet."
    
    active_goals = get_active_goals()
    
    prompt = f"Analyze this food log and give nutrition insights:\n{foods}"
    
    if active_goals:
        goals_text = "\n".join([f"- {goal}" for goal in active_goals])
        prompt += f"\n\nActive fitness goals:\n{goals_text}\n\nProvide analysis that relates to these fitness goals."
    
    return gpt(prompt)

def ask_ai(question):
    return gpt(question)

