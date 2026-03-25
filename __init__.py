import os
import importlib
import glob

# Node registration dictionaries
NODE_CLASS_MAPPINGS = {}
NODE_DISPLAY_NAME_MAPPINGS = {}

# Automatically import all .py files from the nodes directory
nodes_dir = os.path.join(os.path.dirname(__file__), "nodes")
node_files = glob.glob(os.path.join(nodes_dir, "*.py"))

for file_path in node_files:
    file_name = os.path.basename(file_path)
    if file_name == "__init__.py":
        continue
    
    module_name = f".nodes.{file_name[:-3]}"
    try:
        # Import the module
        module = importlib.import_module(module_name, package=__package__)
        
        # Load mappings if they exist
        if hasattr(module, "NODE_CLASS_MAPPINGS"):
              NODE_CLASS_MAPPINGS.update(module.NODE_CLASS_MAPPINGS)
        
        # UTILITY_NODE_CLASS_MAPPINGS for backward compatibility
        if hasattr(module, "UTILITY_NODE_CLASS_MAPPINGS"):
            NODE_CLASS_MAPPINGS.update(module.UTILITY_NODE_CLASS_MAPPINGS)

        if hasattr(module, "NODE_DISPLAY_NAME_MAPPINGS"):
            NODE_DISPLAY_NAME_MAPPINGS.update(module.NODE_DISPLAY_NAME_MAPPINGS)
        
        # UTILITY_NODE_DISPLAY_NAME_MAPPINGS for backward compatibility
        if hasattr(module, "UTILITY_NODE_DISPLAY_NAME_MAPPINGS"):
            NODE_DISPLAY_NAME_MAPPINGS.update(module.UTILITY_NODE_DISPLAY_NAME_MAPPINGS)
            
    except Exception as e:
        print(f"[DebugPadawan Essentials] Failed to load module {module_name}: {e}")

# Version and Metadata
__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
__version__ = "1.5.1"
__author__ = "DebugPadawan"