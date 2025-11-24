import requests
import os
from openai import OpenAI
import re

# Try Edamam first (more accurate), fallback to OpenAI
EDAMAM_APP_ID = os.getenv("EDAMAM_APP_ID", "")
EDAMAM_APP_KEY = os.getenv("EDAMAM_APP_KEY", "")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

def fetch_calories(food_name, quantity):
    # Try Edamam first (nutrition database - more accurate)
    if EDAMAM_APP_ID and EDAMAM_APP_KEY:
        try:
            url = "https://api.edamam.com/api/nutrition-data"
            params = {
                "app_id": EDAMAM_APP_ID,
                "app_key": EDAMAM_APP_KEY,
                "ingr": f"{quantity}g {food_name}"
            }
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            if "calories" in data:
                return data.get("calories", 0), None
        except Exception:
            pass  # Fall through to OpenAI
    
    # Fallback to OpenAI if Edamam not available
    if OPENAI_API_KEY:
        try:
            client = OpenAI(api_key=OPENAI_API_KEY)
            prompt = f"Estimate calories for {quantity}g of {food_name}. Respond with ONLY a number (no text, no explanation)."
            
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=10
            )
            result = response.choices[0].message.content.strip()
            numbers = re.findall(r'\d+', result)
            if numbers:
                calories = float(numbers[0])
                calories = (calories / 100) * quantity
                return calories, None
        except Exception as e:
            return None, f"OpenAI error: {str(e)}"
    
    return None, "No API keys set. Set EDAMAM_APP_ID/EDAMAM_APP_KEY (recommended) or OPENAI_API_KEY."

