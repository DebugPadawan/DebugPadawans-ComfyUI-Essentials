import torch
import random
from typing import List, Any, Tuple, Union

class GetListItem:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "input_list": ("*", {"forceInput": True}),
                "index": ("INT", {"default": 0, "min": -1000000, "max": 1000000}),
            }
        }

    RETURN_TYPES = ("*",)
    RETURN_NAMES = ("item",)
    FUNCTION = "get_item"
    CATEGORY = "DebugPadawan/List"

    def get_item(self, input_list: Any, index: int) -> Tuple[Any]:
        if not isinstance(input_list, list):
            if isinstance(input_list, torch.Tensor):
                input_list = input_list.tolist()
            elif hasattr(input_list, '__iter__') and not isinstance(input_list, str):
                input_list = list(input_list)
            else:
                input_list = [input_list]

        if not input_list:
            return (None,)
            
        # Handle negative indexing
        try:
            return (input_list[index],)
        except IndexError:
            return (input_list[-1] if index >= 0 else input_list[0],)


class ListCreate:
    """
    Node for creating a list from up to 8 individual inputs.
    """
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {},
            "optional": {
                f"input_{i}": ("*", {"forceInput": True}) for i in range(1, 9)
            }
        }
    
    RETURN_TYPES = ("LIST", "INT")
    RETURN_NAMES = ("list", "count")
    FUNCTION = "create_list"
    CATEGORY = "DebugPadawan/List"
    
    def create_list(self, **kwargs) -> Tuple[List[Any], int]:
        result = [v for k, v in kwargs.items() if v is not None]
        return (result, len(result))


class ListFilter:
    """
    Node for filtering a list based on string matching or numeric bounds.
    """
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "input_list": ("LIST",),
                "filter_mode": (["contains", "starts_with", "ends_with", "regex", "equals"],),
                "filter_value": ("STRING", {"default": ""}),
            },
            "optional": {
                "exclude": ("BOOLEAN", {"default": False}),
            }
        }
        
    RETURN_TYPES = ("LIST", "INT")
    RETURN_NAMES = ("filtered_list", "count")
    FUNCTION = "filter_list"
    CATEGORY = "DebugPadawan/List"
    
    def filter_list(self, input_list: List[Any], filter_mode: str, filter_value: str, exclude: bool = False) -> Tuple[List[Any], int]:
        import re
        result = []
        for item in input_list:
            s_item = str(item)
            match = False
            
            if filter_mode == "contains": match = filter_value in s_item
            elif filter_mode == "starts_with": match = s_item.startswith(filter_value)
            elif filter_mode == "ends_with": match = s_item.endswith(filter_value)
            elif filter_mode == "equals": match = s_item == filter_value
            elif filter_mode == "regex":
                try:
                    match = bool(re.search(filter_value, s_item))
                except:
                    match = False
            
            if exclude: match = not match
            if match: result.append(item)
            
        return (result, len(result))


class ListSlicer:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "input_list": ("LIST",),
                "start": ("INT", {"default": 0, "min": 0}),
                "end": ("INT", {"default": 1, "min": 0}),
            }
        }
    
    RETURN_TYPES = ("LIST", "INT")
    RETURN_NAMES = ("list_slice", "count")
    FUNCTION = "slice_list"
    CATEGORY = "DebugPadawan/List"

    def slice_list(self, input_list: List, start: int, end: int) -> Tuple[List, int]:
        # If end is 0 or less than start, we treat as "to the end" or at least 1 item
        if end <= start:
            res = input_list[start:]
        else:
            res = input_list[start:end]
        return (res, len(res))


class ListInfo:
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
    CATEGORY = "DebugPadawan/List"
    
    def get_list_info(self, input_list: List) -> Tuple[int, str, str]:
        if not input_list:
            return (0, "", "")
        return (len(input_list), str(input_list[0]), str(input_list[-1]))


class RandomListSelector:
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
    
    def select_random(self, input_list: List, seed: int, count: int, allow_duplicates: bool) -> Tuple[List, int, Any]:
        if not input_list:
            return ([], 0, None)
        
        rng = random.Random(seed)
        list_len = len(input_list)
        
        if allow_duplicates:
            selected = [rng.choice(input_list) for _ in range(count)]
        else:
            selected = rng.sample(input_list, min(count, list_len))
        
        first_item = selected[0] if selected else None
        return (selected, len(selected), first_item)


class ListShuffler:
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
    
    def shuffle_list(self, input_list: List, seed: int) -> Tuple[List, int]:
        if not input_list:
            return ([], 0)
        shuffled = list(input_list)
        random.Random(seed).shuffle(shuffled)
        return (shuffled, len(shuffled))


class ListMerger:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "list_a": ("LIST",),
                "list_b": ("LIST",),
                "mode": (["concatenate", "interleave", "union"],),
            }
        }
    
    RETURN_TYPES = ("LIST", "INT")
    RETURN_NAMES = ("merged_list", "count")
    FUNCTION = "merge_lists"
    CATEGORY = "DebugPadawan/List"
    
    def merge_lists(self, list_a: List, list_b: List, mode: str) -> Tuple[List, int]:
        if mode == "concatenate":
            result = list_a + list_b
        elif mode == "interleave":
            result = []
            for i in range(max(len(list_a), len(list_b))):
                if i < len(list_a): result.append(list_a[i])
                if i < len(list_b): result.append(list_b[i])
        elif mode == "union":
            seen = set()
            result = []
            for item in list_a + list_b:
                s = str(item)
                if s not in seen:
                    seen.add(s)
                    result.append(item)
        
        return (result, len(result))


class ListDeduplicator:
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
    
    def deduplicate(self, input_list: List) -> Tuple[List, int, int]:
        seen = set()
        result = []
        for item in input_list:
            item_key = str(item)
            if item_key not in seen:
                seen.add(item_key)
                result.append(item)
        
        return (result, len(result), len(input_list) - len(result))


NODE_CLASS_MAPPINGS = {
    "DebugPadawan_GetListItem": GetListItem,
    "DebugPadawan_ListCreate": ListCreate,
    "DebugPadawan_ListFilter": ListFilter,
    "DebugPadawan_ListSlicer": ListSlicer,
    "DebugPadawan_ListInfo": ListInfo,
    "DebugPadawan_RandomListSelector": RandomListSelector,
    "DebugPadawan_ListShuffler": ListShuffler,
    "DebugPadawan_ListMerger": ListMerger,
    "DebugPadawan_ListDeduplicator": ListDeduplicator,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "DebugPadawan_GetListItem": "Get List Item",
    "DebugPadawan_ListCreate": "List Create (Multi-Input)",
    "DebugPadawan_ListFilter": "List Filter",
    "DebugPadawan_ListSlicer": "List Slicer",
    "DebugPadawan_ListInfo": "List Info",
    "DebugPadawan_RandomListSelector": "Random List Selector",
    "DebugPadawan_ListShuffler": "List Shuffler",
    "DebugPadawan_ListMerger": "List Merger",
    "DebugPadawan_ListDeduplicator": "List Deduplicator",
}
