def copy_file(command: str) -> str:
    commands = command.split(" ")
    if (len(commands) != 3
            or commands[1] == commands[2]
            or commands[0] != "cp") :
        return "Do nothing!"

    try:
        with (open(commands[1], "r")
              as file_in, open(commands[2], "w")
              as file_out):
            file_out.write(file_in.read())
    except FileNotFoundError:
        return "Source file not found!"
