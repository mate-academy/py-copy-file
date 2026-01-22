def copy_file(command: str) -> None:
    if len(command.split()) >= 3:
        try:
            with (open(command.split()[1].lower(), "r") as initial_file,
                  open(command.split()[2].lower(), "w") as new_file):
                if initial_file.name == new_file.name:
                    return
                else:
                    new_file.write(initial_file.read())
        except FileNotFoundError:
            print("File not found")
