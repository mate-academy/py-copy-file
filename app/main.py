def copy_file(command: str) -> None:

    if len(command.split()) == 3:
        action, source_file, copied_file = command.split()

        if action == "cp":

            if source_file != copied_file:

                with open(source_file, "r") as source_file, open(
                        copied_file,
                        "w"
                ) as copied_file:
                    copied_file.write(source_file.read())

    return
