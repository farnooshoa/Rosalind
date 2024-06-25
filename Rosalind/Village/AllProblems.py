#import this

#Variables and Some Arithmetic
a= 821 
b= 878
print (f' {a}^2 + {b}^2 ={a**2+b**2}')

#strings and lists
wordOneStartPos = 66
wordOneEndPos = 76

wordTwoStartPos = 158
wordTwoEndPos = 164

txtStr = "l1fzFgj36YDZuDHrFKYmbs0etLFgyE3e8mdk410Jj4JrDl7BqWK2oXuEkv2OcSnfRwLycaenopsisMdJuX5LvCaDucyO0jZAoVr6tCbpZWV2mxft8FGfJNSV48VrdpOmfmrSQwANLh0jqXIAxuQDTpysj7xzVJcaninus8qPLl3bFI9Xh40ZlqUEfDvT6."

# Note: end position is not inclusive, so we add 1 to capture it
print(
    f'{txtStr[wordOneStartPos:wordOneEndPos + 1]} {txtStr[wordTwoStartPos:wordTwoEndPos + 1]}')

#Conditions and Loops 
startPos = 4790
endPos =  9192
result = 0

for x in range(startPos, endPos + 1):
    if x % 2 != 0:
        result += x

# result = sum(
#     [x for x in range(startPos, endPos + 1) if x % 2 != 0]
# )

print(result)

#Reading and Writing

outputFile = []
with open ('/Users/farnooshoa/Desktop/Rosalind/Rosalind/Village/input.txt', 'r') as f:
    outputFile = [line for pos, line in enumerate 
                  (f.readlines())if pos %2 != 0 ]
with open ('/Users/farnooshoa/Desktop/Rosalind/Rosalind/Village/out.txt', 'w') as f:
   f.write (''.join([line for line in outputFile]))

# Dictionaries
str ="When I find myself in times of trouble Mother Mary comes to me Speaking words of wisdom let it be And in my hour of darkness she is standing right in front of me Speaking words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the broken hearted people living in the world agree There will be an answer let it be For though they may be parted there is still a chance that they will see There will be an answer let it be Let it be let it be let it be let it be There will be an answer let it be Let it be let it be let it be let it be Whisper words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the night is cloudy there is still a light that shines on me Shine until tomorrow let it be I wake up to the sound of music Mother Mary comes to me Speaking words of wisdom let it be Let it be let it be let it be yeah let it be There will be an answer let it be Let it be let it be let it be yeah let it be Whisper words of wisdom let it be"
wordCountDict = {}

for word in str.split(' '):
    if word in wordCountDict:
        wordCountDict[word] += 1
    else:
        wordCountDict [word]= 1
  
# Optimized, Pythonic approach, using collections module:
# wordCoutDict = Counter(txtStr.split(' '))

for key,value in wordCountDict.items():
    print (key, value)