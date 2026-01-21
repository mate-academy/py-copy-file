def copy_file(task: str) -> None:
    command_parts = task.split(" ")
    if len(command_parts) != 3 or command_parts[1] == command_parts[-1]:
        return
    if command_parts[0] == "cp":
        try:
            with (open(command_parts[1], "r") as source_file,
                  open(command_parts[-1], "w") as destination_file):
                for line in source_file.readlines():
                    destination_file.write(line)
        except FileNotFoundError:
            return
