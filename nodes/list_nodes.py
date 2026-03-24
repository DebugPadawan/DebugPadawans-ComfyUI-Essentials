import torch

class GetListItem:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "input_list": ("*", {"forceInput": True}),
                "index": ("INT", {"default": 0, "min": 0, "max": 0xFFFFFFFFFFFFFFFF}),
            }
        }

    RETURN_TYPES = ("*",)
    RETURN_NAMES = ("item",)
    FUNCTION = "get_item"
    CATEGORY = "DebugPadawan/List"

    def get_item(self, input_list, index):
        if not isinstance(input_list, list):
            # Attempt to convert to list if it's a ComfyUI tensor batch or similar
            if isinstance(input_list, torch.Tensor):
                input_list = input_list.tolist()
            elif hasattr(input_list, '__iter__') and not isinstance(input_list, str):
                input_list = list(input_list)
            else:
                # If it's a single item, wrap it in a list to allow indexing
                input_list = [input_list]

        if not input_list:
            raise ValueError("Input list is empty.")
        if index < 0 or index >= len(input_list):
            raise IndexError(f"Index {index} out of bounds for list of length {len(input_list)}.")

        return (input_list[index],)


class ListSlicer:
    """
    Node for getting a slice of a list
    """
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "input_list": ("LIST",),
                "start": ("INT", {"default": 0, "min": 0}),
                "end": ("INT", {"default": 0, "min": 0}),
            }
        }
    
    RETURN_TYPES = ("LIST", "INT")
    RETURN_NAMES = ("list_slice", "count")
    FUNCTION = "slice_list"
    CATEGORY = "DebugPadawan/List"

    def slice_list(self, input_list, start, end):
        if end == 0:
            res = input_list[start:]
        else:
            res = input_list[start:end]
        return (res, len(res))


class ListInfo:
    """
    Node for getting information about a list
    """
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "input_list": ("LIST",),
            }
        }
    
    RETURN_TYPES = ("INT", "STRING", "STRING")
    RETURN_NAMES = ("count", "first_item", "last_item")
    
    FUNCTION = "get_list_info"
    CATEGORY = "DebugPadawan/Utilities"
    
    def get_list_info(self, input_list):
        count = len(input_list)
        first_item = str(input_list[0]) if input_list else ""
        last_item = str(input_list[-1]) if input_list else ""
        
        return (count, first_item, last_item)


NODE_CLASS_MAPPINGS = {
    "DebugPadawan_GetListItem": GetListItem,
    "DebugPadawan_ListSlicer": ListSlicer,
    "DebugPadawan_ListInfo": ListInfo,
    # Alias for backward compatibility
    "DP_GetListItem": GetListItem,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "DebugPadawan_GetListItem": "Get List Item",
    "DebugPadawan_ListSlicer": "List Slicer",
    "DebugPadawan_ListInfo": "List Info",
    "DP_GetListItem": "Get List Item (Legacy)",
}
