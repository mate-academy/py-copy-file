def copy_file(command: str) -> None:
    command_parts = command.strip().split()

    if len(command_parts) != 3:
        print("The command format is incorrect")
        return

    command_name, source_file_name, destination_file_name = command_parts

    if command_name != "cp":
        print("The command is not 'cp'")
        return

    if source_file_name == destination_file_name:
        print("The source and destination file names are the same")
        return

    try:
        with (open(source_file_name, "r") as source_file,
              open(destination_file_name, "w") as destination_file
              ):
            destination_file.write(source_file.read())
    except FileNotFoundError:
        print("The source file is not found")
        return
    print("Successfully copying a file")
