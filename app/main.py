def copy_file(command: str) -> None:
    list_command = command.split()
    if len(list_command) == 3 and list_command[0] == "cp":
        cp, file, file_new = list_command
        if file != file_new:
            try:
                with (
                    open(file, "r") as file_in,
                    open(file_new, "w") as file_out
                ):
                    content = file_in.read()
                    file_out.write(content)
            except FileNotFoundError:
                print("file not found")
            except Exception as e:
                print(f"An error occurred: {e}")
