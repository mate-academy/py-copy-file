def copy_file(command: str) -> None:
    command, source_file, result_file = command.split()

    if source_file == result_file or command != "cp":
        return

    with (open(source_file, "r") as source,
          open(result_file, "w") as result):
        result.write(source.read())
