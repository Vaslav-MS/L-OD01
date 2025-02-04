def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

user_input = input("Введите строку: ")
print("Это палиндром!" if is_palindrome(user_input) else "Это не палиндром!")
