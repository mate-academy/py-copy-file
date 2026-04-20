def copy_file(command: str) -> str | int:

    arguments = [text for text in command.split(" ") if text != ""]
    if len(arguments) != 3:
        return "Too few parameter(s)"
    if arguments[0] != "cp":
        return "Not a valid command"

    if arguments[1] != arguments[2]:
        try:
            with (open(arguments[1], "r") as file_in,
                  open(arguments[2], "w") as file_out):
                file_out.write(file_in.read())
        except FileNotFoundError as e:
            return str(e)
    return 0
