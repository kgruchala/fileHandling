def copy():
    import datetime, shutil, os
    from pathlib import Path

    source_path = r"C:\Users\kamil\Desktop\Nowy folder"
    x = datetime.datetime.now()
    x = str(x.year)
    destination = "G:\\try\\" + x + "\\"
    if len(os.listdir(source_path)) == 0:
        print("Directory is empty, nothing to copy. Closing")
    else:
        try:
            for src_file in Path(source_path).glob('*.*'):
                shutil.move(src_file, destination)
            print("udało się")
        except:
            print("coś poszło nie tak, sprawdź zawartość folderów")
        finally:
            print("koniec przenoszenia")