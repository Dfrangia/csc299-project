# Diet Tracker

Simple Python CLI to log foods, track daily calories, view history, and get AI recommendations.

## Setup

**Recommended:** Get free Edamam API keys (more accurate calorie data):
1. Go to https://developer.edamam.com/
2. Sign up and create an application
3. Set environment variables:
```bash
$env:EDAMAM_APP_ID='your-app-id'
$env:EDAMAM_APP_KEY='your-app-key'
```

**Also set OpenAI API key** (for AI recommendations):
```bash
$env:OPENAI_API_KEY='your-key'
```

Get OpenAI key at https://platform.openai.com/api-keys

**Note:** If Edamam keys aren't set, it will use OpenAI to estimate calories (less accurate).

## Usage

```bash
python main.py
```

Commands:
- `log food apple 100` - Log 100g of apple
- `today` - Show today's calories
- `history` - Show calorie history
- `recommend` - Get AI recommendations
- `analyze foods` - AI nutrition analysis
- `ask ai <question>` - Ask AI anything

## Files

- `main.py` - Chat interface
- `foods.py` - Food logging functions
- `storage.py` - JSON file storage
- `api_client.py` - Edamam API calls
- `agents.py` - AI functions (OpenAI)
- `api_key.py` - API key configuration
