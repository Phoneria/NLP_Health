import pandas as pd
from groq import Groq
import json
GROQ_API_KEY = "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"

def process_action_text(text):
    ACTION_REWRITE_PROMPT = f"""  
    Your task is to process the content of TEXT by following these steps:
    TEXT = {text}
    Remove all date-related information from the text.

    Drop any unnecessary or irrelevant information that does not contribute to the main action.

    Rewrite the text while maintaining the core meaning and emphasizing the "actions" described in the text.

    Output must be just contains what customer should do
    
    Ensure the generated text is concise, focused on the core actions, and contains the word "actions."

    Dont write your prompts like 'Here is the answer' etc.
    
    Give output as bulletpoints as instruction following type

    Just rewrite me text as your output 
    """
    
    client = Groq(api_key=GROQ_API_KEY)
    print("TEXT : ", text)
    chat_completion = client.chat.completions.create(
        messages=[{
            "role": "user",
            "content": ACTION_REWRITE_PROMPT,
        }],
        model="llama3-70b-8192",
    )
    print(chat_completion.choices[0].message.content)
    return chat_completion.choices[0].message.content



# Assuming you have a DataFrame named random_rows
def create_prompt_input(row):
    prompt_input = {
        "TRADE_NAME": row["TRADE_NAME"],
        "FIRM_NAME": row["FIRM_NAME"],
        "MANUFACTURER_RECALL_REASON": row["MANUFACTURER_RECALL_REASON"],
        "Recall Type": row["Recall Type"]
    }
    return json.dumps(prompt_input)

