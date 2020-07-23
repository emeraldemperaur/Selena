import random
import string

import core.preferences.corepreferences as selenapreferences
import core.preferences.log_manager as selena_logger


class selenaUtils(object):
    def __init__(self):
        self._selena_log_listener = selena_logger.selenaLogger()
        self.selena_preference = selenapreferences.fetch_core_preferences()
        self.f_name_index = random.randint(0, 4)
        self.l_name_index = random.randint(0, 4)
        self.address_index = random.randint(0, 6)
        self.map_index = random.randint(0, 1)
        self.m_prefix_names = ["John", "Jose", "Remy", "Meka", "Toshi"]
        self.f_prefix_names = ["Jane", "Pamela", "Danielle", "Ada", "Nisha"]
        self.suffix_names = ["Smith", "Nakamura", "Bourne", "Cartier", "Tesla"]
        self.address_names = ["Seymour", "Empiaur", "Main", "Chapel", "Evergreen", "Wisteria", "Square One"]
        self.address_types = ["Street", "Avenue", "Drive", "Crescent", "Boulevard", "Terrace", "Lane"]
        self.region_map = {"NAmerica": ["Canada", "Mexico"],
                           "SAmerica": ["Brazil", "Argentina"],
                           "Europe": ["France", "Netherlands"],
                           "NAfrica": ["Morocco", "Algeria"],
                           "WAfrica": ["Nigeria", "Ghana"],
                           "EAfrica": ["Ethiopia", "Kenya"],
                           "SAfrica": ["South Africa", "Angola"]
                           }
        self.province_map = {"NAmerica": ["British Columbia", "Quintana Roo"],
                             "SAmerica": ["Santa Catarina", "Buenos Aires"],
                             "Europe": ["Île-de-France", "Drenthe"],
                             "NAfrica": ["Casablanca-Settat"],
                             "WAfrica": ["Lagos", "Ashanti"],
                             "EAfrica": ["Oromia", "Nairobi"],
                             "SAfrica": ["Gauteng", "Luanda"]
                             }
        self.city_map = {"NAmerica": ["Vancouver", "Cancún"],
                         "SAmerica": ["Florianópolis", "La Plata"],
                         "Europe": ["Paris", "Assen"],
                         "NAfrica": ["Casablanca", "Algiers"],
                         "WAfrica": ["Lagos", "Kumasi"],
                         "EAfrica": ["Addis Ababa", "Nairobi"],
                         "SAfrica": ["Johannesburg", "Luanda"]
                         }
        self.postal_code_map = {"NAmerica": ["V6B 1B4", "77500"],
                                "SAmerica": ["88000-000", "B1900"],
                                "Europe": ["75000", "9401"],
                                "NAfrica": ["20240", "16000"],
                                "WAfrica": ["105102", "00000"],
                                "EAfrica": ["1000", "00100"],
                                "SAfrica": ["2000", "46703"]}
        self.random_source = string.ascii_letters + string.digits + string.punctuation
        self.f_name = None

    def username_generator(self, gender=None, name_length=None):
        f_name_index = self.f_name_index
        l_name_index = self.l_name_index
        l_name = self.suffix_names[l_name_index]
        if gender:
            if gender.lower() == "female":
                self.f_name = self.f_prefix_names[f_name_index]
        elif gender is None:
            self.f_name = self.m_prefix_names[f_name_index]
        if name_length is None:
            user_name = f"{l_name}.{self.f_name}"
            alt_user_name = f"{self.f_name}.{l_name}"
            _selena_output_ = f"-->| Generated Mannequin username: '{user_name}'/'{alt_user_name}'"
            if self.selena_preference['narrator'] == "enabled":
                print(_selena_output_)
            self._selena_log_listener.info(_selena_output_)
            # if name_length is None, returns list w/ username[0] and alt username[1]
            return user_name, alt_user_name
        elif name_length:
            if name_length is not int:
                name_length = 6
            raw_name = f"{self.f_name}{l_name}"
            user_name = raw_name[0:name_length]
            _selena_output_ = f"-->| Generated (Minimum {str(name_length)}) Mannequin username: '{user_name}'"
            if self.selena_preference['narrator'] == "enabled":
                print(_selena_output_)
            self._selena_log_listener.info(_selena_output_)
            # if name_length argument provided, returns username of specified length
            return user_name

    def alphanum_password_generator(self):
        password = random.choice(string.ascii_lowercase)
        password += random.choice(string.ascii_uppercase)
        password += random.choice(string.digits)
        password += random.choice(string.punctuation)
        for i in range(6):
            password += random.choice(self.random_source)
        raw_password = list(password)
        random.SystemRandom().shuffle(raw_password)
        password = ''.join(raw_password)
        _selena_output_ = f"-->| Generated Alphanumeric Mannequin password: '{password}'"
        if self.selena_preference['narrator'] == "enabled":
            print(_selena_output_)
        self._selena_log_listener.info(_selena_output_)
        return password

    def address_generator(self, geo_region):
        region_list = ["NAmerica", "SAmerica", "Europe", "NAfrica", "WAfrica", "EAfrica", "SAfrica"]
        # region argument
        street_number = random.randint(0, 100)
        address_map_index = self.map_index
        address_index = self.address_index
        address_name = self.address_names[address_index]
        address_type = self.address_types[address_index]
        country = self.region_map[geo_region][address_map_index]
        province = self.province_map[geo_region][address_map_index]
        city = self.city_map[geo_region][address_map_index]
        postal_code = self.postal_code_map[geo_region][address_map_index]
        # returns list with address elements: street#[0], address_name[1], address_type[2], city[3], province[4],
        # country[5], postal_code[6]
        address_list = [street_number, address_name, address_type, city, province, country, postal_code]
        _selena_output_ = f"-->| Generated Mannequin Address: '{address_list}'"
        if self.selena_preference['narrator'] == "enabled":
            print(_selena_output_)
        self._selena_log_listener.info(_selena_output_)
        return address_list


utility_belt = selenaUtils()
username_a = utility_belt.username_generator()
username_b = utility_belt.username_generator("female")
username_c = utility_belt.username_generator(None, "three")
username_d = utility_belt.username_generator("female", 9)
username_a1 = username_a[0]
username_a2 = username_a[1]
username_b1 = username_b[0]
username_b2 = username_b[1]
password_test = utility_belt.alphanum_password_generator()
password_test_b = utility_belt.alphanum_password_generator()
address_test = utility_belt.address_generator("NAmerica")
print(username_a)
print(username_b)
print(username_c)
print(username_d)
print(username_a1)
print(username_a2)
print(username_b1)
print(username_b2)
print(password_test)
print(password_test_b)
print(address_test)
