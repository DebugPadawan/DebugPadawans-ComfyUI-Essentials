class StringFormatter:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "format_string": ("STRING", {"multiline": True, "default": "Result: {input1}, {input2}"}),
            },
            "optional": {
                "input1": ("STRING", {"multiline": True, "default": ""}),
                "input2": ("STRING", {"multiline": True, "default": ""}),
                "input3": ("STRING", {"multiline": True, "default": ""}),
                "input4": ("STRING", {"multiline": True, "default": ""}),
                "input5": ("STRING", {"multiline": True, "default": ""}),
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "format_text"
    CATEGORY = "DebugPadawan/Text"
    DESCRIPTION = "Formats a string using f-string-like syntax with multiple inputs."

    def format_text(self, format_string, input1="", input2="", input3="", input4="", input5=""):
        # Create a dictionary of inputs to be used in the format string
        # Filter out empty inputs if necessary, though format() handles missing keys gracefully.
        inputs = {
            "input1": input1,
            "input2": input2,
            "input3": input3,
            "input4": input4,
            "input5": input5,
        }
        
        # Use str.format_map for f-string-like behavior
        # It's important to provide a default value for any potential missing keys in the format_string
        # For simplicity, we are assuming keys in format_string will match inputX,
        # or that missing ones will not cause an error with a default empty string.
        try:
            formatted_string = format_string.format(**inputs)
        except KeyError as e:
            # Handle cases where format_string contains keys not provided by inputs
            # This can happen if user uses {input6} but only input1-5 are available
            formatted_string = f"Error: Missing input for key {e} in format string."
        except Exception as e:
            formatted_string = f"An unexpected error occurred during formatting: {e}"

        return (formatted_string,)

NODE_CLASS_MAPPINGS = {
    "DP_StringFormatter": StringFormatter
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "DP_StringFormatter": "String Formatter"
}
