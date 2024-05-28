def copy_file(command: str) -> None:
    if len(command.split()) != 3:
        raise ValueError(f"the command should have 3 arguments,"
                         f" got {len(command.split())} instead")
    cmd, source_f, result_f = command.split()
    if cmd != "cp":
        raise TypeError("the command should have 'cp' keyword, "
                        "got '%s' instead" % cmd)

    if source_f == result_f:
        raise TypeError(f"{source_f} and {result_f} are the same file")
    with open(source_f, "r") as source, open(result_f, "w") as result:
        for line in source:
            result.write(line)
