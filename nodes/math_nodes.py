import random
import math

class IntMathOperation:
    """
    Node for performing basic integer math operations
    """
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "a": ("INT", {"default": 0, "step": 1}),
                "b": ("INT", {"default": 0, "step": 1}),
                "operation": (["add", "subtract", "multiply", "divide", "modulo", "power"],),
            }
        }
    
    RETURN_TYPES = ("INT", "FLOAT")
    RETURN_NAMES = ("int_result", "float_result")
    FUNCTION = "perform_math"
    CATEGORY = "DebugPadawan/Math"

    def perform_math(self, a, b, operation):
        if operation == "add":
            res = a + b
        elif operation == "subtract":
            res = a - b
        elif operation == "multiply":
            res = a * b
        elif operation == "divide":
            res = a / b if b != 0 else 0
        elif operation == "modulo":
            res = a % b if b != 0 else 0
        elif operation == "power":
            res = math.pow(a, b)
        else:
            res = 0
            
        return (int(res), float(res))


class FloatMathOperation:
    """
    Node for performing basic float math operations
    """
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "a": ("FLOAT", {"default": 0.0, "step": 0.01}),
                "b": ("FLOAT", {"default": 0.0, "step": 0.01}),
                "operation": (["add", "subtract", "multiply", "divide", "power"],),
            }
        }
    
    RETURN_TYPES = ("FLOAT", "INT")
    RETURN_NAMES = ("float_result", "int_result")
    FUNCTION = "perform_math"
    CATEGORY = "DebugPadawan/Math"

    def perform_math(self, a, b, operation):
        if operation == "add":
            res = a + b
        elif operation == "subtract":
            res = a - b
        elif operation == "multiply":
            res = a * b
        elif operation == "divide":
            res = a / b if b != 0 else 0.0
        elif operation == "power":
            res = math.pow(a, b)
        else:
            res = 0.0
            
        return (float(res), int(res))


class RandomGenerator:
    """
    Node for generating random integers or floats based on a seed
    """
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
                "min_val": ("FLOAT", {"default": 0.0, "step": 0.01}),
                "max_val": ("FLOAT", {"default": 1.0, "step": 0.01}),
                "mode": (["float", "int"],),
            }
        }
    
    RETURN_TYPES = ("FLOAT", "INT")
    RETURN_NAMES = ("float_val", "int_val")
    FUNCTION = "generate"
    CATEGORY = "DebugPadawan/Math"

    def generate(self, seed, min_val, max_val, mode):
        # Initialize the random generator with the seed
        rng = random.Random(seed)
        
        if mode == "float":
            res = rng.uniform(min_val, max_val)
            return (float(res), int(res))
        else:
            # For int mode, ensure min and max are integers
            res = rng.randint(int(min_val), int(max_val))
            return (float(res), int(res))

NODE_CLASS_MAPPINGS = {
    "DebugPadawan_IntMathOperation": IntMathOperation,
    "DebugPadawan_FloatMathOperation": FloatMathOperation,
    "DebugPadawan_RandomGenerator": RandomGenerator,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "DebugPadawan_IntMathOperation": "Int Math Operation",
    "DebugPadawan_FloatMathOperation": "Float Math Operation",
    "DebugPadawan_RandomGenerator": "Random Generator",
}
