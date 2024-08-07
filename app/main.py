def copy_file(command: str) -> None:
    comm, file_name, copy_name = command.split()
    if len(command.split()) == 3 and comm == "cp" and file_name != copy_name:
        try:
            with (
                open(file_name, "r") as file_in,
                open(copy_name, "w") as file_out
            ):
                file_out.write(file_in.read())
        except FileNotFoundError:
            print(f"File {file_name} not found")
