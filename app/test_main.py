import os.path

import app.main as main
import pytest


def check_files(first_file: str, second_file: str) -> bool:
    for current_file in [first_file, second_file]:
        if not os.path.exists(current_file):
            return False

    with open(first_file, "r") as first_file, open(
        second_file, "r"
    ) as second_file:
        if first_file.read() != second_file.read():
            return False

    return True


@pytest.mark.parametrize(
    "command, first_file, second_file, bool_result",
    [
        pytest.param(
            "cp file.txt file.txt",
            "file.txt",
            "file.txt",
            True,
            id="Copying the same file",
        ),
        pytest.param(
            "cp file.txt new_file.txt",
            "file.txt",
            "new_file.txt",
            True,
            id="Copying to the new file",
        ),
        pytest.param(
            "cpfile.txtnew_file.txt",
            "file.txt",
            "new_file_.txt",
            False,
            id="Wrong command",
        ),
        pytest.param(
            "cp not_existed_file.txt new_file.txt",
            "not_existed_file.txt",
            "new_file_.txt",
            False,
            id="Testing if file doesn't exist",
        ),
    ],
)
def test_copy_files(
    command: str, first_file: str, second_file: str, bool_result: bool
) -> None:
    main.copy_file(command)
    assert check_files(first_file, second_file) == bool_result

    if (
        bool_result
        and first_file != second_file
        and os.path.exists(second_file)
    ):
        os.remove(second_file)
