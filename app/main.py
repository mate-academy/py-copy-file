
def copy_file(command: str) -> None:

    str_parts = command.strip().split(" ")

    if len(str_parts) == 3 and str_parts[0] == "cp":
        cmd, origin, destination = str_parts

        if origin != destination:
            try:
                with (open(origin, "r") as source_file,
                      open(destination, "w") as destination_file):

                    destination_file.write(source_file.read())

            except FileNotFoundError:
                pass
