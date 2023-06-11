class CommandError(Exception):
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

        raise CommandError(f"Unknown command: {command[0]}\n"
                           "Did you mean 'cp'?")

    except CommandError as e:
        print(e)
    except FileNotFoundError as e:
        print(e)
