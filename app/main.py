def copy_file(command: str) -> None:
    if len(command.split()) != 3:
        return print("Command length is not equal to 3")

    action, original_file, new_file = command.split()
    if action == "cp" and original_file != new_file:
        with open(original_file, "r") as file_in, \
                open(new_file, "w") as file_out:
            file_out.write(file_in.read())
