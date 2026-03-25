import random
import math
from typing import Tuple, List, Union

class BaseMathOperation:
    def _perform_calculation(self, a: float, b: float, operation: str, is_int: bool = True) -> Tuple[Union[int, float], Union[float, int]]:
        res = 0.0
        if operation == "add": res = a + b
        elif operation == "subtract": res = a - b
        elif operation == "multiply": res = a * b
        elif operation == "divide": res = a / b if b != 0 else 0.0
        elif operation == "modulo": res = a % b if b != 0 else 0.0
        elif operation == "power": res = math.pow(a, b)
        elif operation == "max": res = max(a, b)
        elif operation == "min": res = min(a, b)
        
        if is_int:
            return (int(res), float(res))
        else:
            return (float(res), int(res))

class IntMathOperation(BaseMathOperation):
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "a": ("INT", {"default": 0, "step": 1}),
                "b": ("INT", {"default": 0, "step": 1}),
                "operation": (["add", "subtract", "multiply", "divide", "modulo", "power", "max", "min"],),
            }
        }
    
    RETURN_TYPES = ("INT", "FLOAT")
    RETURN_NAMES = ("int_result", "float_result")
    FUNCTION = "perform_math"
    CATEGORY = "DebugPadawan/Math"

    def perform_math(self, a, b, operation):
        return self._perform_calculation(float(a), float(b), operation, is_int=True)

class FloatMathOperation(BaseMathOperation):
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "a": ("FLOAT", {"default": 0.0, "step": 0.01}),
                "b": ("FLOAT", {"default": 0.0, "step": 0.01}),
                "operation": (["add", "subtract", "multiply", "divide", "power", "max", "min"],),
            }
        }
    
    RETURN_TYPES = ("FLOAT", "INT")
    RETURN_NAMES = ("float_result", "int_result")
    FUNCTION = "perform_math"
    CATEGORY = "DebugPadawan/Math"

    def perform_math(self, a, b, operation):
        return self._perform_calculation(a, b, operation, is_int=False)

class SingleNumberOp:
    """
    Operations on a single number (floor, ceil, rounded, abs, sin, cos).
    """
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "value": ("FLOAT", {"default": 0.0, "step": 0.001}),
                "operation": (["floor", "ceil", "round", "abs", "sin", "cos", "sqrt", "negate"],),
            }
        }
    
    RETURN_TYPES = ("FLOAT", "INT")
    RETURN_NAMES = ("float_val", "int_val")
    FUNCTION = "op"
    CATEGORY = "DebugPadawan/Math"
    
    def op(self, value: float, operation: str) -> Tuple[float, int]:
        res = 0.0
        if operation == "floor": res = float(math.floor(value))
        elif operation == "ceil": res = float(math.ceil(value))
        elif operation == "round": res = float(round(value))
        elif operation == "abs": res = abs(value)
        elif operation == "sin": res = math.sin(value)
        elif operation == "cos": res = math.cos(value)
        elif operation == "sqrt": res = math.sqrt(value) if value >= 0 else 0.0
        elif operation == "negate": res = -value
        
        return (res, int(res))

class MathExpression:
    """
    Evaluates simple mathematical expressions.
    BE CAREFUL: Uses eval(), so keep it strictly math only.
    """
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "expression": ("STRING", {"default": "a * (b + 10)"}),
                "a": ("FLOAT", {"default": 1.0}),
                "b": ("FLOAT", {"default": 1.0}),
            }
        }
    
    RETURN_TYPES = ("FLOAT", "INT")
    RETURN_NAMES = ("float_val", "int_val")
    FUNCTION = "eval_expr"
    CATEGORY = "DebugPadawan/Math"
    
    def eval_expr(self, expression: str, a: float, b: float) -> Tuple[float, int]:
        # Basic sanitization
        safe_dict = {"a": a, "b": b, "math": math, "abs": abs, "round": round, "min": min, "max": max}
        try:
             # This is still slightly risky but okay for a local tool.
             # We should use a proper parser if this were production web.
             # But for ComfyUI, users usually have full local access anyway.
             result = eval(expression, {"__builtins__": {}}, safe_dict)
             f_res = float(result)
             return (f_res, int(f_res))
        except Exception as e:
             print(f"[MathExpression Error] {e}")
             return (0.0, 0)

class RandomGenerator:
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
        rng = random.Random(seed)
        if mode == "float":
            res = rng.uniform(min_val, max_val)
        else:
            res = rng.randint(int(min_val), int(max_val))
        return (float(res), int(res))

NODE_CLASS_MAPPINGS = {
    "DebugPadawan_IntMathOperation": IntMathOperation,
    "DebugPadawan_FloatMathOperation": FloatMathOperation,
    "DebugPadawan_SingleNumberOp": SingleNumberOp,
    "DebugPadawan_MathExpression": MathExpression,
    "DebugPadawan_RandomGenerator": RandomGenerator,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "DebugPadawan_IntMathOperation": "Integer Math",
    "DebugPadawan_FloatMathOperation": "Float Math",
    "DebugPadawan_SingleNumberOp": "Number Transform",
    "DebugPadawan_MathExpression": "Math Expression Solver",
    "DebugPadawan_RandomGenerator": "Random Number Gen",
}
