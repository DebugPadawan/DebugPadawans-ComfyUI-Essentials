"""
DebugPadawan's ComfyUI Essentials
A collection of essential custom nodes for ComfyUI
"""

from .nodes.text_processing import NODE_CLASS_MAPPINGS as TEXT_NODES
from .nodes.text_processing import NODE_DISPLAY_NAME_MAPPINGS as TEXT_DISPLAY_NAMES
from .nodes.utilities import UTILITY_NODE_CLASS_MAPPINGS as UTILITY_NODES
from .nodes.utilities import UTILITY_NODE_DISPLAY_NAME_MAPPINGS as UTILITY_DISPLAY_NAMES

# Combine all node mappings
NODE_CLASS_MAPPINGS = {}
NODE_CLASS_MAPPINGS.update(TEXT_NODES)
NODE_CLASS_MAPPINGS.update(UTILITY_NODES)

NODE_DISPLAY_NAME_MAPPINGS = {}
NODE_DISPLAY_NAME_MAPPINGS.update(TEXT_DISPLAY_NAMES)
NODE_DISPLAY_NAME_MAPPINGS.update(UTILITY_DISPLAY_NAMES)

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']

# Version info
__version__ = "1.0.0"
__author__ = "DebugPadawan"