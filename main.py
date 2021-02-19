'''
codeWars Kata codewars.com

In this kata we want to convert a string into an integer. 
The strings simply represent the numbers in words.

Examples:
"one" => 1
"twenty" => 20
"two hundred forty-six" => 246
"seven hundred eighty-three thousand nine hundred and nineteen" => 783919
Additional Notes:

The minimum number is "zero" (inclusively)
The maximum number, which must be supported is 1 million (inclusively)
The "and" in e.g. "one hundred and twenty-four" is optional, in some cases it's present and in others it's not
All tested numbers are valid, you don't need to validate them
'''

#SOLUTION

NUMBERS = {
    'zero': 0, 'one': 1, 'two': 2, 'three': 3,
    'four': 4, 'five': 5, 'six': 6, 'seven': 7,
    'eight': 8, 'nine': 9, 'ten': 10, 'eleven': 11,
    'twelve': 12, 'thirteen': 13, 'fourteen': 14,
    'fifteen': 15, 'sixteen': 16, 'seventeen': 17,
    'eighteen': 18, 'nineteen': 19, 'twenty': 20,
    'thirty': 30, 'forty': 40, 'fifty': 50,
    'sixty': 60, 'seventy': 70,  'eighty': 80,
    'ninety': 90, 'hundred': 100, 'thousand': 1000,
    'million': 1000000, 'and': '',
    }

def parseInt(text):
    split_numbers = text.replace("-", " ")
    split_numbers = split_numbers.split(" ")
    
    if "million" in split_numbers:
        return 1000000
    
    total = 0
    group_total = 0
    
    for i, w in enumerate(split_numbers):
        if w == "and":
            continue
        elif w == "hundred":
            group_total = 100 * group_total
        elif w == "thousand":
            group_total = (1000 ** split_numbers.count("thousand")) * group_total
            total += group_total
            group_total = 0
        else:
            group_total += NUMBERS[w]
        
    total += group_total
    return total

print(parseInt("seven hundred eighty-three thousand nine hundred and nineteen"))



#FIRST ATTEMPT (WRONG)
numbers = {
    'zero':0,
    'one':1,
    'two':2,
    'three':3,
    'four':4,
    'five':5,
    'six':6,
    'seven':7,
    'eight':8,
    'nine':9,
    'ten':10,
    'eleven':11,
    'twelve':12,
    'thirteen':13,
    'fourteen':14,
    'fifteen':15,
    'sixteen':16,
    'seventeen':17,
    'eighteen':18,
    'nineteen':19,
    'twenty': 20,
    'thirty': 30,
    'forty': 40,
    'fifty': 50,
    'sixty': 60,
    'seventy': 70,
    'eighty': 80,
    'ninety': 90,
    'hundred': 100,
    'thousand': 1000,
    'million': 1000000,
    'and': ''
    } 

userString = input("Enter a number without using digits (ex: one hundred and twenty-four):\n")
userString = userString.lower()
listLetters=userString.replace('-', ' ').split(' ')
#get rid of hyphens and split into words
print(listLetters) #check on what's going on

listDigits=[]
for item in listLetters:
    a=numbers.get(item) #get values from dict
    listDigits.append(a) #and create a new list with digits
print(listDigits) #check on what's going on

while ("" in listDigits): 
    listDigits.remove("") #remove empty elements from list
print(*listDigits,sep='') #print without white spaces

'''
создание алгоритма
1) убрать все лишнии знаки и разбить на лист который состоит только из слов-цифр, слов thousand и hundred
2) разбить этот лист на список тысячных групп, к примеру
nine hundred and ninety-nine thousand nine hundred and ninety-nine
[nine, hundred, ninety, nine] [nine, hundred, ninety, nine]
в каждой группе посчитать число - следуя моему предыдущему алгоритму
Define two variables:
            total_sum = 0 # stores final number
            partial_sum = 0 # stores a number before we get to a hundred
        Loop through the list:
            If the list element is a number:
                Convert to number, add to partial_sum
            If the list element is a multiplier:
                Multiply the partial_sum by a multiplier and add to total_sum
                Zero out the partial sum
каждую группу умнажаешь на 1000 в степени x где х это количество групп минус номер группы
результат каждой группы
потом все это складываешь
'''
