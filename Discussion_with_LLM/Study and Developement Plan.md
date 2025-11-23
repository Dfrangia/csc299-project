# Final Project Study and Development Plan

**Project Title:** Personal AI Knowledge and Planning Assistant

**Current Prototype:** `pkm_assistant.py` (Implements PKMS, CLI, and basic AI chat integration.)

## 1. Study Plan: Core Concepts to Master

The final project requires mastery of several Python and software development concepts. Focus on these areas:

|Concept Area|Key Modules / Topics|Relevance to Project|
|---|---|---|
|**Terminal UI**|`typer` (Command structure), `rich` (Optional: Advanced formatting)|Mandatory: Defines the application's interface and user experience.|
|**Data Persistence**|**JSON** (Current), **`sqlite3`** (Advanced), **Neo4J** (Graph DB, Optional)|Mandatory: How you save and load Notes and Tasks (PKMS requirement).|
|**Data Modeling**|Python `dict` and `list` structures, Pydantic (Optional: Data validation)|Crucial for designing the structure of your Notes and Tasks objects.|
|**External APIs**|`requests` (Handling HTTP POST), **Exponential Backoff**, Error Handling (`try/except`)|Mandatory: Robust communication with the Gemini API for the AI Agent.|
|**Agent Design**|Advanced **System Instructions** and **Prompt Engineering**|Core to making your AI smart—teaching it to reference _Notes_ for _Tasks_.|

## 2. Development Roadmap (Prototypes)

This roadmap breaks the project into logical steps, aligning with the incremental development often required in the course structure (Tasks 1-5).

### Phase 1: Prototype 1 (PKMS & AI Chat)

- **Goal:** Establish basic persistence and AI communication.
    
- **Status:** **COMPLETE** (`pkm_assistant.py` currently achieves this).
    
- **Features:** `add_note`, `list_notes`, `chat` (AI uses notes as context).
    
- **Key Learning:** Basic `typer` commands, JSON file I/O, simple `requests` calls.
    

### Phase 2: Prototype 2 (Full PKMS Functionality)

- **Goal:** Make the Notes system fully functional and usable.
    
- **Actionable Tasks:**
    
    1. **Add Search:** Implement a `search-notes <query>` command that finds notes by matching the title or content.
        
    2. **Add Edit/Delete:** Implement `edit-note <id>` and `delete-note <id>` commands.
        
    3. **Improve Context Retrieval:** Modify `get_all_notes_as_context` to only include notes relevant to the AI query (e.g., if the user asks about "Project Alpha," only include notes tagged or titled "Project Alpha").
        

### Phase 3: Prototype 3 (Task Management System)

- **Goal:** Integrate the second required data structure: Tasks.
    
- **Actionable Tasks:**
    
    1. **Data Modeling:** Design the Task structure (e.g., `id`, `title`, `status: [todo, done]`, `priority: [low, medium, high]`, `due_date: [timestamp/string]`).
        
    2. **Add Persistence:** Implement `load_tasks()` and `save_tasks()` (can use a separate `tasks.json` file initially).
        
    3. **Implement Commands:** Add `add-task <title>`, `list-tasks`, and `complete-task <id>`.
        

### Phase 4: Prototype 4 (Integrated AI Planning Agent)

- **Goal:** Create the core agentic feature that connects Notes and Tasks.
    
- **Actionable Tasks:**
    
    1. **Context Unification:** Create a new function, `get_full_context()`, that retrieves **both** Notes and Tasks and formats them together for the AI.
        
    2. **AI Planning Command:** Implement a new command, `agent-plan <timeframe>`, that sends the full context to the AI with a prompt like: "Analyze the open tasks and all personal notes. Propose a schedule/action plan for the next **<timeframe>**."
        
    3. **AI Tagging Agent:** (Optional, high-value) Create a command that uses the AI to automatically assign a `priority` or `due_date` to a newly added task.
        

### Phase 5: Final Refactoring (Database Transition)

- **Goal:** Swap out the simple JSON file system for a more robust data store.
    
- **Actionable Tasks:**
    
    1. **Refactor Storage:** Migrate `load_notes`/`save_notes` and `load_tasks`/`save_tasks` functions to use a single **SQLite database** file (recommended for simplicity and robustness).
        
    2. **Final Polish:** Ensure all commands have clear output and comprehensive docstrings for the `typer` help pages.