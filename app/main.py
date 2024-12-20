def copy_file(command: str) -> str | None:
    command_info = command.split(" ")

    if "cp" in command_info[0]:
        if command_info[1] == command_info[2]:
            return None
        else:
            with (open(command_info[1], "r") as original_file,
                  open(command_info[2], "w") as new_file):
                for line in original_file.readline():
                    new_file.write(line)
