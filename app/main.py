def copy_file(command: str) -> None:
    _, second_arg, third_arg = command.split()
    with open(second_arg, "r") as source, open(third_arg, "w") as destination:
        destination.write(source.read())
