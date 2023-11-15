def copy_file(command: str) -> None:
    files = command.split()
    if files[1] != files[2]:
        with open(files[1], "r") as file_in, open(files[2], "w") as file_out:
            lines = file_in.readlines()
            for line in lines:
                file_out.write(line)
