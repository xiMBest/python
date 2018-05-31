import sys

number = []
firstargument = 0

if __name__ == "__main__":
    result = int(input("Enter number: " + "\n"))

    for secondargument in range(result):
        number.append(0)

    secondargument = 0

    for thirthargument in range(2 ** result):

        print(number)
        secondargument += 1
        firstargument = 0
        forthargumnet = secondargument

        while (forthargumnet % 2 == 0):
            forthargumnet /= 2
            firstargument += 1

        if firstargument < result:
            number[firstargument] = 1 - number[firstargument]

    pass