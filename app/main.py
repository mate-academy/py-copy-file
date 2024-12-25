def copy_file(command: str) -> None:
    cd = command.split(" ")
    if cd[1] == cd[2]:
        return None
    else:
        with open(cd[1], "r") as file_in, open(cd[2], "w") as file_out:
            for line in file_in:
                file_out.write(line)
