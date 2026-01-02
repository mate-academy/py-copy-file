
def copy_file(command: str) -> None:

    if command.split()[0] == "cp" and len(command.split()) == 3:
        parts = command.split()
        source_file_name = parts[1]
        destination_file_name = parts[2]

        if source_file_name == destination_file_name:
            return

    with (open(source_file_name, "r") as file_in,
          open(destination_file_name, "w") as file_out):
        file_out.write(file_in.read())
