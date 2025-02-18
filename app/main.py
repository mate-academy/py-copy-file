def copy_file(command: str) -> None:
    words = command.split(" ")
    if len(words) != 3:
        return
    cp_command, file_to_copy, new_file = command.split(" ")
    if file_to_copy == new_file:
        return
    if cp_command == "cp":
        with (open(file_to_copy, "r") as file_in,
              open(new_file, "w") as file_out):
            file_out.write(file_in.read())
