def copy(command: str) -> None:
    cmd, current_file, future_file = command.split()
    if current_file != future_file or cmd == "cp":
        with (open(current_file, "r") as file_in,
              open(future_file, "w") as file_out):
            file_out.write(file_in.read())
