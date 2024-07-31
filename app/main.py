import shlex


def copy_file(command: str) -> None:
    try:
        command, source_name, destination_name = shlex.split(command)
        if command != "cp":
            raise ValueError("The command is not 'cp'")
    except ValueError as e:
        raise ValueError("The command is not valid") from e

    if source_name == destination_name:
        return

    with open(source_name, "rb") as source, open(
        destination_name, "wb"
    ) as destination:
        destination.write(source.read())
