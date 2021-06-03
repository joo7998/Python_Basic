# file mode
#       action: r(read: default), w(write), a(add)
#       type: t(default), b(binary)

def write01():
    f = open("./sample/test.txt", "w", encoding="UTF-8") # write text
    write_size = f.write("Life is too short, you need Python")
    print(write_size)
    f.close();


def write02():
    f = open("./sample/multilines.txt", "w", encoding="UTF-8")
    for i in range(10):
        f.write("Line %d\n" % i)
    f.close()


def read01():
    f = open("./sample/multilines.txt", "r", encoding="UTF-8")
    text = f.read()
    print(text)
    f.close()


def read02():

    f = open("./sample/multilines.txt", "r", encoding="UTF-8")
    while True:
        line = f.readline() # read one line
        if not line:    # if no more to read
            break
        print(line)
    f.close()


def read03():
    # readlines() -> whole list -> convert
    f = open("./sample/multilines.txt", "r", encoding="UTF-8")
    lines = f.readlines()

    for line in lines:
        print(line)
    f.close()


def copy_binary():
    # binary file (to handle) = mode b
    # rose-flower.jpeg -> rose-flower-copy.jpeg (copy)
    f_src = open("./sample/rose-flower.jpeg", "rb") # binary mode
    data = f_src.read()
    print(type(data))
    f_src.close()

    f_dest = open("./sample/rose-flower-copy.jpeg", "wb")   # binary mode
    f_dest.write(data)
    f_dest.close()

import pickle


def pickle_dump():
    with open("./sample/players.bin", "wb") as f:   # to use pickle -> binary
        data = {"baseball": 9}
        pickle.dump(data, f)
    print("dumped!")


def pickle_load():
    # binary data -> python obj (back)
    with open("./sample/players.bin", "rb") as f:
        data = pickle.load(f)
        print(data, type(data))
    print("loaded!")


def pickle_dump_multi():
    # dump method repeat ->  many obj dump (0)
    with open("./sample/players.bin", "wb") as f:
        pickle.dump({"baseball": 9}, f, 1) # protocol ver.1
        pickle.dump({"basketball": 5}, f, pickle.HIGHEST_PROTOCOL) # latest protocol ver
        pickle.dump({"soccer": 11}, f) # if ver not specified -> use the latest

    print("overlap dump!")


def pickle_load_multi():
    # difficult to know no. pickle ojb within the file
    with open("./sample/players.bin", "rb") as f:
        # print(pickle.load(f))
        # print(pickle.load(f))
        # print(pickle.load(f))
        # print(pickle.load(f))
        # loop until EOF error occurs ->load
        data_list = []
        while True:
            try:
                data = pickle.load(f)
            except EOFError:    # no more pickle to read
                break
            data_list.append(data)

        print(data_list)


def slamdunk_read():
    # sangbuk.csv
    # line by line -> dict -> list
    # dump to pickle
    players = []
    with open("./sample/sangbuk.csv", "rt", encoding="utf-8") as f:
        while True:
            line = f.readline()
            if not line:    # no data read
                break
            # data -> dic
            line = line.strip().replace(" ", "")
            info = line.split(",")
            print(info)
            member = { "name": info[0], "backno": info[1], "height": info[2], "position": info[3]}
            # print(info)
            players.append(member)

    print(players)
    # dump -> pickle
    with open("./sample/sangbuk_players.bin", "wb") as f:
        pickle.dump(players, f)

    print("pickle dumped!")


if __name__ == "__main__":
    # write01()
    # write02()
    # read01()
    # read02()
    # read03()
    # copy_binary()
    # using_pickle()
    # pickle_dump()
    # pickle_dump_multi()
    # pickle_load_multi()
    slamdunk_read()