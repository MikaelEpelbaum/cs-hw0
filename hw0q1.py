with open('output.txt', 'w') as f:
    for i in range(1, 25):
        print(i)
        f.write(("{0}\n").format(i))
