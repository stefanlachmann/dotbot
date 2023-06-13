#!/bin/bash

# Exit on error
set -e

# Read the location from the environment variable    
# shellcheck disable=SC2153
location="$LOCATION" || $DOTBOT_LOCATION

# Verify if the location exists
while [[ ! -d "$location" ]]; do
    echo "Invalid location: $location"
    read -rp "Please enter a valid location: " location
done

# Read the dotbot entries from the dotbots_list.txt file
dotbot_list="dotbots_list.txt"
while IFS= read -r entry; do
    # Concatenate the path with the entry
    fullpath="$HOME/$entry"

    # Check if the entry exists
    if [[ -e "$fullpath" ]]; then
        echo "Copying '$entry' to '$location'"
        cp -r "$fullpath" "$location"
    else
        echo "Entry '$entry' does not exist at '$fullpath'. Skipping."
    fi
done < "$dotbot_list"

echo "Dotbot tasks completed."
