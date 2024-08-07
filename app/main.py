class SameNamesError(Exception):
    pass


class NotRightCommand(Exception):
    pass


def copy_file(command: str) -> None:
    if len(command.split()) == 3:
        try:
            command, source_file, destination_file = command.split()
            if command != "cp":
                raise NotRightCommand("Incorrect command")
            if source_file == destination_file:
                raise SameNamesError("File names are the same!")

            with (
                open(
                    f"{source_file}", "r"
                ) as first_file,
                open(
                    f"{destination_file}", "w"
                ) as copy_file
            ):
                copy_file.write(first_file.read())
        except SameNamesError as e:
            print(e)
        except NotRightCommand as e:
            print(e)
