def copy_file(command: str) -> None:
    comm, file, new_file = command.split()
    if file != new_file and comm == "cp":
        with open(file, "r") as file_in, open(new_file, "w") as file_out:
            file_out.write(file_in.read())
