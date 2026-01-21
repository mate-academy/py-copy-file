def copy_file(command: str) -> None:
    split_command = command.split(" ")
    if len(split_command) == 3 and split_command[0] == "cp":
        source_file = split_command[1]
        destination_file = split_command[2]

        if source_file == destination_file:
            return

        try:
            with (open(source_file, "r") as file,
                  open(destination_file, "w") as new_file):
                new_file.write(file.read())
        except FileNotFoundError:
            print(f"Source file '{source_file}' not found.")
