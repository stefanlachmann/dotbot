import os
import shutil
import subprocess

def test_copy_dotbot_entries():
    # Set up test data
    os.environ["LOCATION"] = "/path/to/location"
    dotbot_list_content = [
        "file1.txt",
        "folder1/",
        "file2.txt"
    ]
    dotbot_list_file = "dotbots_list.txt"
    with open(dotbot_list_file, "w") as file:
        file.write("\n".join(dotbot_list_content))

    # Run the script
    subprocess.run(["bash", "./copy_dotbot_entries.sh"])

    # Assert that the files/folders were copied to the specified location
    expected_copied_files = [
        "file1.txt",
        "folder1/",
        "file2.txt"
    ]
    for entry in expected_copied_files:
        fullpath = os.path.join("/home/user", entry)
        location_path = os.path.join("/path/to/location", entry)
        assert os.path.exists(location_path), f"Entry '{entry}' not found at '{location_path}'"

    # Clean up
    os.remove(dotbot_list_file)
    shutil.rmtree("/path/to/location")

