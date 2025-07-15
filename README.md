# Reddit User Persona Generator

## Project Overview
This project generates a detailed user persona for a given Reddit profile by scraping their posts and comments, then using Google Gemini LLM (via the Gemini API) to analyze the content and extract persona characteristics. Each characteristic is supported by evidence (a quote or summary from a post/comment) and a citation (permalink to the source). This tool is designed for AI/LLM internship assignment purposes and demonstrates skills in data scraping, prompt engineering, and LLM integration.

## Features
- Input: Reddit user profile URL
- Scrapes up to 100 posts and comments using PRAW
- Builds a persona with detailed characteristics:
  - Interests and hobbies
  - Values and beliefs
  - Communication style
  - Expertise or knowledge areas
  - Personality traits (e.g., introvert/extrovert, optimistic/pessimistic)
  - Demographic hints (age, location, profession, if available)
  - Any other notable personal information
- Each trait is supported by evidence and a citation (permalink)
- Outputs persona to a text file in the `output/` directory
- Uses Google Gemini LLM API for advanced persona analysis

## Technology Stack
- **Python 3**
- **PRAW** for Reddit data scraping
- **Google Gemini API** (via `google-generativeai` Python SDK) for LLM-based persona generation

## Setup Instructions
1. **Clone this repository**
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   pip install google-generativeai
   ```
3. **Reddit API Credentials:**
   - Create a Reddit app at https://www.reddit.com/prefs/apps
   - Add your credentials directly in `persona_generator.py` (already hardcoded for demo)
4. **Google Gemini API Key:**
   - The API key is hardcoded in `utils/llm_persona_builder.py` for demonstration purposes. For production, use environment variables.

## Usage
```bash
python persona_generator.py <reddit_profile_url>
```
Example:
```bash
python persona_generator.py https://www.reddit.com/user/kojied/
```

## Output
- The generated persona is saved as a text file in the `output/` directory, named `<username>_persona.txt`.
- Each characteristic includes:
  - Characteristic: [description]
  - Evidence: [quote or summary from post/comment]
  - Source: [permalink]

## Example Output
```
- Characteristic: Interested in technology and cultural topics
  Evidence: "I think there's some kind of cultural appropriation of the New York City scene in general."
  Source: https://www.reddit.com/r/AskReddit/comments/1hnx9q/h1b_holders_what_are_your_thoughts_on_the/

- Characteristic: Engages in discussions about immigration and work visas
  Evidence: "H1B holders, what are your thoughts on the narrative that you are being exploited?"
  Source: https://www.reddit.com/r/AskReddit/comments/1hnx9q/h1b_holders_what_are_your_thoughts_on_the/
```

## Flowchart
The following flowchart illustrates the end-to-end process:

```mermaid
flowchart TD
    A[Start: User provides Reddit Profile URL] --> B[Extract Username from URL]
    B --> C[Initialize Reddit API PRAW with Credentials]
    C --> D[Fetch User Posts (Submissions)]
    C --> E[Fetch User Comments]
    D --> F[Combine Posts and Comments]
    E --> F
    F --> G[Select Top 5 Most Relevant Items]
    G --> H[Format Prompt: Instructions, Traits, Posts, Permalinks]
    H --> I[Initialize Gemini LLM API with API Key]
    I --> J[Send Prompt to Gemini LLM]
    J --> K[Gemini LLM Analyzes Content and Generates Persona]
    K --> L[Parse Output: Ensure Each Characteristic Has Evidence and Citation]
    L --> M[Create or Ensure Output Directory Exists]
    M --> N[Save Persona Output to Text File]
    N --> O[End: Output Persona with Detailed Traits, Evidence, and Citations]
```

## Notes
- This project is for educational and demonstration purposes.
- For production use, do not hardcode API keys; use environment variables or secure vaults.
- The quality of persona generation depends on the LLM and the user's Reddit activity.
- The script follows PEP-8 guidelines and is modular for easy extension.

## License
This project is open-source and free to use for learning and demonstration purposes. 