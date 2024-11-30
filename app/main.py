def copy_file(command: str) -> None:
    for part in command.split(" "):
        if part[1] != part[2]:
            with open(part[1], "r") as file_in, open(part[2], "w") as file_out:
                file_out.write(file_in)
