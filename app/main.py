def copy_file(command: str) -> None:
    command_part = command.split()
    cp, source, target = command_part
    if source == target:
        print("Source and target are the same")

    with open(source, "r") as file_in, open(target, "w") as file_out:
        file_out.write(file_in.read())
