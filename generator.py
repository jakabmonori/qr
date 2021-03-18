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
import util as util
from PIL import Image
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

    def generate_qr(self, string_length, no_of_codes, url_base, save_location, array, img_path):
        for x in range(int(no_of_codes)):
            img = ""
            rnd_string = ""
            result_string = ""
            logo = Image.open(img_path)
            logo_pos = ""

            #Generating random string via the function
            rnd_string = self.generate_string(int(string_length))
            
            #Concatenating the url_base, a '/' symbol and the rnd_string together, and assigning it to a var
            result_string = url_base + '/' + rnd_string

            #Creating the QR Code itself
            self.qr.add_data(result_string)
            self.qr.make(fit=True)

            #Array Generation
            self.generate_array(x, array, rnd_string)

            #Creating QR Code image with logo in center
            img = self.qr.make_image(fill_color="red", back_color="white").convert('RGB')

            logo = util.resize_image(logo, 100, 100)

            logo_pos = ((img.size[0] - logo.size[0]) // 2, (img.size[1] - logo.size[1]) // 2)
            img.paste(logo, logo_pos)

            if rnd_string == "":
                img.save(save_location + '/' + 'asd' + '.png')
            else:
                img.save(save_location + '/' + rnd_string + '.png')


            #Clearing QR Code for next cycle
            self.qr.clear()
        self.call_exporter(self.exporter_arr)

    """def generate_array():
        exporter_arr"""

    def call_exporter(self, export_arr):
        self.csvgen.write_to_csv(export_arr)

    def generate_array(self, x, array, rnd_string):
        date = self.get_date()
        self.exporter_arr[x] = array[3], rnd_string, array[4], array[5], array[6], array[7], "taxable", "1", "1", "0", "1", "0", array[10], array[8], array[9], "https://qrsystem.hu/wp-content/uploads/" + date + '/' + rnd_string + '.png' 
        return self.exporter_arr

    def get_date(self):
        x = datetime.datetime.now()
        year = x.strftime("%Y")
        month = x.strftime("%m")
        result = year + '/' + month
        return result


            
            



    


