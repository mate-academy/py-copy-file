def copy_file(command: str) -> None:
    intro, outro = command.split(" ")[1:]
    if intro != outro:
        with open(intro, "r") as file_in, open(outro, "w") as file_out:
            file_out.write(file_in.read())
