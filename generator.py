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
from exporter import csv_generator

class Generator:

    str_chars = string.ascii_letters + string.digits

    exporter_arr = [None]

    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_H
    )

    def __init__(self, no_of_codes):
        self.exporter_arr = [None] * int(no_of_codes) 


    def generate_string(self, string_length):
        result_str = ''.join(random.choice(self.str_chars) for i in range(int(string_length)))
        return result_str

    def generate_qr(self, string_length, no_of_codes, url_base, save_location):
        for x in range(int(no_of_codes)):
            img = ""
            rnd_string = ""
            result_string = ""

            rnd_string = self.generate_string(int(string_length))
            
            result_string = url_base + '/' + rnd_string
            print('Created string: ' + result_string)

            self.qr.add_data(result_string)
            self.qr.make(fit=True)

            self.generate_array(x, rnd_string, string_length, result_string)

            img = self.qr.make_image(fill_color="red", back_color="white")
            img.save(save_location + '/' + rnd_string + '.png')
            self.qr.clear()
        print(self.exporter_arr)
        self.call_exporter(self.exporter_arr)

    def generate_array(self, x, rnd_string, string_length, result_string):
        self.exporter_arr[x] = [rnd_string, string_length, result_string]

    def call_exporter(self, export_arr):
        csvgen = csv_generator()
        csvgen.test(export_arr)



    


