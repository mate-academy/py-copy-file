def copy_file(command: str) -> None:
    command, source_file, result_file = command.split()

    if not source_file == result_file and command == "cp":
        with (open(source_file, "r") as source,
              open(result_file, "w") as result):
            result.write(source.read())
