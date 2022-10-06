def copy_file(command: str) -> None:
    names = command.split()
    cp_command = names[0]
    old_file = names[1]
    new_file = names[2]
    if old_file != new_file and cp_command == "cp":
        with open(old_file, "r") as file_in, open(new_file, "w") as file_out:
            content = file_in.read()
            file_out.write(content)
