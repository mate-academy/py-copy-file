def copy_file(command: str) -> None:
    if len(command.split()) == 3:
        linux_command, old_file, new_file = command.split()
    else:
        raise "Need write command, copied file, new file"
    if linux_command == "cp":
        with open(old_file, "r") as file_in, open(new_file, "w") as file_out:
            file_out.write(file_in.read())
    else:
        raise "Command not found"
