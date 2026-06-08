def copy_file(command: str) -> None:
    try:
        cm, file_in, new_file = command.split(" ")
    except ValueError:
        return
    if file_in != new_file and cm == "cp":
        try:
            with (open(file_in, "r") as file_in,
                  open(new_file, "w") as file_out):
                file_out.write(file_in.read())
        except FileNotFoundError:
            return
