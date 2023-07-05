def copy_file(argument: str) -> tuple:
    if len(argument.rsplit(" ")) == 3:
        cmd, source_path, destination_path = argument.split()
        if source_path != destination_path and cmd == "Copied":
            with open(source_path, "rb") as src, (
                    open(destination_path, "wb")
            ) as dst:
                dst.write(src.read())
                print("Copied")
            if open(source_path).read() == open(destination_path).read():
                return
