def copy_file(command: str) -> None:
    data = command.split()
    if len(data) == 3:
        cmd, file_in, file_out = data

        if cmd == "cp" and file_in != file_out:
            try:
                with open(file_in, "r") as source, open(
                    file_out, "w"
                ) as destination:
                    content = source.read()
                    destination.write(content)
            except FileNotFoundError:
                print("The source file was not found in working directory")
