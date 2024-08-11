from errors import InvalidCommandCp, IdenticalFileNames


def copy_file(command: str) -> None:
    copy_info = command.split()

    if len(copy_info) != 3 or copy_info[0] != "cp":
        raise InvalidCommandCp(
            "Command 'cp' is invalid. "
            "This command should look like this : "
            "'cp source_file.txt target_file.txt'"
        )

    _, source_file, target_file = copy_info

    if source_file == target_file:
        raise IdenticalFileNames(
            "The source and target files are identical. "
            "Does nothing."
        )

    with open(source_file, "r") as file_in, open(target_file, "w") as file_out:
        file_out.write(file_in.read())
        print("Copying completed!")
