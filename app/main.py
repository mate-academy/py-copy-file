def copy_file(command: str) -> None:
    file_to_copy = command.split(" ")[1]
    new_file = command.split(" ")[2]

    if file_to_copy == new_file:
        return

    with (open(file_to_copy, "r") as file_in,
          open(new_file, "w") as file_out):
        file_out.write(file_in.read())
