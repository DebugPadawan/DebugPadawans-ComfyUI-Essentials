"""
Text Comparison Node
Compare two text strings with various operations
"""

class TextCompare:
    """
    Node for comparing two text strings
    Returns a boolean result based on the comparison mode
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text_a": ("STRING", {
                    "multiline": True,
                    "default": ""
                }),
                "text_b": ("STRING", {
                    "multiline": True,
                    "default": ""
                }),
                "mode": (["equals", "not equals", "contains", "starts with", "ends with"], {
                    "default": "equals"
                }),
            },
            "optional": {
                "case_sensitive": ("BOOLEAN", {"default": True}),
            }
        }
    
    RETURN_TYPES = ("BOOLEAN", "STRING")
    RETURN_NAMES = ("result", "result_text")
    
    FUNCTION = "compare"
    CATEGORY = "DebugPadawan/Text"
    
    def compare(self, text_a, text_b, mode, case_sensitive=True):
        """
        Compare two strings based on the selected mode
        
        Args:
            text_a (str): First text to compare
            text_b (str): Second text to compare
            mode (str): Comparison mode (equals, not equals, contains, starts with, ends with)
            case_sensitive (bool): Whether comparison is case sensitive
            
        Returns:
            tuple: (boolean result, result as string "True"/"False")
        """
        if not case_sensitive:
            text_a = text_a.lower()
            text_b = text_b.lower()
        
        result = False
        
        if mode == "equals":
            result = text_a == text_b
        elif mode == "not equals":
            result = text_a != text_b
        elif mode == "contains":
            result = text_b in text_a
        elif mode == "starts with":
            result = text_a.startswith(text_b)
        elif mode == "ends with":
            result = text_a.endswith(text_b)
        
        return (result, "True" if result else "False")


class TextLength:
    """
    Node for getting the length of a text string
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ("STRING", {
                    "multiline": True,
                    "default": ""
                }),
            },
            "optional": {
                "count_mode": (["characters", "words", "lines"], {
                    "default": "characters"
                }),
            }
        }
    
    RETURN_TYPES = ("INT", "STRING")
    RETURN_NAMES = ("length", "length_text")
    
    FUNCTION = "get_length"
    CATEGORY = "DebugPadawan/Text"
    
    def get_length(self, text, count_mode="characters"):
        """
        Get the length of text in different modes
        
        Args:
            text (str): The text to measure
            count_mode (str): What to count (characters, words, lines)
            
        Returns:
            tuple: (length as int, length as string)
        """
        if count_mode == "characters":
            length = len(text)
        elif count_mode == "words":
            # Split by whitespace and filter empty strings
            words = [w for w in text.split() if w]
            length = len(words)
        elif count_mode == "lines":
            lines = text.split('\n')
            length = len(lines)
        else:
            length = len(text)
        
        return (length, str(length))


class TextCase:
    """
    Node for transforming text case
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ("STRING", {
                    "multiline": True,
                    "default": ""
                }),
                "mode": (["uppercase", "lowercase", "capitalize", "title case", "swap case"], {
                    "default": "lowercase"
                }),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("result",)
    
    FUNCTION = "transform_case"
    CATEGORY = "DebugPadawan/Text"
    
    def transform_case(self, text, mode):
        """
        Transform the case of the text
        
        Args:
            text (str): The text to transform
            mode (str): Case transformation mode
            
        Returns:
            tuple: (transformed text,)
        """
        if mode == "uppercase":
            result = text.upper()
        elif mode == "lowercase":
            result = text.lower()
        elif mode == "capitalize":
            result = text.capitalize()
        elif mode == "title case":
            result = text.title()
        elif mode == "swap case":
            result = text.swapcase()
        else:
            result = text
        
        return (result,)


class TextTrim:
    """
    Node for trimming whitespace from text
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ("STRING", {
                    "multiline": True,
                    "default": ""
                }),
                "mode": (["both", "left", "right", "all"], {
                    "default": "both"
                }),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("result",)
    
    FUNCTION = "trim"
    CATEGORY = "DebugPadawan/Text"
    
    def trim(self, text, mode):
        """
        Trim whitespace from text
        
        Args:
            text (str): The text to trim
            mode (str): Where to trim (both, left, right, all)
            
        Returns:
            tuple: (trimmed text,)
        """
        if mode == "both":
            result = text.strip()
        elif mode == "left":
            result = text.lstrip()
        elif mode == "right":
            result = text.rstrip()
        elif mode == "all":
            # Remove all whitespace including newlines and collapse multiple spaces
            result = ' '.join(text.split())
        else:
            result = text
        
        return (result,)


NODE_CLASS_MAPPINGS = {
    "DebugPadawan_TextCompare": TextCompare,
    "DebugPadawan_TextLength": TextLength,
    "DebugPadawan_TextCase": TextCase,
    "DebugPadawan_TextTrim": TextTrim,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "DebugPadawan_TextCompare": "Text Compare",
    "DebugPadawan_TextLength": "Text Length",
    "DebugPadawan_TextCase": "Text Case",
    "DebugPadawan_TextTrim": "Text Trim",
}