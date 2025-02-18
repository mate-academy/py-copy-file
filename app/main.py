def copy_file(command_and_file_names: str) -> None:
    command_and_file_names = command_and_file_names.split()
    if "cp" in command_and_file_names and len(command_and_file_names) == 3:
        source_file = command_and_file_names[1]
        new_file = command_and_file_names[2]
        if source_file != new_file:
            with open(source_file, "r") as source, open(new_file, "w") as new:
                new.write(source.read())
                print(
                    f"Content from the file - {source.name}"
                    f" was copied to the file - {new.name}"
                )
