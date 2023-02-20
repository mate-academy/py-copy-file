def copy_file(command: str) -> None:
    cp, file_orig, file_cop = command.split()
    if (cp == "cp"
            and file_orig != file_cop):
        with open(file_orig, "r") as origin, open(file_cop, "w") as copy:
            content = origin.read()
            copy.write(content)
