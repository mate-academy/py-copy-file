from pathlib import Path
from app.main import copy_file


def test_copy_file_same_name(tmp_path: Path) -> None:
    file_path = tmp_path / "test.txt"
    file_path.write_text("Hello world")

    command = f"cp {file_path} {file_path}"
    copy_file(command)

    assert file_path.read_text() == "Hello world"


def test_copy_file_different_name(tmp_path: Path) -> None:
    source_path = tmp_path / "source.txt"
    dest_path = tmp_path / "dest.txt"
    source_path.write_text("Test content for copying")

    command = f"cp {source_path} {dest_path}"
    copy_file(command)

    assert dest_path.read_text() == "Test content for copying"
    assert source_path.read_text() == dest_path.read_text()
