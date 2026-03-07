def copy_file(command: str) -> None:
    files = command.split(" ")

    if len(files) < 3:
        return

    if (files[0] != "cp") or (files[1] == files[2]):
        return

    try:
        with open(files[1], "r") as file:
            file_content = file.read()

            with open(files[2], "w") as f:
                f.write(file_content)

    except FileNotFoundError:
        return
