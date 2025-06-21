import json

class TextToJSON:
    """
    Node for converting a text string to a JSON object.
    Attempts to fix invalid JSON if possible.
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text_input": ("STRING", {
                    "multiline": True,
                    "default": '{"key": "value"}'
                }),
            }
        }
    
    RETURN_TYPES = ("JSON", "STRING")
    RETURN_NAMES = ("json_output", "error_message")
    
    FUNCTION = "convert_to_json"
    CATEGORY = "DebugPadawan/JSON"
    
    def convert_to_json(self, text_input):
        """
        Convert a text string to a JSON object. Attempts to fix invalid JSON.
        
        Args:
            text_input (str): Input text to convert
            
        Returns:
            tuple: (JSON object, error message)
        """
        try:
            # Parse the text input as JSON
            json_output = json.loads(text_input)
            return (json_output, "")
        except json.JSONDecodeError as e:
            # Attempt to fix common JSON issues
            fixed_json = self.try_fix_json(text_input)
            if fixed_json:
                try:
                    json_output = json.loads(fixed_json)
                    return (json_output, "JSON was corrected.")
                except json.JSONDecodeError:
                    pass  # If fixing fails, fall through to error handling
            
            # Return an error message if the JSON is invalid
            return (None, f"Invalid JSON: {str(e)}")
        except Exception as e:
            # Handle other exceptions
            return (None, f"Error: {str(e)}")
    
    def try_fix_json(self, text_input):
        """
        Attempt to fix common JSON formatting issues.
        
        Args:
            text_input (str): Input text to fix
            
        Returns:
            str: Fixed JSON string, or None if it cannot be fixed
        """
        try:
            # Replace single quotes with double quotes
            fixed = text_input.replace("'", '"')
            
            # Add missing commas between JSON objects or arrays
            fixed = fixed.replace("}{", "},{")
            
            # Ensure the JSON starts and ends with braces or brackets
            if not (fixed.startswith("{") or fixed.startswith("[")):
                fixed = "{" + fixed
            if not (fixed.endswith("}") or fixed.endswith("]")):
                fixed = fixed + "}"
            
            return fixed
        except Exception:
            return None


NODE_CLASS_MAPPINGS = {
    "DebugPadawan_TextToJSON": TextToJSON,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "DebugPadawan_TextToJSON": "Text to JSON",
}