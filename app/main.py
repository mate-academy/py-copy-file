def copy_file(command: str) -> None:
    cp, file, new_file = command.split()

    if(
        cp == "cp"
        and file.endswith(".txt") and len(file.split(".")[0]) > 0
        and new_file.endswith(".txt") and len(new_file.split(".")[0]) > 0
        and file != new_file
    ):
        with open(file, "r") as file_in, open(new_file, "w") as file_out:
            file_out.write(file_in.read())
