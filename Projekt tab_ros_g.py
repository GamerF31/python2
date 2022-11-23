class tab_ros_g:
    pojemnosc: int
    zajetosc: int
    dane: list[str]

    def __init__(self,dane=[None,None]):

        self.dane = dane
        self.zajetosc = 0
        self.pojemnosc=2

    def ustal(self,idx:int,wartosc:any):
        if self.zajetosc<idx+1:
            self.zajetosc=idx+1

        while self.pojemnosc<self.zajetosc:
            self.pojemnosc *= 2

        for i in range(self.pojemnosc-len(self.dane)):
            self.dane.append(None)

        for i in range(self.zajetosc):
            if self.dane[i] is None:
                self.dane[i]=''
            self.dane[idx]=wartosc


    def pobierz(self,idx: int)->str:
        if idx>len(self.dane):
            return "puste"
        return self.dane[idx]
    def dodaj_za_koniec(self,wartosc: any):
        if self.zajetosc<self.pojemnosc:
            self.dane.insert(self.zajetosc,wartosc)
            self.dane.pop(-1)
            self.zajetosc+=1
        elif self.zajetosc==self.pojemnosc:
            self.pojemnosc=2
            for i in range(self.pojemnosc - len(self.dane)-1):
                self.dane.append(None)
            self.dane.insert(self.zajetosc, wartosc)
            self.zajetosc+=1
    def wstaw_przed(self,idx:int,wartosc:any):
        if self.zajetosc<self.pojemnosc:
            self.dane.insert(idx,wartosc)
            self.dane.pop(-1)
            self.zajetosc+=1
        elif self.zajetosc==self.pojemnosc:
            self.pojemnosc*=2
            for i in range(self.pojemnosc - len(self.dane)-1):
                self.dane.append(None)
            self.dane.insert(idx, wartosc)
            if self.zajetosc < idx:
                self.zajetosc = idx
            else:
                self.zajetosc+=1
        for i in range(self.zajetosc):
            if self.dane[i] is None:
                self.dane[i]=''
                self.zajetosc+=1

    def uprosc(self):
        while self.pojemnosc/2>self.zajetosc:
            x = self.pojemnosc-self.pojemnosc/2
            for i in range(int(x)):
                self.dane.pop(-1)
            self.pojemnosc/=2

    def find_min_index(self, lst, start):
        i = start
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[i]:
                i = j
        return i

    def sortuj(self):
        temp = []
        for i in range(len(self.dane)):
            if isinstance(self.dane[i], int):
                temp.append(self.dane[i])
                self.dane[i] = ''
        print(f'temporary: {temp}')
        for i in range(len(temp)):
            idx_of_minimum = self.find_min_index(temp, i)
            temp[i], temp[idx_of_minimum] = temp[idx_of_minimum], temp[i]


        del self.dane[0:len(temp)]
        self.dane = temp + self.dane
        return self.dane




    def print(self):
        for i in range(len(self.dane)):
            if self.dane[i] is not None:
                if self.dane[i]=='':
                    print(';',end=' ')
                else:
                    print(f'{self.dane[i]}',end=' ')