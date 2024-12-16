def copy_file(command: str) -> None:
    command = command.split(" ")
    source_file_name = command[1]
    destination_file_name = command[2]
    if len(command) != 3 or command[0] != "cp":
        return
    if source_file_name != destination_file_name:
        with (open(source_file_name, "r") as file,
              open(destination_file_name, "w") as new_file):
            for line in file:
                new_file.write(f"{line}")
