#
#
#
# For some reason (probably an easy one) I have to convert every variable to int at the for loops (the "range(var)" part)
#
#
#

import string
import random
import qrcode
import datetime
from exporter import csv_generator

class Generator:

    csvgen = csv_generator()

    str_chars = string.ascii_letters + string.digits

    exporter_arr = [[None]] * 10

    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_H
    )

    def __init__(self, no_of_codes):
        self.exporter_arr = [None] * int(no_of_codes) 


    def generate_string(self, string_length):
        result_str = ''.join(random.choice(self.str_chars) for i in range(int(string_length)))
        return result_str

    def generate_qr(self, string_length, no_of_codes, url_base, save_location, array):
        for x in range(int(no_of_codes)):
            img = ""
            rnd_string = ""
            result_string = ""

            rnd_string = self.generate_string(int(string_length))
            
            result_string = url_base + '/' + rnd_string
            print('Created string: ' + result_string)

            self.qr.add_data(result_string)
            self.qr.make(fit=True)

            self.generate_array(x, array, rnd_string)

            img = self.qr.make_image(fill_color="red", back_color="white")
            img.save(save_location + '/' + rnd_string + '.png')
            self.qr.clear()
        print(self.exporter_arr)
        self.call_exporter(self.exporter_arr)

    """def generate_array():
        exporter_arr"""

    def call_exporter(self, export_arr):
        self.csvgen.test(export_arr)

    def generate_array(self, x, array, rnd_string):
        date = self.get_date()
        self.exporter_arr[0][x] = [[array[3], rnd_string, array[4], array[5], array[6], array[7], "taxable", "1", "1", "0", "1", "0", array[10], array[8], array[9], "https://qrsystem.hu/wp-content/uploads/" + date + '/' + rnd_string + '.png' ]]
        return self.exporter_arr

    def get_date(self):
        x = datetime.datetime.now()
        year = x.strftime("%H")
        month = x.strftime("$m")
        result = year + '/' + month + '/'
        return result


            
            



    


