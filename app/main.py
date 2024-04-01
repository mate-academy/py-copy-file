def copy_file(command: str) -> None:
    _, old_file, new_file = command.split()

    if len(command.split()) != 3 or command.split()[0] != "cp":
        print("Invalid command format.")
        return

    if old_file != new_file:
        with (
            open(old_file, "r") as file_in,
            open(new_file, "w") as file_out
        ):
            file_out.write(file_in.read())
