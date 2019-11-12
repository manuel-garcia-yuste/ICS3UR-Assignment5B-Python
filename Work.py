#!/usr/bin/env python3

# Created by: Manuel Garcia Yuste
# Created on : October 2019
# This program do a continue statement


def main():
    print("DIVISORS")
    number = int(input("Enter an integer greater than zero: "))

    if number <= 0:
        print("I have asked for an integer greater than zero!")
    else:
        print(f"The dividers of {number} are ", end="")
        for i in range(1, number + 1):
            if number % i == 0:
                print(i, end=" ")


if __name__ == "__main__":
    main()
