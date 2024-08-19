def copy_file(command: str) -> None:
    if (not (command.startswith("cp "))
            and len(command.split()) == 3):
        return

    cmd, file1, file2 = command.split()
    if (file1 == file2
            or not file1.endswith(".txt")
            or not file2.endswith(".txt")):
        return

    with open(f"{file1}", "r") as file_in, open(f"{file2}", "w") as file_out:
        file_out.write(file_in.read())
