#!/usr/local/bin/bash

function sync() {
	# cp -r "$HOME/$1" .
	cp -r "$1" . # location
}

# use to automate task of removing unneeded files like *.swap or whatever
function cleanup() {
 	echo "$PWD"/"$1"
 	sudo rm -rf "$PWD"/"$1"
}


# sync files
dotbot_list_files="dotbots_files_list.txt"
while IFS= read -r entry; do
		echo "syncing file: $entry"
		sync "$entry"
done < "$dotbot_list_files"


# sync Folders
dotbot_list_files="dotbots_folders_list.txt"
while IFS= read -r entry; do
		echo "syncing folder: $entry"
		sync "$entry"
done < "$dotbot_list_files"


    if hash lolcat 2>/dev/null; then
        'sync completed' | lolcat
    else
         'sync completed'
    fi
