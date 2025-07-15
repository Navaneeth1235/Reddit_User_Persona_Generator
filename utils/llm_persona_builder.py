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
        "Format the output as follows (fill in as much as possible based on the evidence):\n\n"
        "# [Persona Name]\n\n"
        "**Age:** [age]\n"
        "**Occupation:** [occupation]\n"
        "**Status:** [status]\n"
        "**Location:** [location]\n"
        "**Tier:** [tier]\n"
        "**Archetype:** [archetype]\n\n"
        "**Traits:** Practical | Adaptable | Spontaneous | Active\n\n"
        "---\n\n"
        "## Motivations\n"
        "- Convenience: [bar/score or description]\n"
        "- Wellness: [bar/score or description]\n"
        "- Speed: [bar/score or description]\n"
        "- Preferences: [bar/score or description]\n"
        "- Comfort: [bar/score or description]\n"
        "- Dietary Needs: [bar/score or description]\n\n"
        "---\n\n"
        "## Personality\n"
        "- Introvert/Extrovert: [bar/score or description]\n"
        "- Intuition/Sensing: [bar/score or description]\n"
        "- Feeling/Thinking: [bar/score or description]\n"
        "- Perceiving/Judging: [bar/score or description]\n\n"
        "---\n\n"
        "## Behaviour & Habits\n"
        "- [Bullet point 1]\n"
        "- [Bullet point 2]\n"
        "- [Bullet point 3]\n...\n\n"
        "---\n\n"
        "## Goals & Needs\n"
        "- [Bullet point 1]\n"
        "- [Bullet point 2]\n"
        "- [Bullet point 3]\n...\n\n"
        "---\n\n"
        "## Frustrations\n"
        "- [Bullet point 1]\n"
        "- [Bullet point 2]\n"
        "- [Bullet point 3]\n...\n\n"
        "---\n\n"
        "## Evidence & Citations\n"
        "- [Quote or summary from post/comment]\n  Source: [permalink]\n"
        "- [Quote or summary from post/comment]\n  Source: [permalink]\n...\n\n"
        "Use the posts/comments as evidence and cite the source for each insight.\n\n"
    )
    for i, item in enumerate(user_content[:5]):
        prompt += f"[{item['type'].capitalize()}] {item['content']}\nSource: {item['permalink']}\n\n"
    prompt += "\nPersona: "

    response = model.generate_content(prompt)
    return response.text 