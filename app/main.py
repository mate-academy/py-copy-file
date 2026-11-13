def copy_file(command: str) -> None:
    src_name = command[command.index("cp ") + 1:command.rindex(".txt ")]
    des_name = command[command.rindex(".txt ") + 1:]
    if des_name != src_name:
        with open(src_name, "r") as src, open(des_name, "w") as des:
            content = src.read()
            src.close()
            des.write(content)
            des.close()
