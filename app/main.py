def copy_file(command: str) -> None:
    order, file_to_copy, new_file = command.split()
    if order == "cp" and file_to_copy != new_file:
        with open(file_to_copy, "r") as file_out:
            with open(new_file, "w") as file_in:
                file_in.write(file_out.read())
