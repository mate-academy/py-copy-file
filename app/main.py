def copy_file(command: str) -> None:
    if command.startswith("cp ") and len(command.split(" ")) == 3:
        list_of_files = command[3:].split(" ")
        if list_of_files[0] != list_of_files[1]:
            with (open(list_of_files[0], "r") as file_in,
                  open(list_of_files[1], "a") as file_out):
                for line in file_in.readlines():
                    file_out.write(line)
