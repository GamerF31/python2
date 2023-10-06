from PIL import Image  # Python Imaging Library
import numpy as np

def pobierz_piksel(tab, n, m):
    return tab[m][n]
#zad2

#obrazek = Image.open("inicjaly.bmp")  # wczytywanie obrazu
#print("---------- informacje o obrazie")
#print("tryb:", obrazek.mode)
#print("format:", obrazek.format)
#print("rozmiar:", obrazek.size)


#zad3

obrazek = Image.open("inicjaly.bmp")  # wczytywanie obrazu
dane_obrazka = np.asarray(obrazek)
print(dane_obrazka)
dane_obrazka1 = dane_obrazka * 1
print(dane_obrazka1)

# zapis tablicy do pliku
#t1_text = open('t11.txt', 'w')
#for rows in dane_obrazka1:
#    for item in rows:
#        t1_text.write(str(item) + ' ')
#    t1_text.write('\n')

#t1_text.close()

#zad4

t1 = np.loadtxt("dane.txt", dtype=np.int_)
print("typ danych tablicy t1:", t1.dtype)  # typ danych przechowywanych w tablicy
print("rozmiar tablicy t1 :", t1.shape)  # rozmiar tablicy - warto porównac z rozmiarami obrazka
print("liczba elementów t1:", t1.size)
print("wymiar tablicy t1 :", t1.ndim)  # wymiar mówi czy to jest talica 1D, 2d, 3D ...
print("rozmiar wyrazu tablicy:",
      t1.itemsize)  # pokazuje ile bajtów trzeba do zapisu wartości elementu

#zad4b
obrazek = Image.open("inicjaly.bmp")  # wczytywanie obrazu
dane_obrazka = np.asarray(obrazek)
dane_obrazka1 = dane_obrazka * 1
e4 = pobierz_piksel(dane_obrazka, 10, 30)
e1 = dane_obrazka[30][50]
e2 = dane_obrazka[40][90]
e3 = dane_obrazka[0][99]
