def copy_file(command: str) -> None:
    cp, file_name, new_file_name = command.split()

    if file_name != new_file_name and cp == "cp":
        with (open(file_name, "r") as file_in,
              open(new_file_name, "w") as file_out):
            file_out.write(file_in.read())
