import requests
import datetime
from pytz import timezone
from datetime import datetime

def get_time_info_by_ip(ip_address):
    try:
        # Add User-Agent header to mimic a web browser
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        # Використовуємо API ipapi.co для отримання інформації про час за IP
        response = requests.get(f"https://ipapi.co/{ip_address}/json/", headers=headers)
        response.raise_for_status()  # Перевіряємо на помилки HTTP
        
        data = response.json()
        
        if not data.get('error'):
            timezone_str = data.get('timezone', 'UTC')
            
            # Отримуємо поточний час для знайденої часової зони
            tz = timezone(timezone_str)
            current_datetime = datetime.now(tz)
            
            # Отримуємо день року
            day_of_year = current_datetime.timetuple().tm_yday
            
            # Виводимо результати
            print("\nРезультати:")
            print(f"IP-адреса: {ip_address}")
            print(f"Часовий пояс: {timezone_str}")
            print(f"Поточна дата та час: {current_datetime.strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"День у році: {day_of_year}")
        else:
            print("Помилка:", data.get('reason', 'Невідома помилка'))
    except requests.exceptions.RequestException as e:
        print(f"Помилка при виконанні запиту: {e}")
    except Exception as e:
        print(f"Сталася помилка: {e}")


print("Введіть IP-адресу для отримання інформації про час (наприклад, 8.8.8.8):")
ip = input().strip()
get_time_info_by_ip(ip)