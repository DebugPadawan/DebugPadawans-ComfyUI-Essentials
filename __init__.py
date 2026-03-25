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
from .nodes.color_palette import NODE_CLASS_MAPPINGS as COLOR_PALETTE_NODES
from .nodes.color_palette import NODE_DISPLAY_NAME_MAPPINGS as COLOR_PALETTE_DISPLAY_NAMES
from .nodes.math_nodes import NODE_CLASS_MAPPINGS as MATH_NODES
from .nodes.math_nodes import NODE_DISPLAY_NAME_MAPPINGS as MATH_DISPLAY_NAMES
from .nodes.list_nodes import NODE_CLASS_MAPPINGS as LIST_NODES
from .nodes.list_nodes import NODE_DISPLAY_NAME_MAPPINGS as LIST_DISPLAY_NAMES

from .nodes.json_to_text import NODE_CLASS_MAPPINGS as JSON_TO_TEXT_NODES
from .nodes.json_to_text import NODE_DISPLAY_NAME_MAPPINGS as JSON_TO_TEXT_DISPLAY_NAMES
from .nodes.string_formatter import NODE_CLASS_MAPPINGS as STRING_FORMATTER_NODES
from .nodes.string_formatter import NODE_DISPLAY_NAME_MAPPINGS as STRING_FORMATTER_DISPLAY_NAMES
from .nodes.text_compare import NODE_CLASS_MAPPINGS as TEXT_COMPARE_NODES
from .nodes.text_compare import NODE_DISPLAY_NAME_MAPPINGS as TEXT_COMPARE_DISPLAY_NAMES
from .nodes.type_conversion import NODE_CLASS_MAPPINGS as TYPE_CONVERSION_NODES
from .nodes.type_conversion import NODE_DISPLAY_NAME_MAPPINGS as TYPE_CONVERSION_DISPLAY_NAMES
from .nodes.number_utils import NODE_CLASS_MAPPINGS as NUMBER_UTILS_NODES
from .nodes.number_utils import NODE_DISPLAY_NAME_MAPPINGS as NUMBER_UTILS_DISPLAY_NAMES

# Combine all node mappings
NODE_CLASS_MAPPINGS = {
    **TEXT_NODES,
    **UTILITY_NODES,
    **TIMING_NODES,
    **JSON_NODES,
    **IMAGE_NODES,
    **COLOR_PALETTE_NODES,
    **MATH_NODES,
    **LIST_NODES,
    **JSON_TO_TEXT_NODES,
    **STRING_FORMATTER_NODES,
    **TEXT_COMPARE_NODES,
    **TYPE_CONVERSION_NODES,
    **NUMBER_UTILS_NODES,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    **TEXT_DISPLAY_NAMES,
    **UTILITY_DISPLAY_NAMES,
    **TIMING_DISPLAY_NAMES,
    **JSON_DISPLAY_NAMES,
    **IMAGE_DISPLAY_NAMES,
    **COLOR_PALETTE_DISPLAY_NAMES,
    **MATH_DISPLAY_NAMES,
    **LIST_DISPLAY_NAMES,
    **JSON_TO_TEXT_DISPLAY_NAMES,
    **STRING_FORMATTER_DISPLAY_NAMES,
    **TEXT_COMPARE_DISPLAY_NAMES,
    **TYPE_CONVERSION_DISPLAY_NAMES,
    **NUMBER_UTILS_DISPLAY_NAMES,
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']

# Version info
__version__ = "1.4.0"
__author__ = "DebugPadawan"