from this import s

Word = 'Word2'
Words = ['word1', 'word2', 'word3']
for i in Words:
    if Word == i:
        print('Слово найдено')

print('The Hilton'.istitle()) #=> True
print('The dog'.istitle()) #=> False
print('sticky rice'.istitle()) #=> False

sentence = 'The Cat in the Hat'
sentence.lower() #=> 'the cat in the hat'
print(sentence.lower())

import re
def text_match(text):
        patterns = '^[a-zA-Z0-9_]*$'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(text_match("The Cat in the Hat."))
print(text_match("Python_Exercises_1"))

# import library
import re

print(bool(re.match("^[A-Za-z0-9_-]*$",
                    'ValidString12-_')))

print(bool(re.match("^[A-Za-z0-9_-]*$",
                    'inv@lidstring')))
# import library
import re

# make a pattern
pattern = "^[A-Za-z0-9_-]*$"

# input
string = "G33ks_F0r_Geeks"

# convert match object
# into boolean values
state = bool(re.match(pattern, string))

print(state)









import re

# [abc] - [a-zA-z]
# \d - [0-9]
# \D - [^0-9]
# \s - [\n\t]
# \S - [^\n\t]
# \w - [a-zA-Z0-9]
# \W - [^a-zA-Z0-9]
# * - >=0 matches
# + - >=1 matches
# ? - 0-1 matches
# {n} - n matches
# | - or
# $ - if string end with this pattern
# . - [^\n]



s="[example (.com), github (.com), stackoverflow (.com)]"
import re
s1=re.sub("[(.com)]","",s)
print (s1)

first_string="example ,\ngithub ,\nstackoverflow"
string_cp = first_string.replace(',',"",)
print(string_cp)










name = 'АлександровДенисПетрович'

result = name[0]
for letter in name[1:]:
    if letter.isupper():
        result += f' {letter}'
    else:
        result += letter

print(result)

s = 'АлександровДенисПетрович'

print(''.join(s[j]if j not in[i for i in range(len(s))if s[i]!=s.lower()[i]] else ' '+s[j]for j in range(len(s))).lstrip())


import re
def capital_words_spaces(str1):
  return re.sub(r"(\w)([A-Z])", r"\1 \2", str1)

print(capital_words_spaces("Python"))
print(capital_words_spaces("PythonExercises"))
print(capital_words_spaces("PythonExercisesPracticeSolution"))

import re


def putSpace(input):
    # regex [A-Z][a-z]* means any string starting
    # with capital character followed by many
    # lowercase letters
    words = re.findall('[A-Z][a-z]*', input)

    # Change first letter of each word into lower
    # case
    for i in range(0, len(words)):
        words[i] = words[i][0].lower() + words[i][1:]
    print(' '.join(words))


# Driver program
if __name__ == "__main__":
    input = 'BruceWayneIsBatman'
    putSpace(input)

