def copy_file(command: str) -> None:
    split_command = command.split(" ")

    if split_command[0] != "cp" or len(split_command) != 3:
        print("Invalid command")
        return

    source_file_name = split_command[1]
    destination_file_name = split_command[2]

    if source_file_name == destination_file_name:
        print("Source and destination file cannot be the same")
        return

    try:
        with (open(source_file_name, "r") as source_file_object,
              open(destination_file_name, "w") as destination_file_object):
            for line in source_file_object:
                destination_file_object.write(line)

    except FileNotFoundError:
        print("Source file not found")
        return
