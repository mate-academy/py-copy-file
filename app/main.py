class CommandError(Exception):
    pass


def copy_file(command: str) -> None:
    command = command.split()
    if len(command) != 3:
        raise CommandError("Unsupported format of command")

    cmd, file_name, new_file_name = command
    if cmd == "cp":
        if file_name != new_file_name:
            try:
                with (open(file_name, "r") as source,
                        open(new_file_name, "w") as new_file):
                    new_file.write(source.read())
                print("Copying done!")
            except FileNotFoundError as e:
                print(e)
        else:
            print("File with the same name cannot be copied!")
    else:
        raise CommandError(f"Unknown command: {cmd}\n"
                            "Did you mean 'cp'?")


