def copy_file(command: str) -> None:
    if command.startswith("cp"):
        files = command.split(" ")[1:]
        if len(tuple(files)) > 1:
            with (open(files[0], "r") as file_to_copy,
                  open(files[1], "w") as file_copy):
                file_copy.write(file_to_copy.read())
