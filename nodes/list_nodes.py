import torch
import random


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


class RandomListSelector:
    """
    Node for randomly selecting one or more items from a list
    Supports seeded randomness for reproducible selections
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "input_list": ("LIST",),
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
                "count": ("INT", {"default": 1, "min": 1}),
                "allow_duplicates": ("BOOLEAN", {"default": False}),
            }
        }
    
    RETURN_TYPES = ("LIST", "INT", "*")
    RETURN_NAMES = ("selected_items", "count", "first_item")
    
    FUNCTION = "select_random"
    CATEGORY = "DebugPadawan/List"
    
    def select_random(self, input_list, seed, count, allow_duplicates):
        if not input_list:
            raise ValueError("Input list is empty.")
        
        rng = random.Random(seed)
        list_len = len(input_list)
        
        if count > list_len and not allow_duplicates:
            count = list_len
        
        if allow_duplicates:
            selected = [rng.choice(input_list) for _ in range(count)]
        else:
            selected = rng.sample(input_list, min(count, list_len))
        
        first_item = selected[0] if selected else None
        return (selected, len(selected), first_item)


class ListShuffler:
    """
    Node for shuffling a list with a deterministic seed
    Useful for randomizing order while maintaining reproducibility
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "input_list": ("LIST",),
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
            }
        }
    
    RETURN_TYPES = ("LIST", "INT")
    RETURN_NAMES = ("shuffled_list", "count")
    
    FUNCTION = "shuffle_list"
    CATEGORY = "DebugPadawan/List"
    
    def shuffle_list(self, input_list, seed):
        if not input_list:
            return ([], 0)
        
        # Create a copy to avoid modifying the original
        shuffled = list(input_list)
        rng = random.Random(seed)
        rng.shuffle(shuffled)
        
        return (shuffled, len(shuffled))


class ListMerger:
    """
    Node for merging multiple lists together
    Supports concatenation and interleaving modes
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "list_a": ("LIST",),
                "list_b": ("LIST",),
                "mode": (["concatenate", "interleave"],),
            }
        }
    
    RETURN_TYPES = ("LIST", "INT")
    RETURN_NAMES = ("merged_list", "count")
    
    FUNCTION = "merge_lists"
    CATEGORY = "DebugPadawan/List"
    
    def merge_lists(self, list_a, list_b, mode):
        if mode == "concatenate":
            result = list_a + list_b
        else:  # interleave
            result = []
            max_len = max(len(list_a), len(list_b))
            for i in range(max_len):
                if i < len(list_a):
                    result.append(list_a[i])
                if i < len(list_b):
                    result.append(list_b[i])
        
        return (result, len(result))


class ListDeduplicator:
    """
    Node for removing duplicate items from a list
    Preserves original order
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "input_list": ("LIST",),
            }
        }
    
    RETURN_TYPES = ("LIST", "INT", "INT")
    RETURN_NAMES = ("deduplicated_list", "count", "removed_count")
    
    FUNCTION = "deduplicate"
    CATEGORY = "DebugPadawan/List"
    
    def deduplicate(self, input_list):
        seen = []
        result = []
        for item in input_list:
            # Convert to string for comparison (handles non-hashable types)
            item_key = str(item)
            if item_key not in seen:
                seen.append(item_key)
                result.append(item)
        
        removed = len(input_list) - len(result)
        return (result, len(result), removed)


NODE_CLASS_MAPPINGS = {
    "DebugPadawan_GetListItem": GetListItem,
    "DebugPadawan_ListSlicer": ListSlicer,
    "DebugPadawan_ListInfo": ListInfo,
    "DebugPadawan_RandomListSelector": RandomListSelector,
    "DebugPadawan_ListShuffler": ListShuffler,
    "DebugPadawan_ListMerger": ListMerger,
    "DebugPadawan_ListDeduplicator": ListDeduplicator,
    # Alias for backward compatibility
    "DP_GetListItem": GetListItem,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "DebugPadawan_GetListItem": "Get List Item",
    "DebugPadawan_ListSlicer": "List Slicer",
    "DebugPadawan_ListInfo": "List Info",
    "DebugPadawan_RandomListSelector": "Random List Selector",
    "DebugPadawan_ListShuffler": "List Shuffler",
    "DebugPadawan_ListMerger": "List Merger",
    "DebugPadawan_ListDeduplicator": "List Deduplicator",
    "DP_GetListItem": "Get List Item (Legacy)",
}
