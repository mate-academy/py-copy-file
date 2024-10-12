class CommandNameError(Exception):
    """CommandNameError"""


class DoubleNameError(Exception):
    """DoubleNameError"""


class LanCommandError(Exception):
    """LaneCommandError"""


def copy_file(command: str) -> None:
    split_command = command.split()

    if len(split_command) < 3:
        raise LanCommandError(
            "The command must be"
            " 'cp input_file_name.txt output_file_name.txt'"
        )

    if split_command[1] == split_command[2]:
        raise DoubleNameError(
            f"intput: {split_command[1]} output: {split_command[1]}"
            f" must not have the same names"
        )

    if split_command[0] == "cp":
        with (
            open(split_command[1], "r") as file_input,
            open(split_command[2], "w") as file_output
        ):
            file_output.write(file_input.read())
    else:
        raise CommandNameError(f"'{split_command[0]}' is not 'cp' command")
