def copy_file(command: str) -> None:
    all_files = command.split(" ")

    if all_files[0] is "cp":

        if all_files[1] != all_files[2]:
            with (open(all_files[1], "r") as first_file,
                  open(all_files[2], "w") as second_file):
                second_file.write(first_file.read())
