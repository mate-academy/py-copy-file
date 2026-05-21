def copy_file(command: str) -> None:
    split_command = command.split(" ")

    if len(split_command) < 3:
        return

    if split_command[0] != "cp":
        return

    source_file_name = split_command[1]
    copy_file_name = split_command[2]

    if source_file_name == copy_file_name:
        return

    try:
        with (open(source_file_name, "r") as source_file,
              open(copy_file_name, "w") as cp_file):
            source_file_content = source_file.read()
            cp_file.write(source_file_content)
    except FileNotFoundError:
        print("File not found")
