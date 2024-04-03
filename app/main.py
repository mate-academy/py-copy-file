def copy_file(command: str) -> None:
    if len(command) < 3:
        return
    operation, file_name_to_copy, new_file_name = command.split(" ")

    if file_name_to_copy == new_file_name or operation != "cp":
        return

    with (open(file_name_to_copy, "r") as file_in,
          open(new_file_name, "w") as file_out):
        file_out.write(file_in.read())
