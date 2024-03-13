#Useful when 2 characters are not same
# X = "abd"
# Y = "bcc"
# c = 0
# for i in X:
#     for j in Y:
#         if i == j:
#             c = c + 1

# if c == len(X):
#     print("Anagram")
# else:
#     print("Not anagram")



#what if abb and abc (in this it should not be anagram but above program will count it as anagram)
    


'''another way is SORTING'''
X = "abd"
Y = "dba"

res = sorted(X)
res1 = sorted(Y)

# res = ''.join(sorted(X))
# res1 = ''.join(sorted(Y))

if res == res1:
    print("Anagram")
else:
    print("Not")






