import json

class JSONToText:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "json_data": ("JSON", {"forceInput": True}),
                "indent": ("INT", {"default": 0, "min": 0, "max": 10, "step": 1}),
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "json_to_text"
    CATEGORY = "DebugPadawan/JSON"
    DESCRIPTION = "Converts a JSON object back into a formatted string"

    def json_to_text(self, json_data, indent):
        if indent > 0:
            return (json.dumps(json_data, indent=indent),)
        else:
            return (json.dumps(json_data),)

# A dictionary that contains all nodes you want to export with their names
NODE_CLASS_MAPPINGS = {
    "DP_JSONToText": JSONToText
}

# A dictionary that contains the friendly names for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "DP_JSONToText": "JSON To Text"
}
