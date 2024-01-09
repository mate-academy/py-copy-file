def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) == 3 and parts[1] != parts[2]:
        with (open(parts[1], "r") as file1,
              open(parts[2], "w") as file2):
            file2.write(file1.read())
