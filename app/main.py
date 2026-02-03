import os


def copy_file(command: str) -> None:
    command_elems = command.split(" ")
    command = ""
    filename = ""
    copy_name = ""

    if len(command_elems) == 3:
        command = command_elems[0]
        filename = command_elems[1]
        copy_name = command_elems[2]

    if (
        len(command_elems) == 3 and command == "cp"
        and filename != copy_name
        and os.path.exists(filename)
    ):
        with open(filename, "r") as file_in, open(copy_name, "w") as file_out:
            original_text = file_in.read()
            file_out.write(original_text)
