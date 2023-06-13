import os

dotbot_list = []
dotbots_file = "dotbots_list.txt"

# Process files
files_temp = os.listdir(os.path.expanduser("~"))
for file_name in files_temp:
    file_path = os.path.join(os.path.expanduser("~"), file_name)

    # Check if the entry is a file
    if os.path.isfile(file_path):
        # Ask whether to keep the file
        choice = input(f"Do you want to keep \"{file_name}\"? (y/n) ")

        if choice == "y":
            print(f"Keeping \"{file_name}\"")
            dotbot_list.append(file_path)
            # Add your desired code here for processing the kept file
        else:
            print(f"Discarding \"{file_name}\"")
            # Add your desired code here for handling the discarded file

# Process folders
folders_temp = [folder_name for folder_name in files_temp if os.path.isdir(
    os.path.join(os.path.expanduser("~"), folder_name))]
for folder_name in folders_temp:
    folder_path = os.path.join(os.path.expanduser("~"), folder_name)

    # Ask whether to keep the folder
    choice = input(f"Do you want to keep folder \"{folder_name}\"? (y/n) ")

    if choice == "y":
        print(f"Keeping folder \"{folder_name}\"")
        dotbot_list.append(f"{folder_path}/")
    else:
        print(f"Discarding folder \"{folder_name}\"")

# Prompt for location on disk
location = input(
    f"Enter the project location [default: {os.path.expanduser('~')}/project/dotbot]: ")
if not location:
    location = os.path.expanduser("~/project/dotbot")

# Set the environment variable
os.environ["LOCATION"] = location

# Create the project directory if it doesn't exist
os.makedirs(location, exist_ok=True)

# Initialize a Git repository
os.system(f"git init {location}")
open(os.path.join(location, ".gitignore"), "a").close()

print(f"Project location: {location}")

# Write selected entries to the dotbot_list.txt file
with open(dotbots_file, "w") as file:
    for entry in dotbot_list:
        file.write(entry + "\n")

# Read each entry from the list and check if it exists
for entry in dotbot_list:
    fullpath = os.path.join(os.path.expanduser("~"), entry)

    if os.path.exists(fullpath):
        print(f"Entry '{entry}' exists at '{fullpath}'.")
    else:
        print(f"Entry '{entry}' does not exist at '{fullpath}'.")

run_dotbot = input("Do you wish to run dotbot now? (y/n): ")
if run_dotbot == "y":
    os.system("bash ./run_dotbot.sh")
else:
    print("Another time then. If you wish to run dotbot, execute it with 'bash ./run_dotbot.sh'")

if __name__ == "__main__":
    main()