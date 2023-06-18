def copy_file(command: str) -> None:
    _, source_file, res_file = command.split()
    if not command.startswith("cp"):
        raise Exception("this interface support only 'cp' command")
    if source_file != res_file:
        with open(source_file, "r") as file1, open(res_file, "w") as file2:
            file2.write(file1.read())
