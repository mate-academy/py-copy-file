def copy_file(command: str) -> None:
    comm, file_1, file_2 = command.split()
    check_for_valid_command = comm == "cp" and len(command.split()) == 3
    if file_1 != file_2 and check_for_valid_command:
        with (open(file_1, "r") as file_in,
              open(file_2, "w") as file_out):
            file_out.write(file_in.read())
