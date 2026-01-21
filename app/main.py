def copy_file(command: str) -> None:
    cp, name, new_name = command.split()
    if name != new_name and cp == "cp":
        with open(name, "r") as file_in, open(new_name, "w") as file_out:
            file_out.write(file_in.read())
