"""
Type Conversion Nodes for ComfyUI
Converts between different data types: int, float, string, boolean
"""


class TypeConverter:
    """
    Node for converting between different data types
    Supports: int, float, string, boolean conversions
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "value": ("*", {"forceInput": True}),
                "output_type": (["string", "int", "float", "boolean"],),
            }
        }
    
    RETURN_TYPES = ("*",)
    RETURN_NAMES = ("converted",)
    
    FUNCTION = "convert"
    CATEGORY = "DebugPadawan/Conversion"
    
    def convert(self, value, output_type):
        """
        Convert value to the specified output type
        
        Args:
            value: Input value of any type
            output_type: Target type (string, int, float, boolean)
            
        Returns:
            Converted value
        """
        try:
            if output_type == "string":
                return (str(value),)
            
            elif output_type == "int":
                # Handle boolean conversion
                if isinstance(value, bool):
                    return (int(value),)
                # Handle string conversion
                if isinstance(value, str):
                    # Try to parse as float first (handles "3.14" -> 3)
                    try:
                        return (int(float(value)),)
                    except ValueError:
                        raise ValueError(f"Cannot convert '{value}' to int")
                # Handle float
                return (int(value),)
            
            elif output_type == "float":
                # Handle boolean conversion
                if isinstance(value, bool):
                    return (float(value),)
                # Handle string conversion
                if isinstance(value, str):
                    try:
                        return (float(value),)
                    except ValueError:
                        raise ValueError(f"Cannot convert '{value}' to float")
                # Handle int or float
                return (float(value),)
            
            elif output_type == "boolean":
                # String to boolean
                if isinstance(value, str):
                    lower_val = value.strip().lower()
                    if lower_val in ("true", "yes", "1", "on"):
                        return (True,)
                    elif lower_val in ("false", "no", "0", "off", ""):
                        return (False,)
                    else:
                        # Non-empty string that's not a known false value
                        return (True,)
                # Numeric to boolean
                if isinstance(value, (int, float)):
                    return (bool(value),)
                # Default bool conversion
                return (bool(value),)
            
            else:
                return (value,)
                
        except Exception as e:
            raise ValueError(f"Type conversion error: {str(e)}")


class IntToFloat:
    """
    Dedicated node for converting int to float
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "value": ("INT", {"default": 0}),
            }
        }
    
    RETURN_TYPES = ("FLOAT",)
    RETURN_NAMES = ("float_value",)
    
    FUNCTION = "convert"
    CATEGORY = "DebugPadawan/Conversion"
    
    def convert(self, value):
        return (float(value),)


class FloatToInt:
    """
    Dedicated node for converting float to int
    Supports different rounding modes
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "value": ("FLOAT", {"default": 0.0}),
                "mode": (["round", "floor", "ceil"],),
            }
        }
    
    RETURN_TYPES = ("INT",)
    RETURN_NAMES = ("int_value",)
    
    FUNCTION = "convert"
    CATEGORY = "DebugPadawan/Conversion"
    
    def convert(self, value, mode):
        import math
        if mode == "round":
            return (round(value),)
        elif mode == "floor":
            return (math.floor(value),)
        elif mode == "ceil":
            return (math.ceil(value),)
        return (int(value),)


class StringToInt:
    """
    Dedicated node for converting string to int
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "value": ("STRING", {"multiline": False, "default": "0"}),
            }
        }
    
    RETURN_TYPES = ("INT",)
    RETURN_NAMES = ("int_value",)
    
    FUNCTION = "convert"
    CATEGORY = "DebugPadawan/Conversion"
    
    def convert(self, value):
        try:
            # Handle float strings by converting to float first
            return (int(float(value)),)
        except ValueError:
            raise ValueError(f"Cannot convert '{value}' to int")


class StringToFloat:
    """
    Dedicated node for converting string to float
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "value": ("STRING", {"multiline": False, "default": "0.0"}),
            }
        }
    
    RETURN_TYPES = ("FLOAT",)
    RETURN_NAMES = ("float_value",)
    
    FUNCTION = "convert"
    CATEGORY = "DebugPadawan/Conversion"
    
    def convert(self, value):
        try:
            return (float(value),)
        except ValueError:
            raise ValueError(f"Cannot convert '{value}' to float")


class StringToBoolean:
    """
    Dedicated node for converting string to boolean
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "value": ("STRING", {"multiline": False, "default": "false"}),
            }
        }
    
    RETURN_TYPES = ("BOOLEAN",)
    RETURN_NAMES = ("bool_value",)
    
    FUNCTION = "convert"
    CATEGORY = "DebugPadawan/Conversion"
    
    def convert(self, value):
        lower_val = value.strip().lower()
        if lower_val in ("true", "yes", "1", "on"):
            return (True,)
        elif lower_val in ("false", "no", "0", "off", ""):
            return (False,)
        else:
            # Non-empty string that's not a recognized false value is True
            return (True,)


class NumberToString:
    """
    Dedicated node for converting numbers (int/float) to string
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "value": ("FLOAT", {"default": 0.0}),
                "decimal_places": ("INT", {"default": 2, "min": 0, "max": 10}),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("string_value",)
    
    FUNCTION = "convert"
    CATEGORY = "DebugPadawan/Conversion"
    
    def convert(self, value, decimal_places):
        if decimal_places == 0:
            return (str(int(round(value))),)
        else:
            return (f"{value:.{decimal_places}f}",)


NODE_CLASS_MAPPINGS = {
    "DebugPadawan_TypeConverter": TypeConverter,
    "DebugPadawan_IntToFloat": IntToFloat,
    "DebugPadawan_FloatToInt": FloatToInt,
    "DebugPadawan_StringToInt": StringToInt,
    "DebugPadawan_StringToFloat": StringToFloat,
    "DebugPadawan_StringToBoolean": StringToBoolean,
    "DebugPadawan_NumberToString": NumberToString,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "DebugPadawan_TypeConverter": "Type Converter",
    "DebugPadawan_IntToFloat": "Int to Float",
    "DebugPadawan_FloatToInt": "Float to Int",
    "DebugPadawan_StringToInt": "String to Int",
    "DebugPadawan_StringToFloat": "String to Float",
    "DebugPadawan_StringToBoolean": "String to Boolean",
    "DebugPadawan_NumberToString": "Number to String",
}