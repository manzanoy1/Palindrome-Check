#Yanira Manzano
#04/02/2020
#Assignment 9: Palindrome Check

user = input("Enter a word: ")

lower = user.lower()
final = lower.strip()


def user_input():
    if PalindromeCheck(final):
        print("That is a palindrome!")
    else:
        print("That is not a palindrome..")


def PalindromeCheck(string):
    if len(string) <= 1:
        return True
    if string[0] == string[len(string) - 1] :
        return PalindromeCheck(string[1:len(string) - 1])


user_input()
