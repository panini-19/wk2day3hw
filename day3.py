# ---------- Reversed Strings ----------
# DESCRIPTION:
# Complete the solution so that it reverses the string passed into it.
# 'world'  =>  'dlrow'
# 'thieves'   =>  'seveiht'

# reverse the string
# reverse()
# 

def reverse_string(word):
    new_word = ''
    for letter in word[::-1]:
        new_word += letter
    print(new_word)
reverse_string('thieves')
