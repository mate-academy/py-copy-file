def copy_file(command: str) -> None:
    current_file = command.split()[1]
    copy_file = command.split()[2]
    if current_file != copy_file:
        with open(current_file, "r") as file_in,\
                open(copy_file, "w") as file_out:
            file_out.write("".join(file_in.readlines()))
