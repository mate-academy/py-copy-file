def copy_file(command: str) -> str | None:
    try:
        cp, original, copy = command.split()
        if original == copy or cp != "cp":
            return (
                "Incorrect command!"
                "Please ensure that the command is in the following format:"
                "'cp file.txt new_file.txt'"
            )
        with open(original, "r") as orig_file, open(copy, "w") as copied_file:
            copied_file.write(orig_file.read())
    except FileNotFoundError as error:
        return f"{error}! File not found"

    except ValueError as error:
        return (
            f"{error}! Incorrect command! "
            f"Please ensure that the command is in the following format: "
            f"'cp file.txt new_file.txt'"
        )
