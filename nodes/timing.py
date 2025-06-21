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
                "wait_time_ms": ("INT", {
                    "default": 1000,
                    "min": 0,
                }),
            }
        }
    
    RETURN_TYPES = ("*",)
    RETURN_NAMES = ("passthrough",)
    
    FUNCTION = "wait_and_pass"
    CATEGORY = "DebugPadawan/Timing"
    
    def wait_and_pass(self, value, wait_time_ms):
        """
        Wait for the specified time and pass the input through
        
        Args:
            value: Any value to pass through
            wait_time_ms (int): Time to wait in milliseconds
            
        Returns:
            The same value (passthrough)
        """
        time.sleep(wait_time_ms / 1000.0)
        
        return (value,)


TIMING_NODE_CLASS_MAPPINGS = {
    "DebugPadawan_WaitNode": WaitNode,
}

TIMING_NODE_DISPLAY_NAME_MAPPINGS = {
    "DebugPadawan_WaitNode": "Wait Node",
}