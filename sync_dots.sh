#!/bin/bash


filename="./location.txt"
line_number=1

location=$(sed "${line_number}q;d" "$filename")
echo "Line $line_number: $location"


function sync() {
    if [ "$2" == "folder" ]; then
        local folder_path=${1%/}  # Remove trailing slash from $1
         cp -r "$folder_path" "$location"
        echo "copied folder: $1 to $location/$1"
    else
        cp "$1" "$location"
        echo "copied file: $1 to $location/$1"
    fi
}

# use to automate task of removing unneeded files like *.swap or whatever
function cleanup() {
 	echo "$PWD"/"$1"
 	sudo rm -rf "$PWD"/"$1"
}

# sync files
dotbot_list_files="./dotbots_files.txt"
while IFS= read -r entry; do
		echo "syncing file: $entry"
		sync "$entry"
done < "$dotbot_list_files"



# sync Folders
dotbot_list_folders="./dotbots_folders.txt"
while IFS= read -r entry; do
    echo "Syncing folder: $entry"
    sync "$entry" "folder"
done < "$dotbot_list_folders"


# function completed
    if hash lolcat 2>/dev/null; then
        echo 'sync completed' | lolcat
    else
         'sync completed'
    fi
