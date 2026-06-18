s = input('enter the string:')


reverse = s[::-1]

# vowel = 0
# for ch in s:
#     if ch in "aeiou":
#         vowel += 1
    
# length = len(s)

# print(f'reverse:{reverse}')
# print(f"vowels: {vowel}")
# print(f"length:{length}")

# #level2:

if s == reverse:
    print("it is a palindrome")
else:
    print("not a palindrome")

check = input("enter the char to check count:")

count = 0
for check in s:
    count = s.count(check)
    
print(f"Count:{count}")
  
