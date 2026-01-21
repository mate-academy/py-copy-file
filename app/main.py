from os.path import exists, samefile


def copy_file(command: str) -> None:
    args = command.split(" ")
    if len(args) != 3:
        return
    if args[0] != "cp":
        return

    source_file = args[1]
    target_file = args[2]

    if exists(source_file):
        if exists(target_file):
            if samefile(target_file, source_file):
                return

        with (open(source_file, "r") as source,
              open(target_file, "w") as target):
            for line in source:
                target.write(line)
        return
    return
