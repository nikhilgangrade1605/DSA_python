# s = input('enter the string:')

#level 1
# reverse = s[::-1]

# vowel = 0
# for ch in s:
#     if ch in "aeiou":
#         vowel += 1
    
# length = len(s)

# print(f'reverse:{reverse}')
# print(f"vowels: {vowel}")
# print(f"length:{length}")

# #level2:

# if s == reverse:
#     print("it is a palindrome")
# else:
#     print("not a palindrome")

# check = input("enter the char to check count:")

# count = 0
# for check in s:
#     count = s.count(check)
    
# print(f"Count:{count}")


  
#level 3

N = int(input("enter the number of durations :"))
num = []
for i in range(N):
    durations = int(input(f"enter the {N} durations"))
    num.append(durations)
sum_total = 0
maximum = 0

for i in range(0,len(num)):
    minimum = num[i]
    if num[i] >= maximum:
        maximum = num[i]
    if num[i] <= minimum:
        minimum = num[i]
    sum_total += num[i]

average = sum_total//N

print(f"Sum: {sum_total}")
print(f"Max: {maximum}")
print(f"Min: {minimum}")
print(f"Average: {average}")