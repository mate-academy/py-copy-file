def copy_file(command: str) -> None:
    files = command.split(" ")
    if len(files) == 3 and files[0] == "cp" and files[1] != files[2]:
        with open(files[1], "r") as file_in, open(files[2], "w") as file_out:
            for line in file_in.readlines():
                file_out.write(line)
