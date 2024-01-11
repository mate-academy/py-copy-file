def copy_file(command: str) -> None:
    if len(command) == 3:
        cp, file_from, file_to = command.split(" ")

        if file_from != file_to and cp == "cp":
            with (open(file_to, "r") as file_in,
                  open(file_from, "w") as file_out):
                file_out.write(file_in.read())
