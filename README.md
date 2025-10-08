#!/bin/bash

# Script: template_processor.sh
# Usage: ./template_processor.sh input_template.txt output_file.txt

set -e  # Exit on any error

if [ $# -ne 2 ]; then
    echo "Usage: $0 <input_template> <output_file>"
    echo "Example: $0 config.txt.template config.txt"
    exit 1
fi

INPUT_FILE="$1"
OUTPUT_FILE="$2"

# Check if input file exists
if [ ! -f "$INPUT_FILE" ]; then
    echo "Error: Input file '$INPUT_FILE' not found!"
    exit 1
fi

# Create a temporary file for processing
TEMP_FILE=$(mktemp)

# Copy template to temp file
cp "$INPUT_FILE" "$TEMP_FILE"

echo "Processing template: $INPUT_FILE"
echo "Parameters found in template:"

# Extract all parameter placeholders (format: {{PARAM_NAME}})
grep -o '{{[^}]*}}' "$INPUT_FILE" | sort | uniq | while read -r param; do
    param_name=$(echo "$param" | sed 's/{{//' | sed 's/}}//')
    echo "  - $param_name"
    
    # Ask user for value
    read -p "Enter value for $param_name: " value
    
    # Replace the parameter in the temp file
    sed -i "s|${param}|${value}|g" "$TEMP_FILE"
done

# Move temp file to output
mv "$TEMP_FILE" "$OUTPUT_FILE"

echo "Template processed successfully!"
echo "Output file: $OUTPUT_FILE"



---


application/vnd.openxmlformats-officedocument.wordprocessingml.document
application/msword





7ddd7a0055bd9b3ae62d8aac1f5433ddc47946ac696adb7f9947cda7ad2ef2bc
88aac2fb61e437428b08ef509bdf523125bb5370889702750a20c3841fc90d6c


27d2226c797815b2620d150bb748d0146cb28223bb6a6c38ec968cd3087d6d57
8802953dba15955b64510e20ffd4de5b


7283516ce0e2e7b13b24c89238c27d96



---
fcb708892578b085da1f0291b074a0d475b5a7f4382472dc16a95c6d13939481
52553cde86807cc19d0632c7bd30cc47e5c691478dead1a8266135144b5d7f12


---

9b5ad71b2ce5302211f9c61530b329a4922fc6a4


961beb059958092d7f6820e77b3bf9fe1bf6c04d8350a643bd867dc9921372d5

03e85559b909b3b5d749140de5ffd3688d25b5ea70f3bfada304d43897528910
