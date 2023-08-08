def copy_file(command: str) -> None:
    command = command.split()
    if len(command) != 3:
        print("Enter the correct command.")
        return
    _, file_copy, file_paste = command
    if file_copy != file_paste and _ == "cp":
        with (open(file_copy, "r") as file_in,
              open(file_paste, "w") as file_out):
            file_out.write(file_in.read())
