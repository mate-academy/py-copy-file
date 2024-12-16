def copy_file(command: str) -> None:
    command = command.split(" ")
    file_name = command[1]
    new_file_name = command[2]
    if file_name != new_file_name:
        with (open(file_name, "r") as file,
              open(new_file_name, "w") as new_file):
            for line in file:
                new_file.write(f"{line}")
