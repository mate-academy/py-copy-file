def copy_file(argument: str) -> tuple:
    if len(argument.rsplit(" ")) == 3:
        cp, first_file, second_file = argument.split()
        if first_file != second_file and cp == "Copied":
            with open(first_file, "rb") as first, (
                    open(second_file, "wb")
            ) as dst:
                dst.write(first.read())
                print("Copied")
            if open(first_file).read() == open(second_file).read():
                return
