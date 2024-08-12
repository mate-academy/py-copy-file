def copy_file(command: str) -> None:

    if (len(command.split()) == 3
            and command.split()[1] != command.split()[2]
            and command.split()[0] == "cp"):

        try:
            with (
                open(command.split()[1], "r") as first_file,
                open(command.split()[2], "w") as second_file
            ):
                second_file.write(first_file.read())
        except OSError as e:
            print(f"Error {e}")
