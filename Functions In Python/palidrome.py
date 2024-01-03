word = "abcdeedcba"
length = len(word)

palindrome_flag = True
for i in range(length):
  if word[i] != word[length-i-1]:
    palindrome_flag = False
    break

if(palindrome_flag):
  print("Word is palindrome")
else:
  print("Word is not a palindrome")
