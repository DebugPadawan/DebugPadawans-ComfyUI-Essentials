<div align="center">

# 🎯 DebugPadawan's ComfyUI Essentials

*Essential custom nodes for ComfyUI workflows*

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![ComfyUI](https://img.shields.io/badge/ComfyUI-Compatible-green.svg)](https://github.com/comfyanonymous/ComfyUI)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/DebugPadawan/DebugPadawans-ComfyUI-Essentials.svg)](https://github.com/DebugPadawan/DebugPadawans-ComfyUI-Essentials/stargazers)

</div>

---

## ✨ Features

<table>
<tr>
<td><b>🔤 Text Processing</b></td>
<td>Split, join, and manipulate text strings with precision</td>
</tr>
<tr>
<td><b>📦 Data Conversion</b></td>
<td>Convert between text and JSON formats easily</td>
</tr>
<tr>
<td><b>🐛 Debug Tools</b></td>
<td>Print and inspect values during workflow execution</td>
</tr>
<tr>
<td><b>⏱️ Timing Control</b></td>
<td>Add delays and timing control to your workflows</td>
</tr>
<tr>
<td><b>🔀 Logic & Math</b></td>
<td>Boolean logic gates and mathematical operations</td>
</tr>
<tr>
<td><b>🔧 Utilities</b></td>
<td>Essential helpers for workflow optimization and list management</td>
</tr>
</table>

---

## 🚀 Installation

```bash
# Navigate to your ComfyUI custom nodes directory
cd ComfyUI/custom_nodes

# Clone the repository
git clone https://github.com/DebugPadawan/DebugPadawans-ComfyUI-Essentials.git

# Restart ComfyUI
```

---

## 📦 Available Nodes

### 🔤 Text Processing

<details>
<summary><b>📝 Text Splitter</b> - Split text strings by delimiter</summary>

**Category:** `DebugPadawan/Text`

Splits a text string at a specified delimiter and returns a list of strings.

**📥 Inputs:**
- `text` *(String)*: The text to split (supports multiline input)
- `delimiter` *(String)*: The character(s) to split by (default: `","`)
- `strip_whitespace` *(Boolean, optional)*: Remove leading/trailing whitespace (default: `True`)
- `remove_empty` *(Boolean, optional)*: Remove empty strings from result (default: `True`)

**📤 Outputs:**
- `text_list` *(List)*: The split list of strings
- `count` *(Integer)*: Number of elements in the list

**💡 Example:**
```
Input: "apple, banana, orange"
Delimiter: ","
Output: ["apple", "banana", "orange"] and 3
```

Process CSV-like data, split tag lists, separate coordinates, create filename lists, parse prompt components.

</details>

<details>
<summary><b>🔗 Text Joiner</b> - Combine strings with custom delimiters</summary>

**Category:** `DebugPadawan/Text`

Combines a list of strings into a single text string with a customizable delimiter.

**📥 Inputs:**
- `text_list` *(List)*: List of strings to join
- `delimiter` *(String)*: Character(s) to join with (default: `", "`)
- `prefix` *(String, optional)*: Text to add at the beginning
- `suffix` *(String, optional)*: Text to add at the end

**📤 Outputs:**
- `joined_text` *(String)*: The combined text string

**💡 Example:**
```
Input: ["red", "green", "blue"]
Delimiter: " | "
Prefix: "Colors: "
Suffix: " - end"
Output: "Colors: red | green | blue - end"
```

Combine prompt parts, convert lists to readable text, create metadata tags, build filenames, format output strings.

</details>

<details>
<summary><b>🔄 Text Replace</b> - Replace specific text in a string</summary>

**Category:** `DebugPadawan/Text`

Replaces all occurrences of a specific substring within a text string.

**📥 Inputs:**
- `text` *(String)*: The text to process
- `find` *(String)*: The substring to search for
- `replace` *(String)*: The string to replace it with

**📤 Outputs:**
- `text` *(String)*: The modified text string

**💡 Example:**
```
Input: "A beautiful sunset over the ocean"
Find: "sunset"
Replace: "sunrise"
Output: "A beautiful sunrise over the ocean"
```

Useful for dynamically adjusting prompts, modifying paths, and cleaning up generated text.

</details>

<details>
<summary><b>🔍 Text Regex (Search & Replace)</b> - Pattern-based text manipulation</summary>

**Category:** `DebugPadawan/Text`

Searches for patterns using Regular Expressions and optionally replaces them.

**📥 Inputs:**
- `text` *(String)*: The text to process
- `pattern` *(String)*: The regex pattern to search for
- `replace` *(String)*: The string to replace matches with

**📤 Outputs:**
- `text` *(String)*: The modified text string
- `matches` *(List)*: All strings that matched the pattern
- `found` *(Boolean)*: True if at least one match was found

Extract numbers, redact sensitive info, complex pattern replacement.

</details>

<details>
<summary><b>💬 String Formatter</b> - Create custom strings with placeholders</summary>

**Category:** `DebugPadawan/Text`

Formats a string using f-string-like syntax with up to 5 input strings.

**📥 Inputs:**
- `format_string` *(String)*: The template string with placeholders (e.g., "Hello {input1}, your number is {input2}").
- `input1` - `input5` *(String, optional)*: Up to five input strings to replace placeholders in the `format_string`.

**📤 Outputs:**
- `formatted_string` *(String)*: The resulting formatted string.

**💡 Example:**
```
Format String: "The result of {input1} plus {input2} is {input3}"
Input1: "2"
Input2: "3"
Input3: "5"
Output: "The result of 2 plus 3 is 5"
```

Useful for constructing dynamic prompts, filenames, messages, or URLs from multiple pieces of data.

</details>

---

### 📦 Data Conversion

<details>
<summary><b>🗃️ TextToJSON</b> - Convert text to JSON</summary>

**Category:** `DebugPadawan/JSON`

Converts a valid JSON string into a JSON object, enabling further data processing or integration with other nodes.

**📥 Inputs:**
- `text` *(String)*: The text to parse as JSON

**📤 Outputs:**
- `json` *(JSON/Object)*: The parsed JSON object

**💡 Example:**
```
Input: '{"name": "Alice", "age": 30}'
Output: { "name": "Alice", "age": 30 }
```

Use this node to quickly transform JSON-formatted text into a usable data structure for your ComfyUI workflows.

</details>

<details>
<summary><b>💬 JSONToText</b> - Convert JSON to text</summary>

**Category:** `DebugPadawan/JSON`

Converts a JSON object back into a formatted JSON string.

**📥 Inputs:**
- `json_data` *(JSON/Object)*: The JSON object to convert.
- `indent` *(Integer, optional)*: Number of spaces for indentation (0 for no indentation, default: `0`).

**📤 Outputs:**
- `text` *(String)*: The JSON object as a string.

**💡 Example:**
```
Input: { "name": "Alice", "age": 30 }
Indent: 2
Output:
{
  "name": "Alice",
  "age": 30
}
```

Use this node to convert JSON data into a readable string for display, logging, or integration with nodes that expect string input.

</details>

---

### 🐛 Debug Tools

<details>
<summary><b>🖨️ Debug Print</b> - Console output for debugging</summary>

**Category:** `DebugPadawan/Debug`

Prints values to the console without interrupting the workflow. Perfect for debugging and monitoring data values during execution.

**📥 Inputs:**
- `value` *(Any)*: Any value to print to console (supports all data types)
- `label` *(String, optional)*: Label for the debug output (default: `"Debug"`)

**📤 Outputs:**
- `passthrough` *(Any)*: The same value passed through unchanged

**💻 Console Output:**
```
[MyLabel] list: ['Element1', 'Element2', 'Element3']
[Debug] str: Hello World
[Checkpoint] int: 42
[Data Flow] dict: {'key': 'value', 'count': 5}
[Boolean Test] bool: True
[Float Value] float: 3.14159
```

Monitor values during execution, debug complex workflows, verify data types, set checkpoints, troubleshoot unexpected results.

</details>

---

### ⏱️ Timing Control

<details>
<summary><b>⏳ Wait</b> - Add delays to workflow execution</summary>

**Category:** `DebugPadawan/Timing`

Pauses workflow execution for a specified duration. Useful for rate limiting, timing control, or debugging workflow sequences.

**📥 Inputs:**
- `value` *(Any)*: Any value to pass through after the delay
- `delay_seconds` *(Float)*: Duration to wait in seconds (default: `1.0`)
- `label` *(String, optional)*: Label for console output (default: `"Wait"`)

**📤 Outputs:**
- `passthrough` *(Any)*: The same value passed through after delay

**💻 Console Output:**
```
[Wait] Waiting for 2.5 seconds...
[Wait] Wait completed.
[Custom Timer] Waiting for 5.0 seconds...
[Custom Timer] Wait completed.
```

Rate limit API calls, debug timing issues, control workflow execution speed, add pauses between operations, synchronize parallel processes.

**⚠️ Note:** Use with caution in production workflows as it will genuinely pause execution.

</details>

---

### 🖼️ Image Utilities

<details>
<summary><b>📐 Image Info</b> - Extract image tensor dimensions</summary>

**Category:** `DebugPadawan/Image`

Extracts the width, height, and batch size from a ComfyUI Image tensor.

**📥 Inputs:**
- `image` *(Image)*: The image tensor to analyze

**📤 Outputs:**
- `width` *(Integer)*: Image width in pixels
- `height` *(Integer)*: Image height in pixels
- `batch_size` *(Integer)*: Number of images in the batch

Useful for dynamic resizing, conditional logic based on aspect ratio, or passing dimensions to other nodes.

</details>

---

### 🧮 Math & Random

<details>
<summary><b>➕ Int/Float Math Operation</b> - Perform basic arithmetic</summary>

**Category:** `DebugPadawan/Math`

Performs simple math operations (add, subtract, multiply, divide, modulo, power) on integers or floats.

**📥 Inputs:**
- `a`, `b` *(Int/Float)*: The values to calculate
- `operation` *(List)*: The type of mathematical operation

**📤 Outputs:**
- `result` *(Int/Float)*: The calculated value (returns both Int and Float variations)

</details>

<details>
<summary><b>🎲 Random Generator</b> - Seed-based random values</summary>

**Category:** `DebugPadawan/Math`

Generates a random float or integer between a min and max value, driven by a specific seed for reproducibility.

**📥 Inputs:**
- `seed` *(Integer)*: Seed for the random generator
- `min_val`, `max_val` *(Float/Integer)*: The range bounds
- `mode` *(List)*: Whether to generate a float or an int

**📤 Outputs:**
- `val` *(Float/Integer)*: The random value (returns both Int and Float formats)

</details>

---

### 📝 List Manipulation

<details>
<summary><b>📝 Get List Item</b> - Retrieve an item from a list by index</summary>

**Category:** `DebugPadawan/List`

Retrieves a specific item from a list based on its index. Supports converting some iterable types to lists.

**📥 Inputs:**
- `input_list` *(Any, List force input)*: The input list or iterable.
- `index` *(Integer)*: The zero-based index of the item to retrieve.

**📤 Outputs:**
- `item` *(Any)*: The item at the specified index.

**💡 Example:**
```
Input List: ["apple", "banana", "orange"]
Index: 1
Output: "banana"
```

Useful for extracting specific elements from lists, such as getting a particular image from a batch, a specific tag from a list, or individual components from a parsed string list.

</details>

<details>
<summary><b>✂️ List Slicer</b> - Extract a range of items from a list</summary>

**Category:** `DebugPadawan/List`

Extracts a sub-list from a larger list using start and end indices.

**📥 Inputs:**
- `input_list` *(List)*: The input list.
- `start` *(Integer)*: Starting index (inclusive).
- `end` *(Integer)*: Ending index (exclusive, use 0 for "to the end").

**📤 Outputs:**
- `list_slice` *(List)*: The sub-list.
- `count` *(Integer)*: Number of elements in the slice.

Get the first N images of a batch, skip the first item, or take a specific range of values.

</details>

---

### 🔧 Utility Nodes

<details>
<summary><b>📊 List Info</b> - Analyze list properties</summary>

**Category:** `DebugPadawan/Utilities`

Analyzes a list and returns useful information about it.

**📥 Inputs:**
- `input_list` *(List)*: The list to analyze

**📤 Outputs:**
- `count` *(Integer)*: Number of elements
- `first_item` *(String)*: First element (as string)
- `last_item` *(String)*: Last element (as string)

Validate list processing results, get quick statistics, check if lists are empty, extract boundary values.

</details>

<details>
<summary><b>🔀 Conditional String</b> - Boolean-based string selection</summary>

**Category:** `DebugPadawan/Logic`

Returns one of two strings based on a boolean condition.

**📥 Inputs:**
- `condition` *(Boolean)*: The condition to evaluate
- `true_string` *(String)*: String to return if True (default: `"True"`)
- `false_string` *(String)*: String to return if False (default: `"False"`)

**📤 Outputs:**
- `result` *(String)*: The selected string

Conditional prompt modification, dynamic filename generation, workflow branching, status message generation.

</details>

<details>
<summary><b>🔌 Logic Gate</b> - Boolean operations</summary>

**Category:** `DebugPadawan/Logic`

Performs AND, OR, NOT, or XOR operations on boolean inputs.

**📥 Inputs:**
- `a`, `b` *(Boolean)*: Boolean values.
- `operation` *(List)*: AND, OR, NOT (A), XOR.

**📤 Outputs:**
- `result` *(Boolean)*: The resulting boolean value.

Complex workflow branching and conditional logic.

</details>

---

## 🎨 Quick Start Examples

### Basic Text Processing
```
"apple,banana,orange" → Text Splitter → ["apple", "banana", "orange"]
                                    ↓
["apple", "banana", "orange"] → Text Joiner → "apple | banana | orange"
```

### Text to JSON Conversion
```
'{"foo": "bar"}' → TextToJSON → { "foo": "bar" }
```

### Debug Workflow
```
Input Data → Debug Print ("Input") → Processing Node → Debug Print ("Output") → Result
```

### Timed Processing
```
Data → Wait (2.0s) → Processing → Wait (1.0s) → Output
```

---

## 📋 Node Categories

| Category | Nodes | Purpose |
|----------|-------|---------|
| **DebugPadawan/Text** | Text Splitter, Text Joiner, Text Replace, Text Regex, String Formatter | Text manipulation and processing |
| **DebugPadawan/JSON** | TextToJSON, JSONToText | Text to JSON conversion |
| **DebugPadawan/Debug** | Debug Print | Debugging and monitoring |
| **DebugPadawan/Timing** | Wait | Timing control and delays |
| **DebugPadawan/Utilities** | List Info | Data analysis helpers |
| **DebugPadawan/Logic** | Conditional String, Logic Gate | Conditional operations |
| **DebugPadawan/Image** | Image Info | Image tensor analysis |
| **DebugPadawan/Math** | Int Math Operation, Float Math Operation, Random Generator | Basic arithmetic and random number generation |
| **DebugPadawan/List** | Get List Item, List Slicer | List manipulation |

---

## 🤝 Contributing

We welcome contributions! Feel free to:
- 🐛 Report bugs
- 💡 Suggest new features  
- 🔧 Submit pull requests
- 📖 Improve documentation

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

<div align="center">

**Made with ❤️ by [DebugPadawan](https://github.com/DebugPadawan)**

</div>
