def copy_file(command: str) -> None:
    command, name_firs_file, name_copy_file = command.split()
    if name_firs_file != name_copy_file:
        with (
            open(
                f"{name_firs_file}", "r"
            ) as first_file,
            open(
                f"{name_copy_file}", "w"
            ) as copy_file
        ):
            copy_file.write(first_file.read())
