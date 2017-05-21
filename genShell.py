import random as r

f = []


class Symbol:
    def __init__(self, symbol, param):
        self.symbol = symbol
        # self.paname = paname
        self.param = param
        # self.pamap=map()
        # for i in range(len(paname)):
        #     self.pamap[paname[i]]=param[i]

    def __str__(self):
        string = ''
        string += self.symbol + '('
        for key in self.param:
            string += str(key) + ','
        string = string[:len(string) - 1] + ');'
        return string


def generateNextSymbol(symbol, nonterminalQ, terminalQ):
    s = symbol.symbol
    p = symbol.param
    rate = round(r.random(), 1)
    opp = round(r.random(), 1)
    if s == "S":

        x = p[0]
        y = p[1]
        w = p[2]
        h = p[3]
        # print("rate:", rate)
        # print('param:', p)
        if opp < 0.4 or (h - y) <= 20 or w - x <= 20:
            print(1)
            nonterminalQ.append(Symbol('F', [x, y, w, h]))
        elif opp < 0.7:
            print(2)
            nonterminalQ.append(Symbol('S', [x, y, w * rate, h]))
            nonterminalQ.append(Symbol('S', [w * (rate), y, w, h]))
        else:
            print(3)
            nonterminalQ.append(Symbol('S', [x, y, w, h * rate]))
            nonterminalQ.append(Symbol('S', [x, h * (rate), w, h]))
    elif s == 'F':
        f.append(symbol)
        x = p[0]
        y = p[1]
        w = p[2]
        h = p[3]
        terminalQ.append(Symbol('L', [x, y, x, h]))
        terminalQ.append(Symbol('L', [x, y, w, y]))
        terminalQ.append(Symbol('L', [w, y, w, h]))
        terminalQ.append(Symbol('L', [x, h, w, h]))


nonQ = []
terQ = []
generateNextSymbol(Symbol('S', [0, 0, 1000, 1500]), nonQ, terQ)
while(len(nonQ) > 0):
    now = nonQ.pop()
    generateNextSymbol(now, nonQ, terQ)
lang = open('code.txt', 'w')
for s in terQ:
    print(type(str(s)))
    lang.write(str(s))
for s in f:
    print(s)
