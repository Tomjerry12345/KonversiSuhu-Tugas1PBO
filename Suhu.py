class Suhu():
    def __init__(self , suhu):
        self.suhu = suhu

    def menu(self):
        print("Input Pilihan Konversi Celcius : ")
        print("1.Celcius Ke Reamur")
        print("2.Celcius Ke Fahrenheit")
        print("3.Celcius Ke Kelvin")

    def celciusReamur(self , r):
        hasil = (5/4) * float(r)
        print("Hasil Konversi Celcius Ke Reamur : " , hasil)

    def celciusFahrenheit(self , f):
        hasil = (5/9) * (float(f)-32)
        print("Hasil Konversi Celcis Ke Fahrenheit : ", hasil)

    def celciusKelvin(self , k):
        hasil = int(k)- 273
        print("Hasil Konversi Celcius Ke Kelvin : ", hasil)

def main():
    suhu = input("Input Suhu Celcius: ")
    celcius = Suhu(suhu)
    celcius.menu()
    pilih = input("Input Pilihan :")
    if (int(pilih) == 1):
        celcius.celciusReamur(suhu)
    elif(int(pilih) == 2):
        celcius.celciusFahrenheit(suhu)
    elif (int(pilih) == 3):
        celcius.celciusKelvin(suhu)

main()