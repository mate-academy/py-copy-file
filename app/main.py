def copy_file(command: str) -> None:
    if len(command.split()) != 3:
        raise TypeError(f"the command should have 3 arguments,"
                        f" got {len(command.split())} instead")
    if "cp" not in command.split():
        raise TypeError("the command should have 'cp' keyword, "
                        "got '%s' instead" % command.split()[0])
    source_f, result_f = command.split()[1], \
        command.split()[2]
    if source_f == result_f:
        raise TypeError(f"{source_f} and {result_f} are the same file")
    else:
        with open(source_f, "r") as source, open(result_f, "w") as result:
            for line in source:
                result.write(line)
