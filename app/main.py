def copy_file(command: str) -> None:
    tokens = command.split()
    if len(tokens) != 3:
        return
    if tokens[0] != "cp":
        return
    source_file_name = tokens[1]
    destination_file_name = tokens[2]
    if source_file_name == destination_file_name:
        return

    try:
        with (open(source_file_name, "r") as file_out,
              open(destination_file_name, "w") as file_in):
            file_in.write(file_out.read())
    except FileNotFoundError:
        print("File not found")
