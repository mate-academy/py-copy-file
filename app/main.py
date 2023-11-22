def copy_file(command: str) -> None:
    command_keyword, file, new_file = command.split(" ")
    if command_keyword == "cp":
        if file != new_file:
            with open(file, "r") as file_in, open(new_file, "w") as file_out:
                file_out.write(file_in.read())
