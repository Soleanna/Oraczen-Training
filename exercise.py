import os
import json

# Read transcript
with open("transcript.txt", "r", encoding="utf-8") as file:
    transcript = file.read()

# Ask AI to find important sales information
prompt = """
Read this sales call and find:
- decision
- risk
- commitment
- next_step

For each one, give a short description and the exact quote
from the transcript that supports it. Do not make up quotes.

Transcript:
""" + transcript

# Return
schema = {
    "type": "object",
    "properties": {
        "decision": {
            "type": "object",
            "properties": {
                "value": {"type": "string"},
                "quote": {"type": "string"}
            },
            "required": ["value", "quote"],
            "additionalProperties": False
        },
        "risk": {
            "type": "object",
            "properties": {
                "value": {"type": "string"},
                "quote": {"type": "string"}
            },
            "required": ["value", "quote"],
            "additionalProperties": False
        },
        "commitment": {
            "type": "object",
            "properties": {
                "value": {"type": "string"},
                "quote": {"type": "string"}
            },
            "required": ["value", "quote"],
            "additionalProperties": False
        },
        "next_step": {
            "type": "object",
            "properties": {
                "value": {"type": "string"},
                "quote": {"type": "string"}
            },
            "required": ["value", "quote"],
            "additionalProperties": False
        }
    },
    "required": ["decision", "risk", "commitment", "next_step"],
    "additionalProperties": False
}

# Send transcript to AI
response = client.responses.create(
    model="gpt-5",
    input=prompt,
    text={
        "format": {
            "type": "json_schema",
            "name": "sales_signals",
            "schema": schema,
            "strict": True
        }
    }
)

# Turn response into Python data
result = json.loads(response.output_text)

# Save
with open("output.json", "w", encoding="utf-8") as file:
    json.dump(result, file, indent=2)

print("Saved to output.json")
print(json.dumps(result, indent=2))