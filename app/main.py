def copy_file(command: str) -> None:
    files_names = command.split()
    file_to_copy = files_names[1]
    new_file = files_names[2]
    if file_to_copy == new_file:
        return
    with (open(f"{file_to_copy}", "r") as file_in,
          open(f"{new_file}", "w") as file_out):
        content = file_in.read()
        file_out.write(content)
