from pathlib import Path


def copy_file(command: str) -> None:

    command_list = command.split()
    if (len(command_list) == 3
            and command_list[0] == "cp"
            and Path(command_list[1]).exists()
            and command_list[1] != command_list[2]):

        with (open(command_list[1], "r") as original_file,
              open(command_list[2], "w") as copied_file):

            for line in original_file:
                copied_file.write(line)
