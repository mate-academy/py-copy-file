def copy_file(cp: str) -> None:
    command, file_in, file_out = cp.split()
    if command == "cp":
        with open(
            "app/"
            + file_in, "r"
        ) as original, open("app/" + file_out, "w") as copy:
            copy.write(original.read())
