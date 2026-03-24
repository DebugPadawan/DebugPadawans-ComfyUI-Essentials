import json
import re


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


class TextRegex:
    """
    Node for searching and replacing text using regular expressions
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ("STRING", {
                    "multiline": True,
                    "default": "My phone number is 123-456-7890"
                }),
                "pattern": ("STRING", {
                    "multiline": False,
                    "default": r"\d{3}-\d{3}-\d{4}"
                }),
                "replace": ("STRING", {
                    "multiline": False,
                    "default": "[REDACTED]"
                }),
            }
        }
    
    RETURN_TYPES = ("STRING", "LIST", "BOOLEAN")
    RETURN_NAMES = ("text", "matches", "found")
    
    FUNCTION = "regex_op"
    CATEGORY = "DebugPadawan/Text"
    
    def regex_op(self, text, pattern, replace):
        if not pattern:
            return (text, [], False)
        
        matches = re.findall(pattern, text)
        result = re.sub(pattern, replace, text)
        
        return (result, matches, len(matches) > 0)


NODE_CLASS_MAPPINGS = {
    "DebugPadawan_TextSplitter": TextSplitter,
    "DebugPadawan_TextJoiner": TextJoiner,
    "DebugPadawan_TextReplace": TextReplace,
    "DebugPadawan_TextRegex": TextRegex,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "DebugPadawan_TextSplitter": "Text Splitter",
    "DebugPadawan_TextJoiner": "Text Joiner", 
    "DebugPadawan_TextReplace": "Text Replace",
    "DebugPadawan_TextRegex": "Text Regex (Search & Replace)",
}
