from foods import log_food, list_foods, today_calories, history
from agents import recommend, analyze_foods, ask_ai
from goals import add_goal, list_goals, complete_goal, search_goals
import re

def show_help():
    return """
Commands:
  help                         Show commands
  exit                         Quit

Food Logging:
  log food <name> <grams>      Log a food (e.g., log food apple 100)
  list foods                   Show all logged foods
  today                        Show today's calories
  history                      Show calorie history

Fitness Goals:
  add goal <description>       Add a fitness goal
  list goals                   Show all goals
  complete <id>                Mark goal as complete
  search goals <query>         Search goals

AI (OpenAI):
  recommend                    Get calorie recommendations
  analyze foods                AI nutrition analysis
  ask ai <question>            Ask AI anything
"""

def chat():
    print("""
╔═══════════════════════════════════════════════════════════╗
║                                                           ║
║         ███████╗ ██████╗  ██████╗ ██████╗                ║
║         ██╔════╝██╔═══██╗██╔═══██╗██╔══██╗               ║
║         █████╗  ██║   ██║██║   ██║██║  ██║               ║
║         ██╔══╝  ██║   ██║██║   ██║██║  ██║               ║
║         ██║     ╚██████╔╝╚██████╔╝██████╔╝               ║
║         ╚═╝      ╚═════╝  ╚═════╝ ╚═════╝                ║
║                                                           ║
║         ████████╗██████╗  █████╗  ██████╗██╗  ██╗         ║
║         ╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝         ║
║            ██║   ██████╔╝███████║██║     █████╔╝          ║
║            ██║   ██╔══██╗██╔══██║██║     ██╔═██╗          ║
║            ██║   ██║  ██║██║  ██║╚██████╗██║  ██╗         ║
║            ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝         ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝

                    Made by Demetri Frangiadakis
                  
              AI Powered Nutrition Insights
              
═══════════════════════════════════════════════════════════
""")
    print(show_help())
    print()

    while True:
        msg = input("You: ").strip()

        # Use regex for flexible, case-insensitive command matching
        msg_lower = msg.lower()
        
        # Exit command - flexible matching
        if re.match(r'^(exit|quit|q)$', msg_lower):
            print("Goodbye!")
            break

        # Help command
        elif re.match(r'^(help|h|\?)$', msg_lower):
            print(show_help())

        # Log food command - regex to extract food name and quantity
        elif re.match(r'^log\s+food\s+(.+?)\s+(\d+(?:\.\d+)?)$', msg_lower):
            match = re.match(r'^log\s+food\s+(.+?)\s+(\d+(?:\.\d+)?)$', msg_lower)
            name = match.group(1).strip()
            quantity = float(match.group(2))
            print(log_food(name, quantity))

        # List foods command - flexible matching
        elif re.match(r'^(list\s+foods?|foods?|ls)$', msg_lower):
            print(list_foods())

        # Today command - flexible matching
        elif re.match(r'^(today|todays?|calories?)$', msg_lower):
            print(today_calories())

        # History command - flexible matching
        elif re.match(r'^(history|hist|past)$', msg_lower):
            print(history())

        # Recommend command - flexible matching
        elif re.match(r'^(recommend|rec|suggestion)$', msg_lower):
            print(recommend())

        # Analyze foods command - flexible matching
        elif re.match(r'^(analyze\s+foods?|analysis|analyze)$', msg_lower):
            print(analyze_foods())

        # Ask AI command - regex to extract question
        elif re.match(r'^ask\s+ai\s+(.+)$', msg_lower):
            match = re.match(r'^ask\s+ai\s+(.+)$', msg_lower)
            question = match.group(1).strip()
            print(ask_ai(question))

        # Add goal command - regex to extract description
        elif re.match(r'^add\s+goal\s+(.+)$', msg_lower):
            match = re.match(r'^add\s+goal\s+(.+)$', msg_lower)
            description = match.group(1).strip()
            print(add_goal(description))

        # List goals command - flexible matching
        elif re.match(r'^(list\s+goals?|goals?)$', msg_lower):
            print(list_goals())

        # Complete goal command - regex to extract goal ID
        elif re.match(r'^complete\s+(\d+)$', msg_lower):
            match = re.match(r'^complete\s+(\d+)$', msg_lower)
            goal_id = int(match.group(1))
            print(complete_goal(goal_id))

        # Search goals command - regex to extract query
        elif re.match(r'^search\s+goals?\s+(.+)$', msg_lower):
            match = re.match(r'^search\s+goals?\s+(.+)$', msg_lower)
            query = match.group(1).strip()
            print(search_goals(query))

        else:
            print("Unknown command. Type 'help'.")
            
if __name__ == "__main__":
    chat()

