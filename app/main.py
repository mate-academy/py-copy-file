def copy_file(command: str) -> None:
    info = command.split()
    if len(info) == 3:
        command, original_file, new_file = info[0], info[1], info[2]

        if command == "cp" and (original_file != new_file):
            with open(info[1], "r") as file_in, open(info[2], "w") as file_out:
                content = file_in.read()
                file_out.write(content)
