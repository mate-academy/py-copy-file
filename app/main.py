def copy_file(command: str) -> None:
    statement, source, target = command.split()

    if source != target and statement == "cp":
        with open(source, "rb") as file_in, open(target, "wb") as file_out:
            file_out.write(file_in.read())
