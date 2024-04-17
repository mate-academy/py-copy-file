def copi_file(command: str) -> None:
    command_parts = command.split()
    if command_parts[0] == "cp" and command_parts[1] != command_parts[2]:
        with (open(command_parts[1], "r") as file_in,
              open(command_parts[2], "w") as file_out):
            file_out.write(file_in.read())
            print("File copied")
    else:
        print("Wrong command!")
