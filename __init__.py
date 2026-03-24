"""
DebugPadawan's ComfyUI Essentials
A collection of essential custom nodes for ComfyUI
"""

from .nodes.text_processing import NODE_CLASS_MAPPINGS as TEXT_NODES
from .nodes.text_processing import NODE_DISPLAY_NAME_MAPPINGS as TEXT_DISPLAY_NAMES
from .nodes.utilities import UTILITY_NODE_CLASS_MAPPINGS as UTILITY_NODES
from .nodes.utilities import UTILITY_NODE_DISPLAY_NAME_MAPPINGS as UTILITY_DISPLAY_NAMES
from .nodes.timing import TIMING_NODE_CLASS_MAPPINGS as TIMING_NODES
from .nodes.timing import TIMING_NODE_DISPLAY_NAME_MAPPINGS as TIMING_DISPLAY_NAMES
from .nodes.json import NODE_CLASS_MAPPINGS as JSON_NODES
from .nodes.json import NODE_DISPLAY_NAME_MAPPINGS as JSON_DISPLAY_NAMES
from .nodes.image import NODE_CLASS_MAPPINGS as IMAGE_NODES
from .nodes.image import NODE_DISPLAY_NAME_MAPPINGS as IMAGE_DISPLAY_NAMES
from .nodes.math_nodes import NODE_CLASS_MAPPINGS as MATH_NODES
from .nodes.math_nodes import NODE_DISPLAY_NAME_MAPPINGS as MATH_DISPLAY_NAMES

# Combine all node mappings
NODE_CLASS_MAPPINGS = {
    **TEXT_NODES,
    **UTILITY_NODES,
    **TIMING_NODES,
    **JSON_NODES,
    **IMAGE_NODES,
    **MATH_NODES,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    **TEXT_DISPLAY_NAMES,
    **UTILITY_DISPLAY_NAMES,
    **TIMING_DISPLAY_NAMES,
    **JSON_DISPLAY_NAMES,
    **IMAGE_DISPLAY_NAMES,
    **MATH_DISPLAY_NAMES,
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']

# Version info
__version__ = "1.0.0"
__author__ = "DebugPadawan"