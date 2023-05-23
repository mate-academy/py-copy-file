def copy_file(command: str) -> None:
    if len(command.split()) == 3:
        cp, source, replication = command.split()
        if cp == "cp" and source != replication:
            with open(source, "r") as file, open(replication, "w") as copy:
                copy.write(file.read())
