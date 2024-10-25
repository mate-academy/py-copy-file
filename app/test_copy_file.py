import os
import pytest
from main import copy_file


@pytest.fixture
def setup_files() -> None:
    """Fixture to set up the test environment by creating a sample file."""
    # Create a sample file to copy
    with open("source_file.txt", "w") as f:
        f.write("This is a test file.")

    yield  # This is where the test will run

    # Cleanup: remove created files after tests
    if os.path.exists("source_file.txt"):
        os.remove("source_file.txt")
    if os.path.exists("copy_file.txt"):
        os.remove("copy_file.txt")


def test_copy_file_valid(setup_files: None) -> None:
    """Test copying a valid file."""
    copy_file("cp source_file.txt copy_file.txt")
    with open("copy_file.txt", "r") as f:
        content = f.read()
    assert content == "This is a test file."


def test_copy_file_same_name(setup_files: None) -> None:
    """Test attempting to copy a file to itself."""
    copy_file("cp source_file.txt source_file.txt")
    # Ensure that the content remains unchanged
    with open("source_file.txt", "r") as f:
        content = f.read()
    assert content == "This is a test file."


def test_copy_file_non_existent_source() -> None:
    """Test attempting to copy a non-existent file."""
    copy_file("cp non_existent.txt copy_file.txt")
    assert not os.path.exists("copy_file.txt")
    # The destination file should not exist
