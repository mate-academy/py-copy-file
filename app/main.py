def copy_file(command: str) -> None:
    (
        command,
        first_filename,
        second_filename,
    ) = command.split(" ")
    if command != "cp" or first_filename == second_filename:
        return
    try:
        with (open(first_filename, "r") as source,
              open(second_filename, "w") as copy):
            copy.write(source.read())
    except FileNotFoundError:
        print(f"File not found: {first_filename}")
    except Exception as e:
        print(f"An error occurred: {e}")
