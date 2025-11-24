from storage import load_json, save_json

GOALS_FILE = "goals.json"

def add_goal(description, goal_type="general"):
    goals = load_json(GOALS_FILE)
    goal = {
        "id": len(goals) + 1,
        "description": description,
        "completed": False,
        "type": goal_type
    }
    goals.append(goal)
    save_json(GOALS_FILE, goals)
    return f"Goal added: {description}"

def complete_goal(goal_id):
    goals = load_json(GOALS_FILE)
    for goal in goals:
        if goal["id"] == goal_id:
            goal["completed"] = True
            save_json(GOALS_FILE, goals)
            return f"Goal {goal_id} marked as complete"
    return f"Goal {goal_id} not found"

def list_goals():
    goals = load_json(GOALS_FILE)
    if not goals:
        return "No goals found."
    
    output = ""
    for goal in goals:
        status = "✓" if goal["completed"] else " "
        goal_type = goal.get("type", "general").upper()
        output += f"{goal['id']}. [{status}] [{goal_type}] {goal['description']}\n"
    return output

def search_goals(query):
    goals = load_json(GOALS_FILE)
    results = [goal for goal in goals if query.lower() in goal["description"].lower()]
    if not results:
        return f"No goals found matching '{query}'"
    
    output = ""
    for goal in results:
        status = "✓" if goal["completed"] else " "
        goal_type = goal.get("type", "general").upper()
        output += f"{goal['id']}. [{status}] [{goal_type}] {goal['description']}\n"
    return output

