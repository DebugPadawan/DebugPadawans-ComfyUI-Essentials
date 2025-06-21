"""
Utility Nodes for ComfyUI
Provides various helper utilities
"""

import time

# from https://github.com/pythongosssss/ComfyUI-Custom-Scripts
class AnyType(str):
    def __ne__(self, __value: object) -> bool:
        return False

any = AnyType("*")

class DebugPrint:
    """
    Node for debugging - prints values to console
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "value": (any, {"forceInput": True}),
            },
            "optional": {
                "label": ("STRING", {
                    "multiline": False,
                    "default": "Debug"
                }),
            }
        }
    
    # Use wildcard for output type to pass through any type
    RETURN_TYPES = ("*",)
    RETURN_NAMES = ("passthrough",)
    
    FUNCTION = "debug_print"
    CATEGORY = "DebugPadawan/Debug"
    
    def debug_print(self, value, label="Debug"):
        """
        Print value to console for debugging
        
        Args:
            value: Any value to print
            label (str): Label for the debug output
            
        Returns:
            The same value (passthrough)
        """
        # Convert the value to a string for debugging purposes
        debug_value = str(value) if not isinstance(value, str) else value
        print(f"[{label}] {type(value).__name__}: {debug_value}")
        
        # Return the original value unchanged
        return (value,)
    
    
class ConditionalString:
    """
    Node for conditional string output based on boolean input
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "condition": ("BOOLEAN",),
                "true_string": ("STRING", {
                    "multiline": True,
                    "default": "True"
                }),
                "false_string": ("STRING", {
                    "multiline": True,
                    "default": "False"
                }),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("result",)
    
    FUNCTION = "conditional_string"
    CATEGORY = "DebugPadawan/Logic"
    
    def conditional_string(self, condition, true_string, false_string):
        """
        Return string based on condition
        
        Args:
            condition (bool): Condition to evaluate
            true_string (str): String to return if True
            false_string (str): String to return if False
            
        Returns:
            str: Selected string
        """
        return (true_string if condition else false_string,)


class WaitNode:
    """
    Node that waits for a specified number of milliseconds before passing the input through
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "value": (any, {"forceInput": True}),
                "wait_time_ms": ("INT", {
                    "default": 1000,  # Default wait time is 1000 ms (1 second)
                    "min": 0,         # Minimum wait time is 0 ms
                }),
            }
        }
    
    # Use wildcard for output type to pass through any type
    RETURN_TYPES = ("*",)
    RETURN_NAMES = ("passthrough",)
    
    FUNCTION = "wait_and_pass"
    CATEGORY = "DebugPadawan/Utilities"
    
    def wait_and_pass(self, value, wait_time_ms):
        """
        Wait for the specified time and pass the input through
        
        Args:
            value: Any value to pass through
            wait_time_ms (int): Time to wait in milliseconds
            
        Returns:
            The same value (passthrough)
        """
        # Convert milliseconds to seconds and wait
        time.sleep(wait_time_ms / 1000.0)
        
        # Return the original value unchanged
        return (value,)


# Add these to the main mappings if needed
UTILITY_NODE_CLASS_MAPPINGS = {
    "DebugPadawan_DebugPrint": DebugPrint,
    "DebugPadawan_ConditionalString": ConditionalString,
    "DebugPadawan_WaitNode": WaitNode,
}

UTILITY_NODE_DISPLAY_NAME_MAPPINGS = {
    "DebugPadawan_DebugPrint": "Debug Print",
    "DebugPadawan_ConditionalString": "Conditional String",
    "DebugPadawan_WaitNode": "Wait Node",
}