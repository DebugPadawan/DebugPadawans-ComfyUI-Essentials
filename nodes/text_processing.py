import json


class TextSplitter:
    """
    Node for splitting text strings by a delimiter
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ("STRING", {
                    "multiline": True,
                    "default": "apple,banana,orange"
                }),
                "delimiter": ("STRING", {
                    "multiline": False,
                    "default": ","
                }),
            },
            "optional": {
                "strip_whitespace": ("BOOLEAN", {
                    "default": True
                }),
                "remove_empty": ("BOOLEAN", {
                    "default": True
                }),
            }
        }
    
    RETURN_TYPES = ("LIST", "INT")
    RETURN_NAMES = ("text_list", "count")
    
    FUNCTION = "split_text"
    CATEGORY = "DebugPadawan/Text"
    
    def split_text(self, text, delimiter, strip_whitespace=True, remove_empty=True):
        """
        Split text by delimiter and return list with count
        
        Args:
            text (str): Input text to split
            delimiter (str): Character(s) to split by
            strip_whitespace (bool): Whether to strip whitespace from each item
            remove_empty (bool): Whether to remove empty strings from result
            
        Returns:
            tuple: (list of strings, count of items)
        """
        # Split the text
        result = text.split(delimiter)
        
        # Strip whitespace if requested
        if strip_whitespace:
            result = [item.strip() for item in result]
        
        # Remove empty strings if requested
        if remove_empty:
            result = [item for item in result if item]
        
        return (result, len(result))


class TextJoiner:
    """
    Node for joining a list of strings with a delimiter
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text_list": ("LIST",),
                "delimiter": ("STRING", {
                    "multiline": False,
                    "default": ", "
                }),
            },
            "optional": {
                "prefix": ("STRING", {
                    "multiline": False,
                    "default": ""
                }),
                "suffix": ("STRING", {
                    "multiline": False,
                    "default": ""
                }),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("joined_text",)
    
    FUNCTION = "join_text"
    CATEGORY = "DebugPadawan/Text"
    
    def join_text(self, text_list, delimiter, prefix="", suffix=""):
        """
        Join list of strings with delimiter
        
        Args:
            text_list (list): List of strings to join
            delimiter (str): String to join with
            prefix (str): String to add at the beginning
            suffix (str): String to add at the end
            
        Returns:
            str: Joined string
        """
        # Convert all items to strings
        str_list = [str(item) for item in text_list]
        
        # Join with delimiter
        result = delimiter.join(str_list)
        
        # Add prefix and suffix
        result = prefix + result + suffix
        
        return (result,)


class ListInfo:
    """
    Node for getting information about a list
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "input_list": ("LIST",),
            }
        }
    
    RETURN_TYPES = ("INT", "STRING", "STRING")
    RETURN_NAMES = ("count", "first_item", "last_item")
    
    FUNCTION = "get_list_info"
    CATEGORY = "DebugPadawan/Utilities"
    
    def get_list_info(self, input_list):
        """
        Get information about a list
        
        Args:
            input_list (list): Input list to analyze
            
        Returns:
            tuple: (count, first_item, last_item)
        """
        count = len(input_list)
        first_item = str(input_list[0]) if input_list else ""
        last_item = str(input_list[-1]) if input_list else ""
        
        return (count, first_item, last_item)


class TextToJSON:
    """
    Node for converting a text string to a JSON object
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
        Convert a text string to a JSON object
        
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
            # Return an error message if the JSON is invalid
            return (None, f"Invalid JSON: {str(e)}")
        except Exception as e:
            # Handle other exceptions
            return (None, f"Error: {str(e)}")


NODE_CLASS_MAPPINGS = {
    "DebugPadawan_TextSplitter": TextSplitter,
    "DebugPadawan_TextJoiner": TextJoiner,
    "DebugPadawan_ListInfo": ListInfo,
    "DebugPadawan_TextToJSON": TextToJSON,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "DebugPadawan_TextSplitter": "Text Splitter",
    "DebugPadawan_TextJoiner": "Text Joiner", 
    "DebugPadawan_ListInfo": "List Info",
    "DebugPadawan_TextToJSON": "Text to JSON",
}