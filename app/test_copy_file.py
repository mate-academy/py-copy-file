from main import copy_file


def test_copy_file() -> None:
    copy_file("cp requirements.txt a.txt")
