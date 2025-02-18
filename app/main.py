def copy_file(cp: str) -> None:
    list_input = cp.split()
    command, file_in, file_out = list_input
    if command == "cp" and len(list_input) == 3:
        if file_in != file_out:
            with open(
                "app/"
                + file_in, "r"
            ) as original, open("app/" + file_out, "w") as copy:
                copy.write(original.read())
