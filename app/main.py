def copy_file(command: str) -> None:
    file_origin = command.split()[1]
    file_copy = command.split()[2]
    command = command.split()[0]
    if file_origin != file_copy and command == "cp":
        with (open(f"{file_origin}", "r") as file_in,
              open(f"{file_copy}", "w") as file_out):
            file_out.write(file_in.read())
