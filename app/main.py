def copy_file(command: str) -> None:
    action, file, new_file = command.split(" ")

    if action == "cp":
        if file != new_file:
            with open(file) as file_in, open(new_file, "w") as file_out:
                file_out.write(file_in.read())
