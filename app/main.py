def copy_file(command: str) -> None:
    if command.startswith("cp"):
        temp = command.split()
        old_file, new_file = temp[1], temp[2]
        if temp[1] != temp[2]:
            with open(old_file, "r") as file_in, open(
                new_file, "w"
            ) as file_out:
                file_out.write(file_in.read())
