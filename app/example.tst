def copy_file(cp_cmd: str) -> None:
    arg = cp_cmd.split(" ")
    if arg[0] != "cp" or arg[1] == arg[2]:
        return
    with open(arg[1], "r") as fin, open(arg[2], "w") as fout:
        content = fin.read()
        fout.write(content)


# =====
copy_file("cp main.py example.tst")
