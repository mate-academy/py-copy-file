def copy_file(command: str) -> int:

    arguments = [text for text in command.split(" ") if text != ""]
    if len(arguments) != 3:
        print("Too few parameter(s)")
        return -1
    if arguments[0] != "cp":
        print("Not a valid command")
        return -1

    if arguments[1] != arguments[2]:
        try:
            with (open(arguments[1], "r") as file_in,
                  open(arguments[2], "w") as file_out):
                file_out.write(file_in.read())
        except Exception as e:
            print(e)
            return -1
    return 0
