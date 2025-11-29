# -*- coding: utf-8 -*-
"""
VESPERA Banner Modülü
Platform bağımsız, her cihazda çalışır
"""

import time
import sys
import os


try:
    from colorama import Fore, Style, init as colorama_init
    colorama_init(autoreset=True, strip=False)
    COLORAMA_AVAILABLE = True
except ImportError:
    COLORAMA_AVAILABLE = False
    class Fore:
        GREEN = ''
        CYAN = ''
        YELLOW = ''
        RED = ''
        RESET = ''
    class Style:
        RESET_ALL = ''

def safe_print(text, color='', end='\n'):
    """Güvenli yazdırma - encoding sorunlarını önler"""
    try:
        if COLORAMA_AVAILABLE:
            print(color + text + Fore.RESET, end=end)
        else:
            print(text, end=end)
    except UnicodeEncodeError:
        try:
            text = text.encode('ascii', 'ignore').decode('ascii')
            print(text, end=end)
        except:
            print("", end=end)
    except:
        print(text, end=end)

def typing_effect(text, color='', delay=0.03):
    """Yazı yazıyormuş gibi efekt"""
    try:
        for char in text:
            safe_print(char, color, end='')
            sys.stdout.flush()
            time.sleep(delay)
        print()
    except:
        safe_print(text, color)

def create_vespera_banner():
    """Gelişmiş tablolu VESPERA banner - encoding güvenli"""
    
    try:
        banner = f"""
{Fore.GREEN if COLORAMA_AVAILABLE else ''}╔═══════════════════════════════════════════════════════════════════════════════╗
{Fore.GREEN if COLORAMA_AVAILABLE else ''}║                                                                               ║
{Fore.GREEN if COLORAMA_AVAILABLE else ''}║  {Fore.CYAN if COLORAMA_AVAILABLE else ''}██╗   ██╗{Fore.GREEN if COLORAMA_AVAILABLE else ''}███████╗{Fore.CYAN if COLORAMA_AVAILABLE else ''}███████╗{Fore.GREEN if COLORAMA_AVAILABLE else ''}██████╗ {Fore.CYAN if COLORAMA_AVAILABLE else ''}███████╗{Fore.GREEN if COLORAMA_AVAILABLE else ''}██████╗ {Fore.CYAN if COLORAMA_AVAILABLE else ''} █████╗ {Fore.GREEN if COLORAMA_AVAILABLE else ''}                    ║
{Fore.GREEN if COLORAMA_AVAILABLE else ''}║  {Fore.CYAN if COLORAMA_AVAILABLE else ''}██║   ██║{Fore.GREEN if COLORAMA_AVAILABLE else ''}██╔════╝{Fore.CYAN if COLORAMA_AVAILABLE else ''}██╔════╝{Fore.GREEN if COLORAMA_AVAILABLE else ''}██╔══██╗{Fore.CYAN if COLORAMA_AVAILABLE else ''}██╔════╝{Fore.GREEN if COLORAMA_AVAILABLE else ''}██╔══██╗{Fore.CYAN if COLORAMA_AVAILABLE else ''}██╔══██╗{Fore.GREEN if COLORAMA_AVAILABLE else ''}                    ║
{Fore.GREEN if COLORAMA_AVAILABLE else ''}║  {Fore.CYAN if COLORAMA_AVAILABLE else ''}██║   ██║{Fore.GREEN if COLORAMA_AVAILABLE else ''}███████╗{Fore.CYAN if COLORAMA_AVAILABLE else ''}█████╗ {Fore.GREEN if COLORAMA_AVAILABLE else ''} ██████╔╝{Fore.CYAN if COLORAMA_AVAILABLE else ''}█████╗ {Fore.GREEN if COLORAMA_AVAILABLE else ''} ██████╔╝{Fore.CYAN if COLORAMA_AVAILABLE else ''}███████║{Fore.GREEN if COLORAMA_AVAILABLE else ''}                    ║
{Fore.GREEN if COLORAMA_AVAILABLE else ''}║  {Fore.CYAN if COLORAMA_AVAILABLE else ''}╚██╗ ██╔╝{Fore.GREEN if COLORAMA_AVAILABLE else ''}╚════██║{Fore.CYAN if COLORAMA_AVAILABLE else ''}██╔══╝ {Fore.GREEN if COLORAMA_AVAILABLE else ''} ██╔══██╗{Fore.CYAN if COLORAMA_AVAILABLE else ''}██╔══╝ {Fore.GREEN if COLORAMA_AVAILABLE else ''}██╔══██╗{Fore.CYAN if COLORAMA_AVAILABLE else ''}██╔══██║{Fore.GREEN if COLORAMA_AVAILABLE else ''}                    ║
{Fore.GREEN if COLORAMA_AVAILABLE else ''}║  {Fore.CYAN if COLORAMA_AVAILABLE else ''} ╚████╔╝ {Fore.GREEN if COLORAMA_AVAILABLE else ''}███████║{Fore.CYAN if COLORAMA_AVAILABLE else ''}███████╗{Fore.GREEN if COLORAMA_AVAILABLE else ''}██║  ██║{Fore.CYAN if COLORAMA_AVAILABLE else ''}███████╗{Fore.GREEN if COLORAMA_AVAILABLE else ''}██║  ██║{Fore.CYAN if COLORAMA_AVAILABLE else ''}██║  ██║{Fore.GREEN if COLORAMA_AVAILABLE else ''}                    ║
{Fore.GREEN if COLORAMA_AVAILABLE else ''}║  {Fore.CYAN if COLORAMA_AVAILABLE else ''}  ╚═══╝ {Fore.GREEN if COLORAMA_AVAILABLE else ''} ╚══════╝{Fore.CYAN if COLORAMA_AVAILABLE else ''}╚══════╝{Fore.GREEN if COLORAMA_AVAILABLE else ''}╚═╝  ╚═╝{Fore.CYAN if COLORAMA_AVAILABLE else ''}╚══════╝{Fore.GREEN if COLORAMA_AVAILABLE else ''}╚═╝  ╚═╝{Fore.CYAN if COLORAMA_AVAILABLE else ''}╚═╝  ╚═╝{Fore.GREEN if COLORAMA_AVAILABLE else ''}                    ║
{Fore.GREEN if COLORAMA_AVAILABLE else ''}║                                                                               ║
{Fore.GREEN if COLORAMA_AVAILABLE else ''}║                    {Fore.YELLOW if COLORAMA_AVAILABLE else ''}👁️  ANLIK KONUM TAKİP SİSTEMİ  👁️{Fore.GREEN if COLORAMA_AVAILABLE else ''}                      ║
{Fore.GREEN if COLORAMA_AVAILABLE else ''}║                                                                               ║
{Fore.GREEN if COLORAMA_AVAILABLE else ''}╠═══════════════════════════════════════════════════════════════════════════════╣
{Fore.GREEN if COLORAMA_AVAILABLE else ''}║                                                                               ║
{Fore.GREEN if COLORAMA_AVAILABLE else ''}║  {Fore.CYAN if COLORAMA_AVAILABLE else ''}┌─────────────────────────────────────────────────────────────────┐{Fore.GREEN if COLORAMA_AVAILABLE else ''}  ║
{Fore.GREEN if COLORAMA_AVAILABLE else ''}║  {Fore.CYAN if COLORAMA_AVAILABLE else ''}│{Fore.GREEN if COLORAMA_AVAILABLE else ''}                    {Fore.YELLOW if COLORAMA_AVAILABLE else ''}SYSTEM MODULES{Fore.GREEN if COLORAMA_AVAILABLE else ''}                              {Fore.CYAN if COLORAMA_AVAILABLE else ''}│{Fore.GREEN if COLORAMA_AVAILABLE else ''}  ║
{Fore.GREEN if COLORAMA_AVAILABLE else ''}║  {Fore.CYAN if COLORAMA_AVAILABLE else ''}├─────────────────────────────────────────────────────────────────┤{Fore.GREEN if COLORAMA_AVAILABLE else ''}  ║
{Fore.GREEN if COLORAMA_AVAILABLE else ''}║  {Fore.CYAN if COLORAMA_AVAILABLE else ''}│{Fore.GREEN if COLORAMA_AVAILABLE else ''}  {Fore.CYAN if COLORAMA_AVAILABLE else ''}--{Fore.GREEN if COLORAMA_AVAILABLE else ''} location/geolocation_tracker    {Fore.GREEN if COLORAMA_AVAILABLE else ''}[{Fore.GREEN if COLORAMA_AVAILABLE else ''}ACTIVE{Fore.GREEN if COLORAMA_AVAILABLE else ''}]  {Fore.CYAN if COLORAMA_AVAILABLE else ''}│{Fore.GREEN if COLORAMA_AVAILABLE else ''}  ║
{Fore.GREEN if COLORAMA_AVAILABLE else ''}║  {Fore.CYAN if COLORAMA_AVAILABLE else ''}│{Fore.GREEN if COLORAMA_AVAILABLE else ''}  {Fore.CYAN if COLORAMA_AVAILABLE else ''}--{Fore.GREEN if COLORAMA_AVAILABLE else ''} location/ip_tracker            {Fore.GREEN if COLORAMA_AVAILABLE else ''}[{Fore.GREEN if COLORAMA_AVAILABLE else ''}ACTIVE{Fore.GREEN if COLORAMA_AVAILABLE else ''}]  {Fore.CYAN if COLORAMA_AVAILABLE else ''}│{Fore.GREEN if COLORAMA_AVAILABLE else ''}  ║
{Fore.GREEN if COLORAMA_AVAILABLE else ''}║  {Fore.CYAN if COLORAMA_AVAILABLE else ''}│{Fore.GREEN if COLORAMA_AVAILABLE else ''}  {Fore.CYAN if COLORAMA_AVAILABLE else ''}--{Fore.GREEN if COLORAMA_AVAILABLE else ''} location/reverse_geocoding      {Fore.GREEN if COLORAMA_AVAILABLE else ''}[{Fore.GREEN if COLORAMA_AVAILABLE else ''}ACTIVE{Fore.GREEN if COLORAMA_AVAILABLE else ''}]  {Fore.CYAN if COLORAMA_AVAILABLE else ''}│{Fore.GREEN if COLORAMA_AVAILABLE else ''}  ║
{Fore.GREEN if COLORAMA_AVAILABLE else ''}║  {Fore.CYAN if COLORAMA_AVAILABLE else ''}│{Fore.GREEN if COLORAMA_AVAILABLE else ''}  {Fore.CYAN if COLORAMA_AVAILABLE else ''}--{Fore.GREEN if COLORAMA_AVAILABLE else ''} telegram/message_sender         {Fore.GREEN if COLORAMA_AVAILABLE else ''}[{Fore.GREEN if COLORAMA_AVAILABLE else ''}ACTIVE{Fore.GREEN if COLORAMA_AVAILABLE else ''}]  {Fore.CYAN if COLORAMA_AVAILABLE else ''}│{Fore.GREEN if COLORAMA_AVAILABLE else ''}  ║
{Fore.GREEN if COLORAMA_AVAILABLE else ''}║  {Fore.CYAN if COLORAMA_AVAILABLE else ''}│{Fore.GREEN if COLORAMA_AVAILABLE else ''}  {Fore.CYAN if COLORAMA_AVAILABLE else ''}--{Fore.GREEN if COLORAMA_AVAILABLE else ''} web/flask_server               {Fore.GREEN if COLORAMA_AVAILABLE else ''}[{Fore.GREEN if COLORAMA_AVAILABLE else ''}ACTIVE{Fore.GREEN if COLORAMA_AVAILABLE else ''}]  {Fore.CYAN if COLORAMA_AVAILABLE else ''}│{Fore.GREEN if COLORAMA_AVAILABLE else ''}  ║
{Fore.GREEN if COLORAMA_AVAILABLE else ''}║  {Fore.CYAN if COLORAMA_AVAILABLE else ''}└─────────────────────────────────────────────────────────────────┘{Fore.GREEN if COLORAMA_AVAILABLE else ''}  ║
{Fore.GREEN if COLORAMA_AVAILABLE else ''}║                                                                               ║
{Fore.GREEN if COLORAMA_AVAILABLE else ''}║  {Fore.CYAN if COLORAMA_AVAILABLE else ''}┌─────────────────────────────────────────────────────────────────┐{Fore.GREEN if COLORAMA_AVAILABLE else ''}  ║
{Fore.GREEN if COLORAMA_AVAILABLE else ''}║  {Fore.CYAN if COLORAMA_AVAILABLE else ''}│{Fore.GREEN if COLORAMA_AVAILABLE else ''}                    {Fore.YELLOW if COLORAMA_AVAILABLE else ''}CONFIGURATION{Fore.GREEN if COLORAMA_AVAILABLE else ''}                                {Fore.CYAN if COLORAMA_AVAILABLE else ''}│{Fore.GREEN if COLORAMA_AVAILABLE else ''}  ║
{Fore.GREEN if COLORAMA_AVAILABLE else ''}║  {Fore.CYAN if COLORAMA_AVAILABLE else ''}├─────────────────────────────────────────────────────────────────┤{Fore.GREEN if COLORAMA_AVAILABLE else ''}  ║
{Fore.GREEN if COLORAMA_AVAILABLE else ''}║  {Fore.CYAN if COLORAMA_AVAILABLE else ''}│{Fore.GREEN if COLORAMA_AVAILABLE else ''}  {Fore.CYAN if COLORAMA_AVAILABLE else ''}Name{Fore.GREEN if COLORAMA_AVAILABLE else ''}              {Fore.CYAN if COLORAMA_AVAILABLE else ''}Current Setting{Fore.GREEN if COLORAMA_AVAILABLE else ''}    {Fore.CYAN if COLORAMA_AVAILABLE else ''}Required{Fore.GREEN if COLORAMA_AVAILABLE else ''}  {Fore.CYAN if COLORAMA_AVAILABLE else ''}Description{Fore.GREEN if COLORAMA_AVAILABLE else ''}        {Fore.CYAN if COLORAMA_AVAILABLE else ''}│{Fore.GREEN if COLORAMA_AVAILABLE else ''}  ║
{Fore.GREEN if COLORAMA_AVAILABLE else ''}║  {Fore.CYAN if COLORAMA_AVAILABLE else ''}├─────────────────────────────────────────────────────────────────┤{Fore.GREEN if COLORAMA_AVAILABLE else ''}  ║
{Fore.GREEN if COLORAMA_AVAILABLE else ''}║  {Fore.CYAN if COLORAMA_AVAILABLE else ''}│{Fore.GREEN if COLORAMA_AVAILABLE else ''}  {Fore.CYAN if COLORAMA_AVAILABLE else ''}BOT_TOKEN{Fore.GREEN if COLORAMA_AVAILABLE else ''}         {Fore.YELLOW if COLORAMA_AVAILABLE else ''}Not Set{Fore.GREEN if COLORAMA_AVAILABLE else ''}          {Fore.YELLOW if COLORAMA_AVAILABLE else ''}yes{Fore.GREEN if COLORAMA_AVAILABLE else ''}     {Fore.CYAN if COLORAMA_AVAILABLE else ''}Telegram Bot Token{Fore.GREEN if COLORAMA_AVAILABLE else ''}  {Fore.CYAN if COLORAMA_AVAILABLE else ''}│{Fore.GREEN if COLORAMA_AVAILABLE else ''}  ║
{Fore.GREEN if COLORAMA_AVAILABLE else ''}║  {Fore.CYAN if COLORAMA_AVAILABLE else ''}│{Fore.GREEN if COLORAMA_AVAILABLE else ''}  {Fore.CYAN if COLORAMA_AVAILABLE else ''}CHAT_ID{Fore.GREEN if COLORAMA_AVAILABLE else ''}           {Fore.YELLOW if COLORAMA_AVAILABLE else ''}Not Set{Fore.GREEN if COLORAMA_AVAILABLE else ''}          {Fore.YELLOW if COLORAMA_AVAILABLE else ''}yes{Fore.GREEN if COLORAMA_AVAILABLE else ''}     {Fore.CYAN if COLORAMA_AVAILABLE else ''}Telegram Chat ID{Fore.GREEN if COLORAMA_AVAILABLE else ''}   {Fore.CYAN if COLORAMA_AVAILABLE else ''}│{Fore.GREEN if COLORAMA_AVAILABLE else ''}  ║
{Fore.GREEN if COLORAMA_AVAILABLE else ''}║  {Fore.CYAN if COLORAMA_AVAILABLE else ''}│{Fore.GREEN if COLORAMA_AVAILABLE else ''}  {Fore.CYAN if COLORAMA_AVAILABLE else ''}IFRAME_LINK{Fore.GREEN if COLORAMA_AVAILABLE else ''}      {Fore.YELLOW if COLORAMA_AVAILABLE else ''}Not Set{Fore.GREEN if COLORAMA_AVAILABLE else ''}          {Fore.YELLOW if COLORAMA_AVAILABLE else ''}yes{Fore.GREEN if COLORAMA_AVAILABLE else ''}     {Fore.CYAN if COLORAMA_AVAILABLE else ''}Target URL{Fore.GREEN if COLORAMA_AVAILABLE else ''}         {Fore.CYAN if COLORAMA_AVAILABLE else ''}│{Fore.GREEN if COLORAMA_AVAILABLE else ''}  ║
{Fore.GREEN if COLORAMA_AVAILABLE else ''}║  {Fore.CYAN if COLORAMA_AVAILABLE else ''}│{Fore.GREEN if COLORAMA_AVAILABLE else ''}  {Fore.CYAN if COLORAMA_AVAILABLE else ''}SRVHOST{Fore.GREEN if COLORAMA_AVAILABLE else ''}          {Fore.GREEN if COLORAMA_AVAILABLE else ''}0.0.0.0{Fore.GREEN if COLORAMA_AVAILABLE else ''}            {Fore.CYAN if COLORAMA_AVAILABLE else ''}no{Fore.GREEN if COLORAMA_AVAILABLE else ''}      {Fore.CYAN if COLORAMA_AVAILABLE else ''}Server Host{Fore.GREEN if COLORAMA_AVAILABLE else ''}        {Fore.CYAN if COLORAMA_AVAILABLE else ''}│{Fore.GREEN if COLORAMA_AVAILABLE else ''}  ║
{Fore.GREEN if COLORAMA_AVAILABLE else ''}║  {Fore.CYAN if COLORAMA_AVAILABLE else ''}│{Fore.GREEN if COLORAMA_AVAILABLE else ''}  {Fore.CYAN if COLORAMA_AVAILABLE else ''}SRVPORT{Fore.GREEN if COLORAMA_AVAILABLE else ''}          {Fore.GREEN if COLORAMA_AVAILABLE else ''}5000{Fore.GREEN if COLORAMA_AVAILABLE else ''}               {Fore.CYAN if COLORAMA_AVAILABLE else ''}no{Fore.GREEN if COLORAMA_AVAILABLE else ''}      {Fore.CYAN if COLORAMA_AVAILABLE else ''}Server Port{Fore.GREEN if COLORAMA_AVAILABLE else ''}        {Fore.CYAN if COLORAMA_AVAILABLE else ''}│{Fore.GREEN if COLORAMA_AVAILABLE else ''}  ║
{Fore.GREEN if COLORAMA_AVAILABLE else ''}║  {Fore.CYAN if COLORAMA_AVAILABLE else ''}└─────────────────────────────────────────────────────────────────┘{Fore.GREEN if COLORAMA_AVAILABLE else ''}  ║
{Fore.GREEN if COLORAMA_AVAILABLE else ''}║                                                                               ║
{Fore.GREEN if COLORAMA_AVAILABLE else ''}╠═══════════════════════════════════════════════════════════════════════════════╣
{Fore.GREEN if COLORAMA_AVAILABLE else ''}║                                                                               ║
{Fore.GREEN if COLORAMA_AVAILABLE else ''}║  {Fore.CYAN if COLORAMA_AVAILABLE else ''}┌─────────────────────────────────────────────────────────────────┐{Fore.GREEN if COLORAMA_AVAILABLE else ''}  ║
{Fore.GREEN if COLORAMA_AVAILABLE else ''}║  {Fore.CYAN if COLORAMA_AVAILABLE else ''}│{Fore.GREEN if COLORAMA_AVAILABLE else ''}                    {Fore.YELLOW if COLORAMA_AVAILABLE else ''}OWNER & CODED BY RERO{Fore.GREEN if COLORAMA_AVAILABLE else ''}                          {Fore.CYAN if COLORAMA_AVAILABLE else ''}│{Fore.GREEN if COLORAMA_AVAILABLE else ''}  ║
{Fore.GREEN if COLORAMA_AVAILABLE else ''}║  {Fore.CYAN if COLORAMA_AVAILABLE else ''}├─────────────────────────────────────────────────────────────────┤{Fore.GREEN if COLORAMA_AVAILABLE else ''}  ║
{Fore.GREEN if COLORAMA_AVAILABLE else ''}║  {Fore.CYAN if COLORAMA_AVAILABLE else ''}│{Fore.GREEN if COLORAMA_AVAILABLE else ''}  {Fore.CYAN if COLORAMA_AVAILABLE else ''}Instagram{Fore.GREEN if COLORAMA_AVAILABLE else ''} : {Fore.GREEN if COLORAMA_AVAILABLE else ''}instagram.com/why_reronuzzz{Fore.GREEN if COLORAMA_AVAILABLE else ''}                    {Fore.CYAN if COLORAMA_AVAILABLE else ''}│{Fore.GREEN if COLORAMA_AVAILABLE else ''}  ║
{Fore.GREEN if COLORAMA_AVAILABLE else ''}║  {Fore.CYAN if COLORAMA_AVAILABLE else ''}│{Fore.GREEN if COLORAMA_AVAILABLE else ''}  {Fore.CYAN if COLORAMA_AVAILABLE else ''}Telegram{Fore.GREEN if COLORAMA_AVAILABLE else ''}  : {Fore.GREEN if COLORAMA_AVAILABLE else ''}t.me/why_reronuzzz{Fore.GREEN if COLORAMA_AVAILABLE else ''}                         {Fore.CYAN if COLORAMA_AVAILABLE else ''}│{Fore.GREEN if COLORAMA_AVAILABLE else ''}  ║
{Fore.GREEN if COLORAMA_AVAILABLE else ''}║  {Fore.CYAN if COLORAMA_AVAILABLE else ''}│{Fore.GREEN if COLORAMA_AVAILABLE else ''}  {Fore.CYAN if COLORAMA_AVAILABLE else ''}GitHub{Fore.GREEN if COLORAMA_AVAILABLE else ''}    : {Fore.GREEN if COLORAMA_AVAILABLE else ''}github.com/WHY-RERO{Fore.GREEN if COLORAMA_AVAILABLE else ''}                        {Fore.CYAN if COLORAMA_AVAILABLE else ''}│{Fore.GREEN if COLORAMA_AVAILABLE else ''}  ║
{Fore.GREEN if COLORAMA_AVAILABLE else ''}║  {Fore.CYAN if COLORAMA_AVAILABLE else ''}└─────────────────────────────────────────────────────────────────┘{Fore.GREEN if COLORAMA_AVAILABLE else ''}  ║
{Fore.GREEN if COLORAMA_AVAILABLE else ''}║                                                                               ║
{Fore.GREEN if COLORAMA_AVAILABLE else ''}╚═══════════════════════════════════════════════════════════════════════════════╝
"""
        return banner
    except Exception as e:
        
        return f"""
{'='*70}
VESPERA - Anlık Konum Takip Sistemi
{'='*70}
"""

def show_banner():
    """Banner'ı göster"""
    try:
        banner_text = create_vespera_banner()
        safe_print(banner_text)
        print()
    except Exception as e:
        safe_print("=" * 70)
        safe_print("VESPERA - Anlık Konum Takip Sistemi")
        safe_print("=" * 70)
        print()

def show_loading_message(message, color=''):
    """Yükleniyor mesajı göster"""
    typing_effect(f"[*] {message}", color, delay=0.02)

def show_success_message(message, color=''):
    """Başarı mesajı göster"""
    typing_effect(f"[+] {message}", color, delay=0.02)

def show_info_message(message, color=''):
    """Bilgi mesajı göster"""
    typing_effect(f"[*] {message}", color, delay=0.02)

def show_error_message(message, color=''):
    """Hata mesajı göster"""
    typing_effect(f"[-] {message}", color, delay=0.02)
