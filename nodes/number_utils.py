"""
Number Utility Nodes for ComfyUI
Provides number formatting, clamping, and mathematical helpers
"""
import math


class NumberClamp:
    """
    Node for clamping a number between min and max values
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "value": ("FLOAT", {"default": 0.0}),
                "min_val": ("FLOAT", {"default": 0.0}),
                "max_val": ("FLOAT", {"default": 1.0}),
            }
        }
    
    RETURN_TYPES = ("FLOAT",)
    RETURN_NAMES = ("clamped",)
    
    FUNCTION = "clamp"
    CATEGORY = "DebugPadawan/Number"
    
    def clamp(self, value, min_val, max_val):
        result = max(min_val, min(value, max_val))
        return (result,)


class NumberRound:
    """
    Node for rounding numbers with precision control
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "value": ("FLOAT", {"default": 0.0}),
                "decimal_places": ("INT", {"default": 2, "min": 0, "max": 10}),
            }
        }
    
    RETURN_TYPES = ("FLOAT", "STRING")
    RETURN_NAMES = ("rounded", "rounded_string")
    
    FUNCTION = "round_num"
    CATEGORY = "DebugPadawan/Number"
    
    def round_num(self, value, decimal_places):
        rounded = round(value, decimal_places)
        formatted = f"{rounded:.{decimal_places}f}"
        return (rounded, formatted)


class NumberRange:
    """
    Node for generating a range of numbers (like Python's range)
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "start": ("INT", {"default": 0}),
                "end": ("INT", {"default": 10}),
                "step": ("INT", {"default": 1}),
            }
        }
    
    RETURN_TYPES = ("LIST", "INT")
    RETURN_NAMES = ("range_list", "count")
    
    FUNCTION = "generate_range"
    CATEGORY = "DebugPadawan/Number"
    
    def generate_range(self, start, end, step):
        if step == 0:
            raise ValueError("Step cannot be zero")
        
        if step > 0:
            result = list(range(start, end, step))
        else:
            result = list(range(start, end, step))
        
        return (result, len(result))


class NumberCompare:
    """
    Node for comparing two numbers
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "a": ("FLOAT", {"default": 0.0}),
                "b": ("FLOAT", {"default": 0.0}),
                "comparison": (["equal", "not equal", "greater", "less", "greater or equal", "less or equal"],),
            }
        }
    
    RETURN_TYPES = ("BOOLEAN", "STRING")
    RETURN_NAMES = ("result", "result_text")
    
    FUNCTION = "compare"
    CATEGORY = "DebugPadawan/Number"
    
    def compare(self, a, b, comparison):
        import math
        
        if comparison == "equal":
            result = abs(a - b) < 1e-9  # Float comparison with tolerance
        elif comparison == "not equal":
            result = abs(a - b) >= 1e-9
        elif comparison == "greater":
            result = a > b
        elif comparison == "less":
            result = a < b
        elif comparison == "greater or equal":
            result = a >= b
        elif comparison == "less or equal":
            result = a <= b
        else:
            result = False
        
        return (result, str(result))


class NumberAbs:
    """
    Node for getting the absolute value of a number
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "value": ("FLOAT", {"default": 0.0}),
            }
        }
    
    RETURN_TYPES = ("FLOAT",)
    RETURN_NAMES = ("absolute",)
    
    FUNCTION = "abs_value"
    CATEGORY = "DebugPadawan/Number"
    
    def abs_value(self, value):
        return (abs(value),)


class NumberSign:
    """
    Node for getting the sign of a number (-1, 0, or 1)
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "value": ("FLOAT", {"default": 0.0}),
            }
        }
    
    RETURN_TYPES = ("INT", "STRING")
    RETURN_NAMES = ("sign", "sign_text")
    
    FUNCTION = "get_sign"
    CATEGORY = "DebugPadawan/Number"
    
    def get_sign(self, value):
        if value > 0:
            return (1, "positive")
        elif value < 0:
            return (-1, "negative")
        else:
            return (0, "zero")


class NumberRemap:
    """
    Node for remapping a value from one range to another
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "value": ("FLOAT", {"default": 0.5}),
                "from_min": ("FLOAT", {"default": 0.0}),
                "from_max": ("FLOAT", {"default": 1.0}),
                "to_min": ("FLOAT", {"default": 0.0}),
                "to_max": ("FLOAT", {"default": 100.0}),
            }
        }
    
    RETURN_TYPES = ("FLOAT",)
    RETURN_NAMES = ("remapped",)
    
    FUNCTION = "remap"
    CATEGORY = "DebugPadawan/Number"
    
    def remap(self, value, from_min, from_max, to_min, to_max):
        if from_max == from_min:
            raise ValueError("from_min and from_max cannot be equal")
        
        # Normalize value to 0-1 range
        normalized = (value - from_min) / (from_max - from_min)
        # Remap to target range
        result = to_min + normalized * (to_max - to_min)
        return (result,)


class NumberLerp:
    """
    Node for linear interpolation between two values
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "a": ("FLOAT", {"default": 0.0}),
                "b": ("FLOAT", {"default": 1.0}),
                "t": ("FLOAT", {"default": 0.5, "min": 0.0, "max": 1.0}),
            }
        }
    
    RETURN_TYPES = ("FLOAT",)
    RETURN_NAMES = ("lerped",)
    
    FUNCTION = "lerp"
    CATEGORY = "DebugPadawan/Number"
    
    def lerp(self, a, b, t):
        result = a + t * (b - a)
        return (result,)


NODE_CLASS_MAPPINGS = {
    "DebugPadawan_NumberClamp": NumberClamp,
    "DebugPadawan_NumberRound": NumberRound,
    "DebugPadawan_NumberRange": NumberRange,
    "DebugPadawan_NumberCompare": NumberCompare,
    "DebugPadawan_NumberAbs": NumberAbs,
    "DebugPadawan_NumberSign": NumberSign,
    "DebugPadawan_NumberRemap": NumberRemap,
    "DebugPadawan_NumberLerp": NumberLerp,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "DebugPadawan_NumberClamp": "Number Clamp",
    "DebugPadawan_NumberRound": "Number Round",
    "DebugPadawan_NumberRange": "Number Range",
    "DebugPadawan_NumberCompare": "Number Compare",
    "DebugPadawan_NumberAbs": "Number Absolute",
    "DebugPadawan_NumberSign": "Number Sign",
    "DebugPadawan_NumberRemap": "Number Remap",
    "DebugPadawan_NumberLerp": "Number Lerp",
}