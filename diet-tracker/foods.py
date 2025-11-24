from storage import load_json, save_json
from datetime import date
from api_client import fetch_calories

FOODS_FILE = "foods.json"

def list_foods():
    foods = load_json(FOODS_FILE)
    if not foods:
        return "No foods logged."
    output = ""
    for idx, f in enumerate(foods, 1):
        output += f"{idx}. {f['name']} ({f['quantity']}g) - {f['calories']:.0f} cal - {f['date']}\n"
    return output

def log_food(name, quantity):
    calories, error = fetch_calories(name, quantity)
    if error:
        return error
    
    foods = load_json(FOODS_FILE)
    foods.append({
        "name": name,
        "quantity": quantity,
        "calories": calories,
        "date": date.today().isoformat()
    })
    save_json(FOODS_FILE, foods)
    return f"Logged {name} ({quantity}g) - {calories:.0f} calories"

def today_calories():
    foods = load_json(FOODS_FILE)
    today = date.today().isoformat()
    today_foods = [f for f in foods if f['date'] == today]
    
    if not today_foods:
        return "No foods logged today."
    
    total = sum(f['calories'] for f in today_foods)
    output = f"Today's calories: {total:.0f}\n\n"
    for f in today_foods:
        output += f"  - {f['name']} ({f['quantity']}g): {f['calories']:.0f} cal\n"
    return output

def history():
    foods = load_json(FOODS_FILE)
    if not foods:
        return "No food logs found."
    
    from collections import defaultdict
    daily = defaultdict(float)
    for f in foods:
        daily[f['date']] += f['calories']
    
    output = "Calorie History:\n\n"
    for date_str in sorted(daily.keys()):
        output += f"{date_str}: {daily[date_str]:.0f} calories\n"
    return output

