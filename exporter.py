import csv

class csv_generator:

    csv_filename = "teszt"
    csv_headers = ["Típus", "Név", "Közzétéve", "Látható", "Rövid leírás", "Leírás",  "Adó státusz", "Raktár", "Készlet", "Függő rendelés engedélyezése", "Egyedileg értékesíthető", "Értékelés", "Normál ár", "Kategória", "Címkék", "Képek"]
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
        with open(self.csv_filename + ".csv", 'w', newline='', encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(self.csv_headers_s)
            for x in range(len(export_arr)):
                writer.writerow([export_arr[x][0], export_arr[x][1], export_arr[x][2]])

csvgen = csv_generator()
