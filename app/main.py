class CommandNameError(Exception):
    """CommandNameError"""


class DoubleNameError(Exception):
    """DoubleNameError"""


class LanCommandError(Exception):
    """LaneCommandError"""


def copy_file(command: str) -> None:
    command_elements = command.split()

    if len(command_elements) < 3:
        raise LanCommandError(
            "it must start with 'cp' and include two file names"
            " 'cp input_file_name.txt output_file_name.txt'"
        )

    if command_elements[0] != "cp":
        raise CommandNameError(f"'{command_elements[0]}' is not 'cp' command")

    if command_elements[1] == command_elements[2]:
        raise DoubleNameError(
            f"intput: {command_elements[1]} output: {command_elements[1]}"
            f" must not have the same names"
        )

    with (
        open(command_elements[1], "r") as file_input,
        open(command_elements[2], "w") as file_output
    ):
        file_output.write(file_input.read())
