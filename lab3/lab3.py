import re


def calc_fails():
    file = open('log.txt')
    pattern = "10:[0-5][0-9]:[0-5][0-9].*POST.*[4-5][0-9][0-9]"
    total_fails = 0
    for line in file:
        match = re.search(pattern, line)
        if match:
            print(match.group())
            total_fails += 1
    print("Total number of fails = " + str(total_fails))
    file.close()


if __name__ == "__main__":
    calc_fails()