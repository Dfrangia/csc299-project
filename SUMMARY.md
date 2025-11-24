CSC 299 Final Project Summary

For my final project I built a diet tracker. It's basically a terminal app where you can log foods, see how many calories you've had today, look at your history, and get AI recommendations. I integrated two APIs - Edamam for getting actual calorie data from a real nutrition database, and OpenAI for the AI features like recommendations and analysis. Everything saves to JSON files so it works on any computer.

When I first read the assignment I knew I didn't want to just build another task manager. I'm into nutrition and tracking what I eat, so a diet tracker made sense. But I had no clue how to actually get calorie data for foods. That's when I started looking into nutrition APIs.

The biggest thing for me was data integrity. I knew an LLM could probably guess at calories, but I wanted the real deal - an actual nutrition database. I didn't want users getting bad information just because an AI made something up. So I researched different APIs, looked at their accuracy, checked out free tier limits, compared data quality. That's how I found Edamam. It has a real nutrition database with verified calorie data, not just estimates.

I also care a lot about user experience and error handling. Users make mistakes. They type things wrong, forget commands, use different capitalization. I wanted the app to handle all that without crashing or giving confusing errors.

I used ChatGPT a ton to figure out how nutrition APIs work, what data structures make sense, how to design a chat interface that feels natural, how to integrate multiple APIs, and how to store date-based data in JSON.

After going back and forth with ChatGPT, I ended up with a simple structure - separate files for food logging, storage, API calls, and AI agents. I decided early on to use both Edamam for accurate data and OpenAI for AI stuff to show I could work with multiple APIs.

The earlier tasks helped me understand what the class wanted. Task 1 was about JSON workflows which I'm already familiar with, but it helped me think about structuring data for a chat app. Task 2 showed me how to build a chat interface - the loop pattern I learned there is exactly what I used. Task 3 was pytest - I didn't write formal tests for the final project but the mindset of testing as I go helped catch bugs early. Task 4 was huge because I learned how to call the OpenAI API, handle keys, write prompts, deal with errors. That directly shaped my AI agents. Task 5 was about spec-kit and planning first, which stuck with me even though I didn't use spec-kit for the final project.

I used ChatGPT GPT-4 as my main coding assistant the whole time. For planning I'd describe what I wanted and it would help break it down into modules and functions. Like when I wanted historical calorie tracking, I asked how to structure date-based data in JSON and got suggestions for ISO date strings and grouping by date.

For writing code I'd describe what a function should do and ChatGPT would write the first version. Then I'd test it, find bugs, ask it to fix them. This back and forth worked really well.

I wanted dynamic user input because things don't often match expected input. Users type commands differently, make typos, use different capitalization. I already knew regex so I used it for command parsing to handle all these variations. I used patterns like r'^log\s+food\s+(.+?)\s+(\d+(?:\.\d+)?)$' to extract food names and quantities. The regex makes it flexible - users can type exit, quit, or q and it all works.

For API integration ChatGPT helped me understand the Edamam API, what the response looks like, how to handle errors. It also helped me design a fallback where if Edamam isn't available, the app uses OpenAI to estimate calories, though it's less accurate.

When things broke I'd paste the error and code to ChatGPT and it would help me figure it out. Saved me a lot of time.

I also used GitHub Copilot for autocomplete, especially with repetitive stuff like command parsing. But I always checked what it suggested because sometimes it was wrong.

The most important decision was choosing Edamam over just using an LLM for calorie data. I knew an LLM might have some food data, but I wanted to research the best source. Data integrity matters to me - users are trusting my app with their nutrition tracking. Bad data could mislead them. Edamam has a real nutrition database with verified information, not AI guesses. Worth the extra complexity of integrating another API.

I built a fallback system too - if Edamam keys aren't set, it uses OpenAI to estimate. But I made it clear Edamam is preferred for accuracy. The fallback is for flexibility, but I always tell users to get Edamam keys for the best experience.

I wanted dynamic user input since things don't match expected input. Users type commands differently, make typos, forget exact syntax. I already knew regex so I used it for command parsing instead of simple string matching. This let me make commands case-insensitive, handle variations like exit or quit or q, and extract arguments more reliably. It was more complex than startswith() but I wanted users to have a smooth experience even if they don't type commands exactly right.

I chose Edamam because it has a free tier with 10,000 requests per month and accurate data from a real database. The API returns a lot of info but I focused on calories since that's what my app tracks. I'm familiar with API integration so structuring requests and handling responses wasn't new, but each API has its own quirks. Most importantly I made sure to handle errors gracefully - if the API fails, users get a clear error message, not a crash. This fits with my focus on user experience and error handling.

I stored food logs as a list of dictionaries in JSON. Each entry has id, date in ISO format, food name, quantity, unit, calories, and timestamp. I'm familiar with JSON from other work, but designing the structure for date-based filtering and historical summaries took some thought. I chose ISO date strings to make date comparisons easy and grouping by day straightforward.

My focus on user experience and error handling paid off. The app handles edge cases gracefully - if someone types a command wrong they get a helpful message, not a crash. If the API fails they know what went wrong. If they forget to set API keys, the error tells them exactly what to do. This made the app feel polished.

Choosing Edamam was the right call. Users get accurate calorie info from a real database, not AI guesses. This fits with my value of data integrity - I wanted users to trust the information.

Using regex for command parsing made the app way more user-friendly. Users don't have to memorize exact syntax - they can type exit or quit or q, use any capitalization, and it works. This flexibility makes it feel natural.

Separating everything into different files like main.py, foods.py, storage.py, api_client.py, and agents.py made the code easier to work with. When I needed to fix something I knew where to look. This also made error handling easier - each module handles its own errors.

Using both Edamam and OpenAI showed I could integrate multiple APIs. Edamam gives accurate data for data integrity, OpenAI provides smart recommendations for user experience. The fallback system makes it more robust - if one API isn't available, the app still works.

At first I hardcoded API keys in the code which was stupid. Then I learned about environment variables and moved everything to os.getenv(). Good security lesson, but more importantly it improved user experience - users set their keys once and the app remembers them.

Early on my code would crash if the data directory didn't exist. Terrible user experience - the app would just break on first use. I had to add os.makedirs(DATA_DIR, exist_ok=True) to create it automatically. Simple fix but it showed me how important it is to think about what happens when someone uses your app for the first time.

My first version used simple string matching with startswith(). It worked but was too rigid - if users didn't type commands exactly right it would fail. Since I value user experience and wanted dynamic input handling, I switched to regex. I already knew regex so I rewrote the command parsing to use regex patterns. This made the app way more forgiving - users can type commands in various ways and it still works.

Understanding the Edamam API response format took some trial and error. The JSON structure was nested so I had to figure out the exact path to extract calories. But I stuck with it because I wanted accurate data, not AI estimates. I'm familiar with API integration so handling requests and responses wasn't new, but each API has its own quirks. Most importantly I made sure to handle API errors gracefully - if Edamam is down or returns unexpected data, users get a clear error message, not a crash. This was about applying my focus on error handling to API integration.

I initially tried to make the food logging system too complex - adding meal categories, tags, complex filtering. I realized this was overkill for the assignment so I simplified it to focus on the core features: logging, viewing today's calories, history, and AI recommendations. But I made sure each feature had good error handling and user experience.

This project reinforced my values around user experience, error handling, and data integrity. I applied my existing knowledge to research and choose the best data source Edamam over LLM estimates for data integrity, use regex for dynamic flexible input parsing that handles user variations, design a chat interface that feels natural and forgiving, structure code in a maintainable way, and handle errors gracefully at every level - API failures, invalid input, missing files.

The most valuable part was applying what I already knew to build something that reflects my values. Every time I hit a problem I'd think through solutions, use ChatGPT for quick help when needed, and iterate. But I always kept my priorities in mind: user experience and error handling first, data integrity second. The final app is simple but functional, and I'm proud that I chose to use regex for dynamic input handling and Edamam for accurate nutrition data, even though it added complexity. These weren't learning exercises - they were deliberate technical choices based on what I value.

I think the project shows I can plan, build, debug, and integrate different technologies. But more importantly it shows I value the user's experience and the integrity of the data they're working with. These aren't just technical choices - they're about building something people can actually trust and use.
