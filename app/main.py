def copy_file(command: str) -> None:
    command_, current_file, new_file = command.split()

    if current_file != new_file and command_ == "cp":
        with (
            open(current_file, "r") as file_in,
            open(new_file, "w") as file_out
        ):
            file_out.write(file_in.read())
