def copy_file(command: str) -> None:

    split_com = command.split()

    cp, source_file, destination_file = split_com

    if (len(split_com) == 3
            and source_file != destination_file
            and cp == "cp"):

        try:
            with (open(source_file, "r") as old_file,
                  open(destination_file, "w") as new_file):
                new_file.write(old_file.read())
        except Exception as e:
            print(e)
