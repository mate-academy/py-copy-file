def copy_file(command: str) -> None:
    name_massive = command.split(" ")
    if name_massive[1] != name_massive[2]:
        with (open(name_massive[1], "r") as file_in,
              open(name_massive[2], "w") as file_out):
            file_out.write(file_in.read())
