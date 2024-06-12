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

