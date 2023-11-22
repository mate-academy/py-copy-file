def copy_file(command: str) -> None:
    if len(command.split(" ")) == 3:
        command, file, new_file = command.split(" ")
        if command == "cp":
            if file != new_file:
                with open(file, "r") as file_in, open(new_file, "w") as file_out:
                    file_out.write(file_in.read())
