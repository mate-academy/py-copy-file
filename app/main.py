def copy_file(command: str) -> object:
    new_str = command.split()
    file_current = str(new_str[1])
    file_future = str(new_str[2])

    if file_current != file_future and new_str[0] == "cp":
        with (
            open(file_current, "r") as file_in,
            open(file_future, "w") as file_out
        ):
            text_wit_file = file_in.read()
            file_out.write(text_wit_file)
