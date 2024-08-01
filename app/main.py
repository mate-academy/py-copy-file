def copy_file(command: str) -> None:
    source_file, new_file = command.split(" ")[1:]
    if source_file != new_file:
        with open(source_file) as file_out, open(new_file, "w") as file_in:
            file_in.writelines(file_out.readlines())
