import os
import google.generativeai as genai
import typing_extensions as typing
from dotenv import load_dotenv
import json

load_dotenv()

# Define the schema for nodes and edges
class NodeSchema(typing.TypedDict):
    id: int
    label: str
    x: float
    y: float

class EdgeSchema(typing.TypedDict):
    source: int
    target: int

class MindMapData(typing.TypedDict):
    nodes: typing.List[NodeSchema]
    edges: typing.List[EdgeSchema]

def get_gemini_data(user_input: str, context: str, mind_map_options: typing.Dict[str, dict], model_type: str) -> typing.Union[MindMapData, str]:
    """
    Calls the Gemini API with a structured prompt to retrieve mind map data
    as JSON containing nodes and edges.
    
    :param user_input: The user's input for generating the mind map.
    :param context: The context or description to guide the generation.
    :param mind_map_options: Predefined mind map options to include in the prompt.
    :return: Mind map data in JSON format or an error message.
    """
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API key is missing. Please set API_KEY in your environment variables.")
    if model_type.lower() == 'fast':
        model_name = 'gemini-1.5-flash'
    elif model_type.lower() == 'quality':
        model_name = 'gemini-1.5-pro'
    else:
        return "Error: Invalid model type. Choose either 'fast' or 'quality'."

    # Configure the API client
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(
        model_name,
        generation_config={
            "response_mime_type": "application/json",
            "response_schema": {
                "type": "object",
                "properties": {
                    "nodes": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "id": {"type": "integer"},
                                "label": {"type": "string"},
                                "x": {"type": "number"},
                                "y": {"type": "number"}
                            },
                            "required": ["id", "label", "x", "y"]
                        }
                    },
                    "edges": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "source": {"type": "integer"},
                                "target": {"type": "integer"}
                            },
                            "required": ["source", "target"]
                        }
                    }
                },
                "required": ["nodes", "edges"]
            }
        }
    )

    # Prepare the final structured prompt with context, user input, and mind map options
    structured_prompt = (
    f"Context: {context}\n\n"
    f"Mind Map Options: {json.dumps(mind_map_options)}\n\n"
    f"Based on the input: '{user_input}', create a detailed JSON representation for a mind map."
    f"The mind map should explain how to address the context based on the input.\n"
    f"Each node should be labeled clearly and positioned in a way that **minimizes overlap**. "
    f"Ensure that the mind map includes:\n"
    f"- **Nodes** with attributes: 'id' (integer), 'label' (string), 'x' (float), 'y' (float).\n"
    f"- **Edges** with attributes: 'source' (integer), 'target' (integer).\n\n"
    f"**Important:** Ensure that the generated mind map is **visually clear and organized**. Nodes should be positioned to **avoid overlap** and provide a **structured view** that highlights the relationships and hierarchy of the content effectively.\n\n"
    f"Example output format:\n"
    f"{{'nodes': [{{'id': 1, 'label': 'Topic', 'x': 0, 'y': 0}}], 'edges': [{{'source': 1, 'target': 2}}]}}\n\n"
)


    try:
        response = model.generate_content(structured_prompt)

        response_text = response.text

        if response_text:
            try:
                mind_map_data = json.loads(response_text)
                return mind_map_data
            except json.JSONDecodeError as parse_error:
                return f"Parsing Error: {str(parse_error)}. Response: {response_text}"
        else:
            return "Error: No text found in response."

    except Exception as e:
        return f"Error: {str(e)}"
