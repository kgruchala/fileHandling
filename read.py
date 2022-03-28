def read():
    print("Please, specify the file you would like to read")
    x = input()
    try:
        f = open(x, "r")
        print(f.read())
    except:
        print("Something went wrong with reading the file")
    finally:
        print("Thanks for using read() function")