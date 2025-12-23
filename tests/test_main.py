import os

import pytest

from app.main import (copy_file)


@pytest.fixture
def setup_and_teardown_files():
    """A fixture to create and delete test files."""
    source_filename = "test_source.txt"
    target_filename = "test_target.txt"
    content = "Hello, Mate!"

    with open(source_filename, "w") as f:
        f.write(content)

    yield source_filename, target_filename, content  # Provide the filenames and content for the test

    # Remove files after test
    if os.path.exists(source_filename):
        os.remove(source_filename)
    if os.path.exists(target_filename):
        os.remove(target_filename)


def test_copy_file_successful(setup_and_teardown_files):
    """Test if the file is copied successfully."""
    source_filename, target_filename, content = setup_and_teardown_files

    copy_file(f"cp {source_filename} {target_filename}")

    with open(target_filename, "r") as f:
        copied_content = f.read()

    assert copied_content == content


def test_do_nothing_if_same_names(setup_and_teardown_files):
    """Test that the function does nothing if names are the same."""
    source_filename, _, _ = setup_and_teardown_files

    copy_file(f"cp {source_filename} {source_filename}")
    assert not os.path.exists("test_target.txt")  # Target file should not exist


def test_invalid_command_no_action(setup_and_teardown_files):
    """Test that the function does nothing for an invalid command."""
    _, target_filename, _ = setup_and_teardown_files

    copy_file("invalid_command test_source.txt test_target.txt")
    assert not os.path.exists(target_filename)


def test_missing_source_file(setup_and_teardown_files):
    """Test that the function handles missing source file gracefully."""
    _, target_filename, _ = setup_and_teardown_files

    copy_file("cp non_existing_file.txt test_target.txt")
    assert not os.path.exists(target_filename)


def test_command_with_incorrect_format(setup_and_teardown_files):
    """Test that the function handles an incorrectly formatted command."""
    _, target_filename, _ = setup_and_teardown_files

    copy_file("cp only_one_argument.txt")
    assert not os.path.exists(target_filename)


def test_empty_command(setup_and_teardown_files):
    """Test that the function does nothing for an empty command."""
    _, target_filename, _ = setup_and_teardown_files

    copy_file("")
    assert not os.path.exists(target_filename)
