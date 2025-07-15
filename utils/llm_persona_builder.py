import os
from typing import List, Dict
import google.generativeai as genai

def build_persona_with_llm(user_content: List[Dict], model_name: str = "gemini-2.0-flash") -> str:
    """
    Uses Google Gemini API to generate a detailed persona summary from user content.
    Cites the source post/comment for each trait.
    Returns the persona as a formatted string.
    """
    api_key = "YOUR_GEMINI_API_KEY"
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(model_name)

    prompt = (
        "Analyze the following Reddit posts and comments and build a detailed user persona. "
        "For each characteristic, cite the post or comment (with its permalink) that supports it.\n\n"
        "Extract and summarize the following characteristics if possible:\n"
        "- Interests and hobbies\n"
        "- Values and beliefs\n"
        "- Communication style\n"
        "- Expertise or knowledge areas\n"
        "- Personality traits (e.g., introvert/extrovert, optimistic/pessimistic)\n"
        "- Demographic hints (age, location, profession, if available)\n"
        "- Any other notable personal information\n\n"
        "For each characteristic, use the following format:\n"
        "- Characteristic: [description]\n"
        "  Evidence: [quote or summary from post/comment]\n"
        "  Source: [permalink]\n\n"
    )
    for i, item in enumerate(user_content[:5]):
        prompt += f"[{item['type'].capitalize()}] {item['content']}\nSource: {item['permalink']}\n\n"
    prompt += "\nPersona: "

    response = model.generate_content(prompt)
    return response.text 