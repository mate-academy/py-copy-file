def copy_file(command: str) -> None:
    parts = command.split()
    source_file = parts[1]
    destination_file = parts[2]
    if (parts[0] == "cp" and len(parts) == 3
            and not source_file == destination_file):
        try:
            with open(source_file, "r") as file_in:
                pass

        except FileNotFoundError:
            with open(source_file, "w") as file_in:
                pass

        with (open(source_file, "r") as file_in,
              open(destination_file, "w") as file_out):
            content = file_in.read()
            file_out.write(content)
