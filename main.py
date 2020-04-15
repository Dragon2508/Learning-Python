import math as m # математические функции
import collections as coll # подсчёт неичсисляемых обектов

def SummBin(a, l):
    num = ''
    for i in range(0,l):
        a *= 2.0
        num += str(m.trunc(a))
        if a >= 1.0:
            a -= 1.0
    return num

class Code:
    text = ''
    code = ''
    words = {}
    dewords = {}

    # Кодирование
    def Encoder(self): 
        sum = 0.0
        for i in self.text:
            if i not in self.words:
                self.words[i.lower()] = [1, 0, 0, '']
            else:
                self.words[i][0] += 1
        self.words = coll.OrderedDict(sorted(self.words.items(),key = lambda i:i[0])) # Сортировка словаря с сохранением значения ключа
        for i in self.words:
            self.words[i][0] /=  len(self.text)
            self.words[i][1] = self.words[i][0] / 2 + sum
            self.words[i][2] = m.ceil(m.log2(1 / self.words[i][0])) + 1 #Ceil округление до большего целого
            self.words[i][3] = SummBin(self.words[i][1], self.words[i][2])
            sum += self.words[i][0]
        for i in self.text.lower():
            self.code += self.words[i][3]
        print(self.code)

    # Декодирование
    def Decoder(self):
        for k, i in self.words.items():
            self.dewords[i[3]] = k 
        w = ''
        for i in self.code:
            try:
                w += i
                print(self.dewords[w], end='')
                w = ''
            except:
                pass
            
code = Code()
code.text = input('Input phrase or word: \n')
print('Encoded information: ')
code.Encoder()
print('Decoded information: ')
code.Decoder()
s = 0.0
H = 0.0
for i in code.text.lower():
    s += code.words[i][0] * code.words[i][2]
    H += code.words[i][0] * m.log2(1 / code.words[i][0])
print('\nComparison: \n', s,' < ', H+2)