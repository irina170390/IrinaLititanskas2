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






import re

txt = "example (.com)", "github (.com)", "stackoverflow (.com)"
out = re.sub(r'\([^)]*\([^)]*\([^)]', '', txt)
print(out)

my_string = "example (.com)", "github (.com)", "stackoverflow (.com)"#input()

a=my_string.find('(')
b=my_string.find(')')

result_string = my_string[0:a] + my_string[b+1:len(my_string)]
print(result_string)













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