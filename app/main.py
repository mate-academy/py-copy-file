def copy_file(command: str) -> None:
    args = command.split(" ")
    if (args
            and args[0] == "cp"
            and len(args) == 3
            and args[1] != args[2]):
        try:
            with (open(args[1], "r") as file_to_read,
                  open(args[2], "w") as file_to_write):
                for line in file_to_read:
                    file_to_write.write(line)
        except FileNotFoundError:
            pass
