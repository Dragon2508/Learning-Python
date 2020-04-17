import math as m 
import collections as coll 
import tkinter as tk
import pickle 

def SummBin(a, l):
    num = ''
    for i in range(0,l):
        a *= 2.0
        num += str(m.trunc(a))
        if a >= 1.0:
            a -= 1.0
    return num

class Code:
    code = ''
    text = ''
    words = {}
    dewords = {}

    # Кодирование
    def Encoder(self):
        self.code = '' 
        self.words = {}
        self.dewords = {}
        sum = 0.0
        self.text = Text1.get(1.0, 'end').lower()
        for i in self.text:
            if i not in self.words:
                self.words[i.lower()] = [1, 0, 0, '']
            else:
                self.words[i][0] += 1
        self.words = coll.OrderedDict(sorted(self.words.items(),key = lambda i:i[0])) 
        for i in self.words:
            self.words[i][0] /=  len(self.text)
            self.words[i][1] = self.words[i][0] / 2 + sum
            self.words[i][2] = m.ceil(m.log2(1 / self.words[i][0])) + 1 #
            self.words[i][3] = SummBin(self.words[i][1], self.words[i][2])
            sum += self.words[i][0]
        for i in self.text.lower():
            self.code += self.words[i][3]


    # Декодирование
    def Decoder(self):
        line = ''
        dewords = {}
        for k,i in self.words.items():
            dewords[i[3]] = k
        for i in self.code:
            line += i
            try:
                dewords[line]
            except:
                pass
            else:
                Text3.insert('end', dewords[line])
                line = ''
            
code = Code()

def encod():
    Text2.delete(1.0,'end')
    code.Encoder()
    Text2.insert(1.0, code.code)

def decod():
    Text3.delete(1.0,'end')
    code.Decoder()

form = tk.Tk()
form.wm_title('Алгоритм Гилберта-Мура')
form.wm_resizable(width=False, height=False)

label1 = tk.Label(form, text='Введите текст')
label1.grid(row=0, column=0)

Text1 = tk.Text(form, wrap=tk.WORD, height=10, width=50)
Text1.grid(row=2, column=0)

Text2 = tk.Text(form, wrap=tk.WORD, height=10, width=50)
Text2.grid(row=4, column=0)

Text3 = tk.Text(form, wrap=tk.WORD, height=10, width=50)
Text3.grid(row=6, column=0)

button_cod = tk.Button(form,text = 'Кодировать', height=2, width=15,command = encod)
button_cod.grid(row=3, column=0, pady=15)

button_decode = tk.Button(form,text = 'Декодировать', height=2, width=15,command = decod)
button_decode.grid(row=5, column=0, pady=15)

form.mainloop()
