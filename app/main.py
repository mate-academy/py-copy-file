def copy_file(command: str) -> None:
    action, source_file, destination_file = command.split()

    if len(command.split()) == 3 and source_file != destination_file:
        with (open(source_file, "r") as file_in,
              open(destination_file, "w") as file_out):
            file_out.writelines(file_in)
