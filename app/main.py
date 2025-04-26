import os


def copy_file(input_command: str) -> None:
    parts = input_command.split(" ")
    if len(parts) != 3:
        return

    command, source, target = parts
    if command == "cp":
        if source != target:
            if os.path.exists(source):
                with (open(source, "r") as file_in,
                      open(target, "w") as file_out):
                    file_out.write(file_in.read())
