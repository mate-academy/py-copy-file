def copy_file(command: str) -> None:
    arguments = command.split()

    if (len(arguments) == 3
            and arguments[0] == "cp"
            and not (arguments[1] == arguments[2])):
        source_file, destination_file = arguments[1:]

        with (open(source_file, "r") as source,
              open(destination_file, "w") as destination):
            destination.write(source.read())
