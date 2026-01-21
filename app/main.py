def copy_file(command: str) -> None:
    if len(command.split()) == 3:
        cmd, file_name, file_cp = command.split()
        if file_name != file_cp and cmd == "cp":
            try:
                with (open(file_name, "r") as file_in,
                      open(file_cp, "w") as file_out):
                    file_out.write(file_in.read())
            except FileNotFoundError:
                print(f"Error: {file_name} not found")
    return
