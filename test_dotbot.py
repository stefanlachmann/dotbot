import pytest
from unittest import mock
from dotbot import process_files, process_folders, check_location_exists


def test_process_files(monkeypatch):
    # Define the mock user input
    user_inputs = ["y", "n"]

    # Mock the user input
    monkeypatch.setattr("builtins.input", lambda _: user_inputs.pop(0))

    # Call the function under test
    # Add your test code here

    # Assert the expected behavior
    # Add your assertions here


def test_process_folders(monkeypatch):
    # Define the mock user input
    user_input = "y"

    # Mock the user input
    monkeypatch.setattr("builtins.input", lambda _: user_input)

    # Call the function under test
    # Add your test code here

    # Assert the expected behavior
    # Add your assertions here


def test_check_location_exists(monkeypatch):
    # Define the mock user input
    user_input = "/path/to/existing/location"

    # Mock the user input
    monkeypatch.setattr("builtins.input", lambda _: user_input)

    # Call the function under test
    # Add your test code here

    # Assert the expected behavior
    # Add your assertions here
