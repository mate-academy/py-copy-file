def copy_file(command: str) -> None | bool:
    command = command.split()[1:]
    input_file, output_file = command[0], command[1]
    if input_file != output_file:
        with (open(input_file, "r") as file_in,
              open(output_file, "w") as file_out):
            file_out.write(file_in.read())
        if open("file.txt").read() == open("new_file.txt").read():
            return True
    return
