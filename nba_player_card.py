import openai
from dotenv import dotenv_values

config = dotenv_values(".env")
openai.api_key = config["OPENAI_API_KEY"]


def generate(player_name: str):
    """
    Generates an NBA player card analysis for a given player using a direct prompt
    with the OpenAI Chat Completions API.

    Args:
        player_name (str): The name of the NBA player to analyze.

    Returns:
        str: A formatted NBA player card analysis, or an error message.
    """

    prompt_content = (
        f"Provide a comprehensive NBA Player Card analysis for {player_name}. "
        "Include their full profile, key statistics (raw and advanced like PER, TS%, +/-), "
        "primary offensive and defensive strengths, significant weaknesses or areas for improvement, "
        "and a critical analysis of how their attributes impact team wins (leveraging strengths, mitigating/utilizing weaknesses). "
        "Format your response clearly as an NBA Player Card."
    )
    try:
        response = openai.completions.create(
            model="gpt-4o-mini",
            prompt=prompt_content,
            max_tokens=1500,
            temperature=0.3
        )
        return response.choices[0].text
    except Exception as e:
        return f"An error occurred: {e}"
