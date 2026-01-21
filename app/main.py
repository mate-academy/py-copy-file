def copy_file(command: str) -> None:
    command, old_file, new_file = command.split()
    if command != "cp":
        raise ValueError(f"Name of copy command "
                         f"should not be {command}")

    if old_file != new_file:
        with open(old_file, "r") as file_in, open(new_file, "w") as file_out:
            file_out.write(file_in.read())
