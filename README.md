#!/bin/bash

# Quick template processor for two files
# Usage: ./quick_template.sh template1.txt template2.txt

template_file_env="$1"
template_file_librechat="$2"

if [ -z "$template_file_env" ] || [ ! -f "$template_file_env" ] || [ -z "$template_file_librechat" ] || [ ! -f "$template_file_librechat" ]; then
    echo "Usage: $0 <template_file_env> <template_file_librechat>"
    echo "Both template files must exist"
    exit 1
fi

process_template() {
    local template_file="$1"
    local content=$(cat "$template_file")
    
    echo "=== Processing: $template_file ==="
    
    # Find all parameters and replace them
    while [[ $content =~ ({{([^}]*)}}) ]]; do
        param="${BASH_REMATCH[1]}"
        param_name="${BASH_REMATCH[2]}"
        read -p "Enter URL in format <gpt2giga IP>: <gpt2giga port> for $param_name: " value
        content=${content//$param/$value}
    done
    
    echo "$content" > "$template_file"
    echo "=== Finished: $template_file ==="
    echo
}

# Process both templates
process_template "$template_file_env"
process_template "$template_file_librechat"


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
