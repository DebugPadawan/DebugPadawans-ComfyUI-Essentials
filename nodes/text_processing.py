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


class TextCaseConverter:
    """
    Node for converting text to different case styles
    Useful for formatting prompts, filenames, and display text
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ("STRING", {
                    "multiline": True,
                    "default": "hello world"
                }),
                "case_mode": (["UPPER", "lower", "Title Case", "Sentence case", "snake_case", "kebab-case", "camelCase", "PascalCase"],),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("converted_text",)
    
    FUNCTION = "convert_case"
    CATEGORY = "DebugPadawan/Text"
    
    def convert_case(self, text, case_mode):
        """
        Convert text to the specified case style
        """
        if case_mode == "UPPER":
            return (text.upper(),)
        elif case_mode == "lower":
            return (text.lower(),)
        elif case_mode == "Title Case":
            return (text.title(),)
        elif case_mode == "Sentence case":
            # Capitalize first letter of each sentence
            result = '. '.join(s.capitalize() for s in text.split('. '))
            return (result,)
        elif case_mode == "snake_case":
            # Convert to snake_case
            # First normalize spaces and existing separators
            normalized = text.lower().replace('-', ' ').replace('_', ' ')
            words = normalized.split()
            return ('_'.join(words),)
        elif case_mode == "kebab-case":
            # Convert to kebab-case
            normalized = text.lower().replace('_', ' ').replace('-', ' ')
            words = normalized.split()
            return ('-'.join(words),)
        elif case_mode == "camelCase":
            # Convert to camelCase
            normalized = text.replace('-', ' ').replace('_', ' ')
            words = normalized.split()
            if not words:
                return ("",)
            result = words[0].lower() + ''.join(w.capitalize() for w in words[1:])
            return (result,)
        elif case_mode == "PascalCase":
            # Convert to PascalCase
            normalized = text.replace('-', ' ').replace('_', ' ')
            words = normalized.split()
            result = ''.join(w.capitalize() for w in words)
            return (result,)
        else:
            return (text,)


class TextTrimmer:
    """
    Node for trimming text with various options
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ("STRING", {
                    "multiline": True,
                    "default": "  hello world  "
                }),
                "mode": (["both", "start", "end", "all_whitespace", "collapse_spaces"],),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("trimmed_text",)
    
    FUNCTION = "trim_text"
    CATEGORY = "DebugPadawan/Text"
    
    def trim_text(self, text, mode):
        """
        Trim text based on the specified mode
        """
        if mode == "both":
            return (text.strip(),)
        elif mode == "start":
            return (text.lstrip(),)
        elif mode == "end":
            return (text.rstrip(),)
        elif mode == "all_whitespace":
            # Remove all whitespace characters
            return (''.join(text.split()),)
        elif mode == "collapse_spaces":
            # Collapse multiple spaces into single spaces
            return (' '.join(text.split()),)
        else:
            return (text,)


class TextPrefixSuffix:
    """
    Node for adding prefix and/or suffix to text
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ("STRING", {
                    "multiline": True,
                    "default": "beautiful"
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
                "add_space": ("BOOLEAN", {"default": True}),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("result_text",)
    
    FUNCTION = "add_prefix_suffix"
    CATEGORY = "DebugPadawan/Text"
    
    def add_prefix_suffix(self, text, prefix="", suffix="", add_space=True):
        result = text
        
        if prefix:
            if add_space and text and not text.startswith(' '):
                result = prefix + ' ' + result
            else:
                result = prefix + result
        
        if suffix:
            if add_space and text and not text.endswith(' '):
                result = result + ' ' + suffix
            else:
                result = result + suffix
        
        return (result,)


NODE_CLASS_MAPPINGS = {
    "DebugPadawan_TextSplitter": TextSplitter,
    "DebugPadawan_TextJoiner": TextJoiner, 
    "DebugPadawan_TextReplace": TextReplace,
    "DebugPadawan_TextRegex": TextRegex,
    "DebugPadawan_TextCaseConverter": TextCaseConverter,
    "DebugPadawan_TextTrimmer": TextTrimmer,
    "DebugPadawan_TextPrefixSuffix": TextPrefixSuffix,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "DebugPadawan_TextSplitter": "Text Splitter",
    "DebugPadawan_TextJoiner": "Text Joiner", 
    "DebugPadawan_TextReplace": "Text Replace",
    "DebugPadawan_TextRegex": "Text Regex (Search & Replace)",
    "DebugPadawan_TextCaseConverter": "Text Case Converter",
    "DebugPadawan_TextTrimmer": "Text Trimmer",
    "DebugPadawan_TextPrefixSuffix": "Text Prefix Suffix",
}
