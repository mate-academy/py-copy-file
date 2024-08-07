def copy_file(command: str) -> None:
    com, file_name, copy_name = command.split()
    if len(command.split()) == 3 and com == "cp" and file_name != copy_name:
        try:
            with(
                open(file_name, "r") as file_input,
                open(copy_name, "w") as file_output
            ):
                file_output.write(file_input.read())
        except FileNotFoundError:
            print(f"File {file_name} not found.")
