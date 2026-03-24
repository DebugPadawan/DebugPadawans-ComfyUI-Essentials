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
        """
        result = text.split(delimiter)
        
        if strip_whitespace:
            result = [item.strip() for item in result]
        
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
        str_list = [str(item) for item in text_list]
        result = delimiter.join(str_list)
        result = prefix + result + suffix
        return (result,)


class TextReplace:
    """
    Node for replacing specific text in a string
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ("STRING", {
                    "multiline": True,
                    "default": "A beautiful sunset over the ocean"
                }),
                "find": ("STRING", {
                    "multiline": False,
                    "default": "sunset"
                }),
                "replace": ("STRING", {
                    "multiline": False,
                    "default": "sunrise"
                }),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text",)
    
    FUNCTION = "replace_text"
    CATEGORY = "DebugPadawan/Text"
    
    def replace_text(self, text, find, replace):
        if not find:
            return (text,)
        return (text.replace(find, replace),)


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
        count = len(input_list)
        first_item = str(input_list[0]) if input_list else ""
        last_item = str(input_list[-1]) if input_list else ""
        
        return (count, first_item, last_item)


NODE_CLASS_MAPPINGS = {
    "DebugPadawan_TextSplitter": TextSplitter,
    "DebugPadawan_TextJoiner": TextJoiner,
    "DebugPadawan_TextReplace": TextReplace,
    "DebugPadawan_ListInfo": ListInfo,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "DebugPadawan_TextSplitter": "Text Splitter",
    "DebugPadawan_TextJoiner": "Text Joiner", 
    "DebugPadawan_TextReplace": "Text Replace",
    "DebugPadawan_ListInfo": "List Info",
}
