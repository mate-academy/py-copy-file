def copy_file(command: str) -> None:
    cmd = old_file = new_file = None
    try:
        cmd = command.split()[0]
        old_file = command.split()[1]
        new_file = command.split()[2]
    except IndexError:
        print(f"You don't put all necessary data"
              f"{{'cmd': {cmd},"
              f"'old_file': {old_file},"
              f"'new_file': {new_file}}}")

    try:
        if old_file == new_file:
            raise ValueError(f"You can't copy {old_file} with the same name!")
        if cmd != "cp":
            raise ValueError(f"This command {cmd} unavailable."
                             f" You can just copy file!")
        if not (old_file.endswith(".txt") and new_file.endswith(".txt")):
            raise ValueError("File's format is wrong. It must be just '.txt'")
    except ValueError as ve:
        print(f"{ve}")

    try:
        with open(old_file, "r") as file_in, open(new_file, "w") as file_out:
            file_out.write(file_in.read())
    except FileNotFoundError:
        print(f"File {file_in} doesn't exist or situated in another directory")
