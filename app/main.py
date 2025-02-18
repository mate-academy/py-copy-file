def copy_file(command: str) -> None:
    command, file_we_want_copy, new_file = command.split()
    if file_we_want_copy != new_file:
        with (open(file_we_want_copy, "r") as file_in,
              open(new_file, "w") as file_out):
            file_out.write(file_in.read())
