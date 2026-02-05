from os import path


def copy_file(command: str) -> None:
    parts = command.split(" ")
    if len(parts) == 3:
        cmd, origin, copy = parts[0], parts[1], parts[2]
        if cmd == "cp" and origin != copy:
            if path.isfile(origin):

                with (open(origin, "r") as file_data,
                      open(copy, "w") as file_out):
                    file_out.write(file_data.read())
