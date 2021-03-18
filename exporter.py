import csv

class csv_generator:

    csv_filename = "teszt"
    csv_headers = ["Típus", "Név", "Közzétéve", "Látható a katalógusban", "Rövid leírás", "Leírás",  "Adó státusz", "Raktáron?", "Készlet", "Függő rendelés engedélyezése?", "Egyedileg értékesíthető?", "Engedélyezzük az értékelést?", "Normál ár", "Kategória", "Címkék", "Képek"]
    csv_headers_s = ["Karakterlánc", "Hossz", "URL"]

    def write_to_csv(self, export_arr):
        with open(self.csv_filename + ".csv", 'w', newline='', encoding="utf-8-sig") as file:
            writer = csv.writer(file)
            writer.writerow(self.csv_headers)
            writer.writerows(export_arr)

csvgen = csv_generator()
