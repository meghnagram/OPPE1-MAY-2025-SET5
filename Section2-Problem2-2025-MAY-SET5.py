

n = int(input())
s = "\n".join(input() for i in range(n))

vowels = "aeiou"
vowel_indices = [i for i in range(len(s)) if s[i].lower() in vowels]
s_list = list(s)
n = len(vowel_indices)//2
for i,j in zip(vowel_indices[:n] , vowel_indices[n:][::-1]):
    s_list[i],s_list[j] = s_list[j],s_list[i]

print("".join(s_list))

# #Another Method



# # Write your solution here

# l=[]
# n=int(input())
# while(n!=0):
#     s=input()
#     l.append(s)
#     n=n-1
# m=[]
# for i in l:
#     for index,c in enumerate(i):
#         if c.lower() in ('a','e','i','o','u'):
#             m.append(c)
# r=''
# m=m[::-1]
# for i in l:
#     for index,c in enumerate(i):
#         if c.lower() in ('a','e','i','o','u'):
#                 r=r+m[0]
#                 m=m[1::]
#         else:
#             r=r+c
#     print(r)
#     r=''

# Reverse Vowel Order in a String
# Write a python program that reads a multiline string and reverses only the vowels in the string while keeping all other characters in their original positions.

# Input Format

# First line will have the number of lines (n) in the input
# Next n lines will have the multiline string
# Output Format The modified multiline string.

# Note

# Vowels are considered: a, e, i, o, u (both uppercase and lowercase).
# Non-vowel characters remain in place.
# Case should be preserved while reversing
# Example
# Input: HEllo Output: HollE

