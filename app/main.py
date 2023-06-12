def copy_file(command: str) -> None:
    source, target = command.split()[1:]

    if source != target:
        with open(source) as file_in, open(target, "w") as file_out:
            for line in file_in:
                file_out.write(line)
