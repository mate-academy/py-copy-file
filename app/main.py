def copy_file(command: str) -> None:
    if len(command.split()) != 3:
        print("Invalid command. "
              "Use the format: cp <source_file> <destination_file>")
        return

    command_name, file_in, file_out = command.split()

    if command_name != "cp" or file_in == file_out:
        print("Does nothing")
        return

    with open(file_in, "r") as fi, open(file_out, "w") as fo:
        fo.write(fi.read())
