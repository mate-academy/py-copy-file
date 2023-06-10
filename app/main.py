class CommandError(Exception):
    pass


class PathError(Exception):
    pass


def copy_file(command: str) -> None:
    try:
        command = command.split()
        if len(command) != 3:
            raise CommandError("Unsupported format of command")
        if command[0] == "cp":
            if command[1] != command[2]:
                with (open(command[1], "r") as source,
                      open(command[2], "w") as new_file):
                    new_file.write(source.read())
                print("Copying done!")
                return

            raise PathError(f"File path {command[1]} and "
                            f"'{command[2]}' can not be the same!")

        raise CommandError(f"Unknown command: {command[0]}\n"
                           "Did you mean 'cp'?")

    except (CommandError, PathError) as e:
        print(e)
    except FileNotFoundError as e:
        print(e)
