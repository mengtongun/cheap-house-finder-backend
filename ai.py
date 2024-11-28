import json
import os

import google.generativeai as genai

from input import Filter
from output import response_format

key = os.getenv("GEMINI_API_KEY", "xyz")
model = os.getenv("GEMINI_MODEL", "learnlm-1.5-pro-experimental")
genai.configure(api_key=key)


def get_prompt(input: Filter):
    return (
        # Prompt Instructions
        "Can you help me find affordable apartment rentals in "
        f"{input.location}? "
        "I'm looking for apartments with a monthly rent under "
        f"USD{input.price}, "
        "ideally with at least "
        f"{input.room} "
        "bedroom, pet-friendly, and within walking "
        "distance of public transportation. "
        "Please recommend websites, local resources, "
        "or specific neighborhoods where I might have "
        "the best chance of finding budget-friendly options."
    )


def find_house(input: Filter):

    # Create the model
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 8192,
        "response_mime_type": "application/json",
    }

    model = genai.GenerativeModel(
        model_name="learnlm-1.5-pro-experimental",
        generation_config=generation_config,
    )

    chat_session = model.start_chat(history=[])

    response = chat_session.send_message(
        (
            "role: as agency an expert house finder, "
            + "searcher and property evaluator "
            + "with an in-depth knowledge of global real estate markets, "
            "role: as property buyer"
            + get_prompt(input)
            + "Make the outputs in JSON format. as follow:"
            + response_format
        )
    )

    return json.loads(response.text)
