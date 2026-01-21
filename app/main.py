def copy_file(source: str, destination: str) -> None:
    with open(source, "r") as first, open(destination, "w") as second:
        if first.name != second.name:
            for line in first:
                second.write(line)
            print("Successfully copied file!")
        else:
            raise Exception("Cannot copy to identical file")
