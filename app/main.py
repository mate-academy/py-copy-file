class CommandError(Exception):
    pass


def copy_file(command: str) -> None:
    try:
        command = command.split()
        if len(command) != 3:
            raise CommandError("Unsupported format of command")

        cmd, file_name, new_file_name = command
        if cmd == "cp" and file_name != new_file_name:
            with (open(file_name, "r") as source,
                    open(new_file_name, "w") as new_file):
                new_file.write(source.read())
            print("Copying done!")
        else:
            raise CommandError(f"Unknown command: {cmd}\n"
                               "Did you mean 'cp'?")

    except FileNotFoundError as e:
        print(e)
