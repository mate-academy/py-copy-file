def copy_file(command: str) -> None:
    operation, old_name, new_name = command.split()
    if operation == "cp" and old_name != new_name:
        with open(old_name, "r") as reader, open(new_name, "w") as writer:
            writer.write(reader.read())
