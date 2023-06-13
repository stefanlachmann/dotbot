#!/bin/bash

# Exit on error
set -e

# Read the location from the environment variable    
# shellcheck disable=SC2153


location=$(eval echo "$LOCATION" || eval echo "$DOTBOT_LOCATION")

# Verify if the location exists
while [[ ! -d "$location" ]]; do
    echo "location: $location does not exist"
    read -rp "do you wish to create it (y/n)?" choice
    if [[ $choice == "y" ]]; then
        read -rp "enter location" location
        mkdir -p "$location"
    else
    read -rp "Please enter a valid location: " location
    fi
done

# Read the dotbot entries from the dotbots_list.txt file
dotbot_list="dotbots_list.txt"
while IFS= read -r entry; do
   fullpath="$entry"

    # Check if the entry exists
    if [[ -e "$fullpath" ]]; then
        echo "Copying '$entry' to '$location'"
        cp -r "$fullpath" "$location/$entry"
    else
        echo "Entry '$entry' does not exist at '$fullpath'. Skipping."
    fi
done < "$dotbot_list"

echo "Dotbot tasks completed."
