import os
import time
from openai import OpenAI

def summarize_task(description: str, client: OpenAI) -> str:
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that summarizes task descriptions into short, concise phrases."},
                {"role": "user", "content": f"Summarize this task description into a short phrase: {description}"}
            ],
            max_tokens=50
        )
        content = response.choices[0].message.content
        if content:
            return content.strip()
        return "Summary unavailable"
    except Exception as e:
        return f"Error: {str(e)}"

def main() -> None:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("Error: OPENAI_API_KEY environment variable not set")
        print("Set it with: $env:OPENAI_API_KEY='your-key-here'")
        return
    
    client = OpenAI(api_key=api_key)
    
    sample_descriptions = [
        "I need to write a comprehensive research paper about endangered species conservation efforts. This involves researching specific endangered animals like the Sumatran tiger and black rhinoceros, analyzing the primary threats to their survival such as habitat loss and poaching, studying current conservation programs and their effectiveness, and proposing new strategies to protect these species. The paper should be 15 pages with proper citations and include data visualizations showing population trends over time.",
        "I have a major assignment due for my data structures and algorithms class. I need to implement a binary search tree with insertion, deletion, and traversal operations, analyze the time complexity of each operation, write unit tests to verify correctness, create a visual representation of the tree structure, and prepare a presentation explaining the implementation choices and performance characteristics. The code must be written in Python and include detailed comments."
    ]
    
    print("=" * 60)
    print("Task Summarization Tool - OpenAI GPT-5 mini")
    print("=" * 60)
    print()
    print(f"Processing {len(sample_descriptions)} task descriptions...")
    print()
    
    summaries = []
    start_time = time.time()
    
    for i, description in enumerate(sample_descriptions, 1):
        print(f"[{i}/{len(sample_descriptions)}] Processing description...")
        task_start = time.time()
        summary = summarize_task(description, client)
        task_time = time.time() - task_start
        summaries.append(summary)
        print(f"  ✓ Summary: {summary} (took {task_time:.2f}s)")
        print()
    
    total_time = time.time() - start_time
    
    print("-" * 60)
    print("FINAL SUMMARIES:")
    print("-" * 60)
    for i, summary in enumerate(summaries, 1):
        print(f"{i}. {summary}")
    print()
    print(f"Total processing time: {total_time:.2f} seconds")
    print("=" * 60)
