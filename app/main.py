def copy_file(command: str) -> None:
    file_to_copy = command.split()[1]
    file_copy = command.split()[2]

    if file_copy != file_to_copy and command.split()[0] == "cp":
        with (open(file_to_copy, "r") as file_in,
              open(file_copy, "w") as file_out):
            file_out.write(file_in.read())
