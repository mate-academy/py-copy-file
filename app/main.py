def copy_file(command: str) -> None:
    comm = command.split()
    if comm[0] == "cp" and comm[1] != comm[2]:
        with (
            open(f"{comm[1]}", "r") as file_in,
            open(f"{comm[2]}", "w") as file_out
        ):
            file_out.write(file_in.read())
