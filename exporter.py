import csv

class csv_generator:

    csv_filename = "teszt"
    csv_headers = ["Azonosító", "Típus", "Cikkszám", "Név", "Közzétéve", "Kiemelt?", "Látható a katalógusban", "Rövid leírás", "Leírás", "Akciós ár kezdődátuma", "Akciós ár végdátuma", "Adó státusz", "Adózási osztály", "Raktáron?", "Készlet", "Alacsony készlet mennyiség", "Függő rendelés engedélyezése?", "Egyedileg értékesíthető?", "Tömeg (kg)", "Hosszúság (cm)", "Szélesség (cm)", "Magasság (cm)", "Engedélyezzük az értékelést?", "Vásárlási megjegyzés", "Akciós ár", "Normál ár", "Kategória", "Címkék", "Szállítási osztály", "Képek", "Letöltési korlát", "Letöltés lejárati napok", "Szülő", "Csoportosított termék", "Upsell", "Keresztértékesítés", "Külső URL", "Gomb Szövege", "Pozíció"]
    csv_headers_s = ["Karakterlánc", "Hossz", "URL"]

    def initialize_csv(self):
        with open(self.csv_filename + ".csv", 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(self.csv_headers)

    def write_to_csv(self):
        with open(self.csv_filename + ".csv", 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["1", "random", "4535345"])

    def test(self, export_arr):
        with open(self.csv_filename + ".csv", 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(self.csv_headers_s)
            for x in range(len(export_arr)):
                writer.writerow([export_arr[x][0], export_arr[x][1], export_arr[x][2]])

csvgen = csv_generator()
