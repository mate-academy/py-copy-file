def copy_file(comand: str) -> None:
    comand_split = comand.split(" ")
    try:
        if (
            comand_split[0] == "cp"
            and len(comand_split) == 3
            and comand_split[1] != comand_split[2]
        ):
            with open(comand_split[1], "r") as sorse_file, open(
                comand_split[2], "w"
            ) as copied_file:
                copied_file.writelines(sorse_file.readlines())
    except FileNotFoundError:
        pass
