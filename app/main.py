def copy_file(command: str) -> None:
    cp, file_to_copy, file_copy = command.split()

    if file_copy != file_to_copy and cp == "cp":
        with (open(file_to_copy, "r") as file_in,
              open(file_copy, "w") as file_out):
            file_out.write(file_in.read())
