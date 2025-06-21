# DebugPadawan's ComfyUI Essentials

A collection of essential custom nodes for ComfyUI that provides useful utilities for text processing, data manipulation, and workflow enhancement.

## Features

- **Text Processing Nodes**: Split, join, and manipulate text strings
- **Data Utilities**: Convert between different data types
- **Workflow Helpers**: Common operations to streamline your ComfyUI workflows
- **Debug Tools**: Print and inspect values during workflow execution

## Installation

1. Clone this repository into your ComfyUI `custom_nodes` directory:
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/DebugPadawan/DebugPadawans-ComfyUI-Essentials.git
```

2. Restart ComfyUI

## Available Nodes

### Text Processing

#### Text Splitter
**Category**: DebugPadawan/Text

Splits a text string at a specified delimiter and returns a list of strings.

**Inputs:**
- `text` (String): The text to split (supports multiline input)
- `delimiter` (String): The character(s) to split by (default: ",")
- `strip_whitespace` (Boolean, optional): Remove leading/trailing whitespace from each element (default: True)
- `remove_empty` (Boolean, optional): Remove empty strings from the result (default: True)

**Outputs:**
- `text_list` (List): The split list of strings
- `count` (Integer): Number of elements in the list

**Example:**
- Input: `"apple, banana, orange"`
- Delimiter: `","`
- Output: `["apple", "banana", "orange"]` and `3`

Process CSV-like data, split tag lists, separate coordinates or parameters, create filename lists, and parse prompt components.

---

#### Text Joiner
**Category**: DebugPadawan/Text

Combines a list of strings into a single text string with a customizable delimiter.

**Inputs:**
- `text_list` (List): List of strings to join
- `delimiter` (String): Character(s) to join with (default: ", ")
- `prefix` (String, optional): Text to add at the beginning
- `suffix` (String, optional): Text to add at the end

**Outputs:**
- `joined_text` (String): The combined text string

**Example:**
- Input: `["red", "green", "blue"]`
- Delimiter: `" | "`
- Prefix: `"Colors: "`
- Suffix: `" - end"`
- Output: `"Colors: red | green | blue - end"`

Combine prompt parts, convert lists to readable text, create tags for metadata, build filenames from components, and format output strings.

---

### Debug Tools

#### Debug Print
**Category**: DebugPadawan/Debug

Prints values to the console without interrupting the workflow. Perfect for debugging and monitoring data values during execution. Accepts any input type including strings, integers, floats, booleans, lists, dictionaries, and complex objects.

**Inputs:**
- `value` (*): Any value to print to console (supports all data types)
- `label` (String, optional): Label for the debug output (default: "Debug")

**Outputs:**
- `passthrough` (*): The same value passed through unchanged

**Console Output:**
```
[MyLabel] list: ['Element1', 'Element2', 'Element3']
[Debug] str: Hello World
[Checkpoint] int: 42
[Data Flow] dict: {'key': 'value', 'count': 5}
[Boolean Test] bool: True
[Float Value] float: 3.14159
```

Monitor values during workflow execution, debug complex workflows, verify data types and contents, set workflow checkpoints, and troubleshoot unexpected results. Use descriptive labels and remember that the node doesn't interrupt data flow.

---

### Utility Nodes

#### List Info
**Category**: DebugPadawan/Utilities

Analyzes a list and returns useful information about it.

**Inputs:**
- `input_list` (List): The list to analyze

**Outputs:**
- `count` (Integer): Number of elements
- `first_item` (String): First element (as string)
- `last_item` (String): Last element (as string)

Validate list processing results, get quick list statistics, check if lists are empty, and extract boundary values.

#### Conditional String
**Category**: DebugPadawan/Logic

Returns one of two strings based on a boolean condition.

**Inputs:**
- `condition` (Boolean): The condition to evaluate
- `true_string` (String): String to return if True (default: "True")
- `false_string` (String): String to return if False (default: "False")

**Outputs:**
- `result` (String): The selected string

Conditional prompt modification, dynamic filename generation, workflow branching based on conditions, and status message generation.

