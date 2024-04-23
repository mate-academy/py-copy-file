def copy_file(command: str) -> None:
    parts = command.split(" ")
    if len(parts) < 3:
        print("invalid command format")
    else:
        source = parts[1]
        new = parts[2]
        if source == new:
            print(f"source file name:{source} is same to new file name: {new}")
        else:
            with open(source, "r") as src, open(new, "w") as new:
                content = src.read()
                new.write(content)
