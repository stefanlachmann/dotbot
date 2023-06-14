import os
from unittest.main import main

dotbot_files_list = []
dotbot_folders_list = []
dotbots_files_txt = "dotbots_files.txt"
dotbots_folders_txt = "dotbots_folders.txt"

recreate_files = []
files_temp = os.listdir(os.path.expanduser("~"))


def main():
    initialize()
    create_files_txt()
    create_folders_txt()
    define_location()
    setup_git_repo()
    write_to_file()
    start_dotbot()


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def file_exists_and_not_empty(file_path):
    print(file_path)
    if len(file_path) > 0 and os.path.isfile(file_path) and os.path.getsize(file_path) > 0:
        return True
    return False


def initialize():
    # verify if files exists and if they should be recreated
    file_paths = ["dotbots_folders_txt", "dotbots_files_txt"]
    for f in file_paths:
        if file_exists_and_not_empty(f):
            print(f"File {f} exists and is not empty.")
            question = "Do you want to keep the current version, if no it will be deleted and recreated (y/n)? "
            recreate = input(question)
            recreate_files.append(recreate)
            if recreate == "n":
                os.remove(f)
                print("File {f} removed successfully.")
            else:
                print("File {f} will remain unchanged.")
                recreate_files.append('y')
        else:
            print(
                f"{bcolors.OKBLUE}File {f} does not exist, it will be created{bcolors.ENDC}")


def create_files_txt():
    if file_exists_and_not_empty("dotbots_files.txt") == False or len(recreate_files) > 0 and recreate_files[0] == 'y':

        # Process files
        for file_name in files_temp:
            file_path = os.path.join(os.path.expanduser("~"), file_name)

        # Check if the entry is a file
        if os.path.isfile(file_path):
            # Ask whether to keep the file
            choice = input(f"Do you want to keep \"{file_name}\"? (y/n) ")
            if choice == "y":
                print(f"{bcolors.OKCYAN}Keeping \"{file_name}\"{bcolors.ENDC}")
                dotbot_files_list.append(file_path)
            else:
                print(f"{bcolors.WARNING}Discarding \"{file_name}\" {bcolors.ENDC}")


def create_folders_txt():
    if file_exists_and_not_empty(dotbot_folders_list) == False or len(recreate_files) > 0 and recreate_files[0] == 'y':
        # Process folders
        folders_temp = [folder_name for folder_name in files_temp if os.path.isdir(
            os.path.join(os.path.expanduser("~"), folder_name))]
        for folder_name in folders_temp:
            folder_path = os.path.join(os.path.expanduser("~"), folder_name)

        # Ask whether to keep the folder
        choice = input(f"Do you want to keep folder \"{folder_name}\"? (y/n) ")

        if choice == "y":
            print(f"Keeping folder \"{folder_name}\"")
            dotbot_folders_list.append(f"{folder_path}/")
        else:
            print(f"Discarding folder \"{folder_name}\"")


def define_location():
    # Prompt for location on disk and write to file
    location = input(
        f"Enter the project location [default: {os.path.expanduser('~')}/projects/dotbot]: ")

    if not location:
        location = os.path.expanduser("~/projects/dotbot")

    # Set the environment variable
    with open("location.txt", "w") as file:
        file.write(location)

    # Create the project directory if it doesn't exist
    os.makedirs(location, exist_ok=True)


def setup_git_repo(location_file="location.txt"):
    with open(location_file, 'r') as file:
        # Read the entire contents of the file
        location = file.read()
        print(location)

    # Initialize a Git repository
    os.system(f"git init {location}")
    open(os.path.join(location, ".gitignore"), "a").close()

    print(f"Project location: {location}")


def write_to_file():
    if file_exists_and_not_empty(dotbot_folders_list) == False or len(recreate_files) > 0 and recreate_files[0] == 'y':
        # Write selected entries to the dotbot_files txt file
        with open(dotbots_files_txt, "w") as file:
            for entry in dotbot_files_list:
                file.write(entry + "\n")

        with open(dotbots_folders_txt, "w") as file:
            for entry in dotbot_folders_list:
                file.write(entry + "\n")

    # Read each entry from the lists and check if it exists
    for entry in dotbot_files_list:
        fullpath = os.path.join(os.path.expanduser("~"), entry)
        if os.path.exists(fullpath):
            print(
                f"{bcolors.OKGREEN}Entry '{entry}' exists at '{fullpath}'.{bcolors.ENDC}.")
        else:
            print(
                f"{bcolors.WARNING}Entry {entry} does not exist at {fullpath}.{bcolors.ENDC}.")

    if file_exists_and_not_empty(dotbot_folders_list) == False or len(recreate_files) > 0 and recreate_files[1] == 'y':
            fullpath = os.path.join(os.path.expanduser("~"), entry)
            if os.path.exists(fullpath):
                print(
                    f"{bcolors.OKGREEN}Entry '{entry}' exists at '{fullpath}'.{bcolors.ENDC}.")
            else:
                print(
                    f"{bcolors.WARNING}Entry {entry} does not exist at {fullpath}.{bcolors.ENDC}.")

            if os.path.exists(fullpath):
                print(
                    f"{bcolors.OKGREEN}Entry '{entry}' exists at '{fullpath}{bcolors.ENDC}.")
            else:
                print(
                    f"{bcolors.WARNING}Entry {entry} does not exist at {fullpath}{bcolors.ENDC}.")


def start_dotbot():
    run_dotbot = input("Do you wish to run dotbot now? (y/n): ")
    if run_dotbot == "y":
        os.system("bash ./sync_dots.sh")
    else:
        print("Another time then. If you wish to run dotbot, execute it with 'bash ./run_dotbot.sh'")


if __name__ == "__main__":
    main()
