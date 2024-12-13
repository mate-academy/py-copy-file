def copy_file(cp: str) -> None:
    list_input = cp.split()
    if command == "cp" and len(list_input) = 3:
        command, file_in, file_out = list_input
        with open(
            "app/"
            + file_in, "r"
        ) as original, open("app/" + file_out, "w") as copy:
            copy.write(original.read())
