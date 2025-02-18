def copy_file(command: str) -> None:
    arguments = command.split()
    if (len(arguments) == 3 and arguments[0] == "cp"
            and arguments[1] != arguments[2]):
        first_file, second_file = arguments[1], arguments[2]
        with (open(first_file, "r") as original,
              open(second_file, "w") as copied):
            copied.write(original.read())
