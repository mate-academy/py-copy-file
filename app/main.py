import os.path


def copy_file(command: str) -> None:
    list_of_files = command.split(" ")

    if len(list_of_files) == 3:

        command = list_of_files[0]
        source = list_of_files[1]
        target = list_of_files[2]

        if (
            target != source
            and command == "cp"
            and os.path.exists(source)
        ):
            with open(source, "r") as out, open(target, "w") as into:
                for line in out:
                    into.write(line)
