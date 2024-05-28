BUFFER_SIZE = 256


def copy_file(command: str) -> None:
    command, first_path, second_path = command.split(" ")
    if first_path == second_path or command != "cp":
        return
    with (open(first_path, "r") as file_read,
          open(second_path, "w") as file_write):
        buffer = file_read.read(BUFFER_SIZE)
        while buffer:
            file_write.write(buffer)
            buffer = file_read.read(BUFFER_SIZE)
