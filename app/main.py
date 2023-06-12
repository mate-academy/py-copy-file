def copy(command: str) -> None:
    cmd, current, future = command.split()
    if current != future or cmd == "cp":
        with open(current, "r") as file_in, open(future, "w") as file_out:
            file_out.write(file_in.read())
