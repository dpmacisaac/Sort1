import random

def write_file(path: str, arr: [str]) -> None:
    '''
        takes an array of strings and outputs them on newlines in a given file
    '''
    try:
        with open(path, "w") as file:
            for item in arr:
                file.write(str(item) + "\n")
    except:
        pass

rand_strings = []
for i in range(10000):
    l = random.randint(1,200)
    s = ""
    for j in range(l):
        t = (random.randint(1,255))
        if t != 10:
            s+=(chr(t))
    rand_strings.append(s)

write_file("test.txt",rand_strings)

