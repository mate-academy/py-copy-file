import os


def copy_file(command: str) -> None:
    if len(command.split(" ")) < 3:
        return

    copy_command, file_name_in, file_name_out = command.split(" ")
    if (
        file_name_in == file_name_out
        or not os.path.isfile(file_name_in)
        or copy_command != "cp"
        or file_name_out is None
    ):
        return

    with (
        open(file_name_in, "r") as file_in,
        open(file_name_out, "w") as file_out,
    ):
        file_out.write(file_in.read())
