import time

# from https://github.com/pythongosssss/ComfyUI-Custom-Scripts
class AnyType(str):
    def __ne__(self, __value: object) -> bool:
        return False

any = AnyType("*")

class WaitNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "value": (any, {"forceInput": True}),
                "wait_time_seconds": ("FLOAT", {
                    "default": 1.0,  # Default wait time is 1 second
                    "min": 0.0,      # Minimum wait time is 0 seconds
                }),
            }
        }
    
    RETURN_TYPES = ("*",)
    RETURN_NAMES = ("passthrough",)
    
    FUNCTION = "wait_and_pass"
    CATEGORY = "DebugPadawan/Timing"
    
    def wait_and_pass(self, value, wait_time_seconds):
        """
        Wait for the specified time and pass the input through
        
        Args:
            value: Any value to pass through
            wait_time_seconds (float): Time to wait in seconds
            
        Returns:
            The same value (passthrough)
        """
        time.sleep(wait_time_seconds)
        
        return (value,)


TIMING_NODE_CLASS_MAPPINGS = {
    "DebugPadawan_WaitNode": WaitNode,
}

TIMING_NODE_DISPLAY_NAME_MAPPINGS = {
    "DebugPadawan_WaitNode": "Wait Node",
}