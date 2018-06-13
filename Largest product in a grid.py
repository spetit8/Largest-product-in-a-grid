import pyperclip

def MultVert(Input, MaxProd):
    for i in range(len(Text) - 3):
        for j in range(len(Text[i])):
            Prod = Text[i][j]*Text[i+1][j]*Text[i+2][j]*Text[i+3][j]
            if Prod > MaxProd:
                MaxProd = Prod
    return MaxProd


def MultHoriz(Input, MaxProd):
    for i in range(len(Text)):
        for j in range(len(Text[i]) - 3):
            Prod = Text[i][j]*Text[i][j+1]*Text[i][j+2]*Text[i][j+3]
            if Prod > MaxProd:
                MaxProd = Prod
    return MaxProd
    
def MultDiag(Input, MaxProd):
    for i in range(len(Text) - 3):
        for j in range(len(Text[i]) - 3):
            Prod = Text[i][j]*Text[i+1][j+1]*Text[i+2][j+2]*Text[i+3][j+3]
            if Prod > MaxProd:
                MaxProd = Prod
            Prod = Text[i+3][j]*Text[i+2][j+1]*Text[i+1][j+2]*Text[i][j+3]
            if Prod > MaxProd:
                MaxProd = Prod
    return MaxProd

Text = pyperclip.paste().split('\r\n')
MaxProd = 0

for x in range(len(Text)):
    Text[x] = Text[x].split()
    Text[x] = list(map(int, Text[x]))

MaxProd = MultVert(Text, MaxProd)
MaxProd = MultHoriz(Text, MaxProd)
MaxProd = MultDiag(Text, MaxProd)
print(MaxProd)

