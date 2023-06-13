# Dotbot

<!-- markdownlint-disable -->
<p align="center">
  <img src="./assets/dotbot.png" alt="Dotbot" title="Dotbot">
</p>
<!-- markdownlint-enable -->
Dotbot is a script that helps you manage your dotfiles and directories in a convenient way. It allows you to selectively choose which files and folders to keep and organizes them in a specified project location. Dotbot also provides integration with Git for version control.

## Features

- Interactively select and organize dotfiles and directories.
- Specify a project location for storing the selected dotfiles and directories.
- Initialize a Git repository in the project location for version control.
- Generate a list of selected dotfiles and directories in a text file.
- Verify the existence of selected dotfiles and directories.
- Option to run a separate dotbot script for further processing.

## Prerequisites

- Python 3.x
- Git

## Usage

1. Clone the repository:

2. Navigate to the project directory:

3 Run the dotbot.py script:

```Python
python3 dotbot.py
```

4. Follow the prompts to select and organize your dotfiles and directories.

5. Specify the project location where the dotfiles and directories will be stored. If not provided, a default location will be used.

6. The selected dotfiles and directories will be listed, and their existence will be verified.

7. Optionally, you can choose to run the dotbot script for further processing.

8. If you wish to run the dotbot script separately, execute it with the following command:

```bash
bash run_dotbot.sh
```

## Unit tests

Unit tests for the dotbot.py module can be found in the tests directory. To run the tests, you will need pytest. Install pytest using the following command:

```py
pip install pytest
```

To run the tests, navigate to the project directory and execute the following command:

```py
pytest -s
```

License
This project is licensed under the MIT License.
