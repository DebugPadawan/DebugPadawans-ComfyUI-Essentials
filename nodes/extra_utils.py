import os
import json
from typing import Any, Tuple

class AnyType(str):
    def __ne__(self, __value: object) -> bool:
        return False

generic_type = AnyType("*")

class NodeSearch:
    """
    Utility node to list or search available ComfyUI nodes (by class or name).
    Helpful for developers to find node internal names.
    """
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "search_query": ("STRING", {"default": ""}),
                "search_mode": (["class_name", "display_name", "category"],),
            }
        }
    
    RETURN_TYPES = ("LIST", "STRING")
    RETURN_NAMES = ("node_list", "count_summary")
    FUNCTION = "search_nodes"
    CATEGORY = "DebugPadawan/Utilities"
    
    def search_nodes(self, search_query: str, search_mode: str) -> Tuple[list, str]:
        # This requires access to ComfyUI's internal node mapping
        # NOTE: In actual execution, we'd need to import it.
        # This is a bit of a trick as it's usually in `nodes.NODE_CLASS_MAPPINGS`
        try:
             import nodes as comfy_nodes
             mappings = comfy_nodes.NODE_CLASS_MAPPINGS
             display_names = comfy_nodes.NODE_DISPLAY_NAME_MAPPINGS
        except ImportError:
             return ([], "Could not access ComfyUI node mappings")

        results = []
        query = search_query.lower()
        
        for k, v in mappings.items():
            disp = display_names.get(k, k)
            cat = getattr(v, "CATEGORY", "Unknown")
            
            match = False
            if not query:
                match = True
            elif search_mode == "class_name" and query in k.lower():
                match = True
            elif search_mode == "display_name" and query in disp.lower():
                match = True
            elif search_mode == "category" and query in cat.lower():
                match = True
                
            if match:
                results.append(f"{k} | {disp} | {cat}")
        
        results.sort()
        return (results, f"Found {len(results)} nodes matching '{search_query}'")


class TextFileLoader:
    """
    Loads text from a file.
    """
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "file_path": ("STRING", {"default": "example.txt"}),
            }
        }
    
    RETURN_TYPES = ("STRING", "LIST")
    RETURN_NAMES = ("content", "lines")
    FUNCTION = "load_file"
    CATEGORY = "DebugPadawan/Utilities"
    
    def load_file(self, file_path: str) -> Tuple[str, list]:
        if not os.path.exists(file_path):
            return (f"File not found: {file_path}", [])
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                lines = content.splitlines()
                return (content, lines)
        except Exception as e:
            return (f"Error loading file: {str(e)}", [])


NODE_CLASS_MAPPINGS = {
    "DebugPadawan_NodeSearch": NodeSearch,
    "DebugPadawan_TextFileLoader": TextFileLoader,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "DebugPadawan_NodeSearch": "Node Search Utility",
    "DebugPadawan_TextFileLoader": "Load Text File",
}
