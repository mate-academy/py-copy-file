def copy_file(command: str) -> None:
    if len(command.split()) == 3:
        command, copied_file, file_to_copy = command.split()
        if command == "cp" and copied_file != file_to_copy:
                with open(copied_file, "r") as file_in, \
                        open(file_to_copy, "w") as file_out:
                    file_out.write(file_in.read() + "\n")
