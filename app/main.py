import shutil


def copy_file(str1: str) -> tuple:
    src_path = str1.rsplit(" ")[1]
    dst_path = str1.rsplit(" ")[2]
    if src_path != dst_path:
        shutil.copy(src_path, dst_path)
        print("Copied")
        if open(src_path).read() == open(dst_path).read():
            print(True)
            try:
                with open(src_path, "r") as src, open(dst_path, "w") as dst:
                    pass
                if src.closed and dst.closed:
                    print("Файли закрито")
                else:
                    print("Файли не закрито")

            except IOError:
                print("Помилка відкриття/закриття файлів")
        else:
            print("файли не однакові")
            print(False)
    else:
        print("файли однакові")
        return


copy_file("Copied file.txt txtа89.txt")
