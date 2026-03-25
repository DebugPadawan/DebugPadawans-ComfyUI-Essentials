import json
import re
from typing import List, Tuple, Union

class TextSplitter:
    """
    Node for splitting text strings by a delimiter.
    Supports simple strings or regular expressions.
    """

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ("STRING", {"multiline": True, "default": "apple,banana,orange"}),
                "delimiter": ("STRING", {"multiline": False, "default": ","}),
                "is_regex": ("BOOLEAN", {"default": False}),
            },
            "optional": {
                "strip_whitespace": ("BOOLEAN", {"default": True}),
                "remove_empty": ("BOOLEAN", {"default": True}),
            }
        }

    RETURN_TYPES = ("LIST", "INT")
    RETURN_NAMES = ("text_list", "count")
    FUNCTION = "split_text"
    CATEGORY = "DebugPadawan/Text"

    def split_text(self, text: str, delimiter: str, is_regex: bool = False, strip_whitespace: bool = True, remove_empty: bool = True) -> Tuple[List[str], int]:
        if not text:
            return ([], 0)
            
        if is_regex:
            try:
                result = re.split(delimiter, text)
            except re.error:
                # Fallback to simple split if regex is invalid
                result = text.split(delimiter)
        else:
            result = text.split(delimiter)

        if strip_whitespace:
            result = [item.strip() for item in result]

        if remove_empty:
            result = [item for item in result if item]

        return (result, len(result))


class TextJoiner:
    """
    Node for joining a list of strings with a delimiter.
    """

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text_list": ("LIST",),
                "delimiter": ("STRING", {"multiline": False, "default": ", "}),
            },
            "optional": {
                "prefix": ("STRING", {"multiline": False, "default": ""}),
                "suffix": ("STRING", {"multiline": False, "default": ""}),
                "skip_empty": ("BOOLEAN", {"default": True}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("joined_text",)
    FUNCTION = "join_text"
    CATEGORY = "DebugPadawan/Text"

    def join_text(self, text_list: List, delimiter: str, prefix: str = "", suffix: str = "", skip_empty: bool = True) -> Tuple[str]:
        if not text_list:
            return (prefix + suffix,)
            
        str_list = [str(item) for item in text_list]
        if skip_empty:
            str_list = [s for s in str_list if s.strip()]
            
        result = delimiter.join(str_list)
        result = prefix + result + suffix
        return (result,)


class TextTemplate:
    """
    Node for flexible string templating using Python's format method.
    Useful for constructing complex prompts or filenames.
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "template": ("STRING", {"multiline": True, "default": "A {subject} in the style of {artist}"}),
                "input_1": ("*", {"forceInput": True}),
            },
            "optional": {
                "input_2": ("*", {"forceInput": True}),
                "input_3": ("*", {"forceInput": True}),
                "input_4": ("*", {"forceInput": True}),
            }
        }
        
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("formatted_text",)
    FUNCTION = "format_template"
    CATEGORY = "DebugPadawan/Text"
    
    def format_template(self, template: str, input_1=None, input_2=None, input_3=None, input_4=None) -> Tuple[str]:
        try:
            # We use a simple replacement if the user doesn't use {0}, {1} etc.
            # but rather named or positional arguments.
            # To be most flexible, we provide both positional and 'valX' names.
            kwargs = {
                "val1": input_1, "val2": input_2, "val3": input_3, "val4": input_4,
                "input_1": input_1, "input_2": input_2, "input_3": input_3, "input_4": input_4
            }
            result = template.format(input_1, input_2, input_3, input_4, **kwargs)
            return (result,)
        except Exception as e:
            return (f"Error: {str(e)}",)


class TextCaseConverter:
    """
    Comprehensive case converter for text.
    Correctly handles snake_case, camelCase, etc.
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ("STRING", {"multiline": True, "default": "hello world"}),
                "mode": (["UPPER", "lower", "Title Case", "Sentence case", "snake_case", "kebab-case", "camelCase", "PascalCase"],),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("converted_text",)
    FUNCTION = "convert_case"
    CATEGORY = "DebugPadawan/Text"
    
    def convert_case(self, text: str, mode: str) -> Tuple[str]:
        if not text:
            return ("",)

        if mode == "UPPER":
            return (text.upper(),)
        elif mode == "lower":
            return (text.lower(),)
        elif mode == "Title Case":
            return (text.title(),)
        elif mode == "Sentence case":
            return ('. '.join(s.strip().capitalize() for s in text.split('. ')),)
            
        # For complex cases, first tokenize
        # Replace non-alphanumeric with spaces, then split
        words = re.sub(r'[^a-zA-Z0-9]', ' ', text).split()
        if not words:
            return (text,)

        if mode == "snake_case":
            return ('_'.join(w.lower() for w in words),)
        elif mode == "kebab-case":
            return ('-'.join(w.lower() for w in words),)
        elif mode == "camelCase":
            return (words[0].lower() + ''.join(w.capitalize() for w in words[1:]),)
        elif mode == "PascalCase":
            return (''.join(w.capitalize() for w in words),)
            
        return (text,)


class TextRegex:
    """
    Advanced Regex node for search, replace, and extraction.
    """

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ("STRING", {"multiline": True, "default": "My phone is 123-456-7890"}),
                "pattern": ("STRING", {"multiline": False, "default": r"(\d{3})-(\d{3}-\d{4})"}),
                "replace": ("STRING", {"multiline": False, "default": r"(\1) \2"}),
            },
            "optional": {
                "flags": (["None", "IGNORECASE", "MULTILINE", "DOTALL"], {"default": "None"}),
            }
        }

    RETURN_TYPES = ("STRING", "LIST", "BOOLEAN")
    RETURN_NAMES = ("text", "matches", "found")
    FUNCTION = "regex_op"
    CATEGORY = "DebugPadawan/Text"

    def regex_op(self, text: str, pattern: str, replace: str = "", flags: str = "None") -> Tuple[str, List[str], bool]:
        if not pattern:
            return (text, [], False)

        re_flags = 0
        if flags == "IGNORECASE": re_flags = re.IGNORECASE
        elif flags == "MULTILINE": re_flags = re.MULTILINE
        elif flags == "DOTALL": re_flags = re.DOTALL

        try:
            compiled = re.compile(pattern, re_flags)
            matches = compiled.findall(text)
            # findall returns tuples if there are multiple groups, let's flatten or stringify
            str_matches = [str(m) for m in matches]
            
            result = compiled.sub(replace, text)
            return (result, str_matches, len(matches) > 0)
        except re.error as e:
            return (f"Regex Error: {str(e)}", [], False)


class TextTrimmer:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ("STRING", {"multiline": True, "default": "  hello world  "}),
                "mode": (["both", "start", "end", "all_whitespace", "collapse_spaces", "remove_newlines"],),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("trimmed_text",)
    FUNCTION = "trim_text"
    CATEGORY = "DebugPadawan/Text"
    
    def trim_text(self, text: str, mode: str) -> Tuple[str]:
        if mode == "both":
            return (text.strip(),)
        elif mode == "start":
            return (text.lstrip(),)
        elif mode == "end":
            return (text.rstrip(),)
        elif mode == "all_whitespace":
            return (''.join(text.split()),)
        elif mode == "collapse_spaces":
            return (' '.join(text.split()),)
        elif mode == "remove_newlines":
            return (text.replace('\n', ' ').replace('\r', ' '),)
        return (text,)


class TextPrefixSuffix:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ("STRING", {"multiline": True, "default": "beautiful"}),
            },
            "optional": {
                "prefix": ("STRING", {"multiline": False, "default": ""}),
                "suffix": ("STRING", {"multiline": False, "default": ""}),
                "add_space": ("BOOLEAN", {"default": True}),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("result_text",)
    FUNCTION = "add_prefix_suffix"
    CATEGORY = "DebugPadawan/Text"
    
    def add_prefix_suffix(self, text: str, prefix: str = "", suffix: str = "", add_space: bool = True) -> Tuple[str]:
        res = text
        if prefix:
            connector = " " if add_space and not prefix.endswith(" ") and not text.startswith(" ") else ""
            res = f"{prefix}{connector}{res}"
        if suffix:
            connector = " " if add_space and not res.endswith(" ") and not suffix.startswith(" ") else ""
            res = f"{res}{connector}{suffix}"
        return (res,)


NODE_CLASS_MAPPINGS = {
    "DebugPadawan_TextSplitter": TextSplitter,
    "DebugPadawan_TextJoiner": TextJoiner, 
    "DebugPadawan_TextTemplate": TextTemplate,
    "DebugPadawan_TextReplace": TextRegex, # Merged replace into Regex or kept separate
    "DebugPadawan_TextRegex": TextRegex,
    "DebugPadawan_TextCaseConverter": TextCaseConverter,
    "DebugPadawan_TextTrimmer": TextTrimmer,
    "DebugPadawan_TextPrefixSuffix": TextPrefixSuffix,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "DebugPadawan_TextSplitter": "Text Splitter",
    "DebugPadawan_TextJoiner": "Text Joiner", 
    "DebugPadawan_TextTemplate": "Text Template (Format)",
    "DebugPadawan_TextReplace": "Text Replace (Legacy)",
    "DebugPadawan_TextRegex": "Text Regex (Pro)",
    "DebugPadawan_TextCaseConverter": "Text Case Converter",
    "DebugPadawan_TextTrimmer": "Text Trimmer",
    "DebugPadawan_TextPrefixSuffix": "Text Prefix Suffix",
}
