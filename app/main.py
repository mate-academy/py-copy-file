def copy_file(command: str) -> None:
    parts = command.split(" ")
    try:
        if len(parts) == 3 and parts[0] == "cp" and parts[1] != parts[2]:
            cp, source_file_name, destination_file_name = parts
            with (open(source_file_name, "r") as file_in,
                  open(destination_file_name, "w") as file_out):
                file_out.write(file_in.read())
    except FileNotFoundError:
        print("File not found")
