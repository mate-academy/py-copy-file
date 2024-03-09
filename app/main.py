def copy_file(command: str) -> None:
    if len(command.split()) != 3:
        return
    action, source_file, destination_file = command.split()
    if source_file != destination_file:
        with (open(source_file, "r") as file_in,
              open(destination_file, "w") as file_out):
            file_out.writelines(file_in)
