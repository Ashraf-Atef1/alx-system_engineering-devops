with open("./rockyou.txt", "r") as r_file:
    with open("./output.txt", "w") as w_file:
        for line in r_file:
            if len(line) == 12:
                w_file.write(line)
