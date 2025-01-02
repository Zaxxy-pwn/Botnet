import socket
import threading
import time

# Menangani koneksi bot
def handle_bot(client_socket, client_address):
    print(f"[INFO] Bot terhubung dari {client_address}")
    client_socket.send("Serangan Dimulai!".encode())
    print(f"[INFO] Perintah 'Serangan Dimulai!' dikirim ke {client_address}")
    
    time.sleep(10)  # Serangan berlangsung selama 10 detik
    client_socket.send("Serangan Dihentikan!".encode())
    print(f"[INFO] Perintah 'Serangan Dihentikan!' dikirim ke {client_address}")
    
    client_socket.close()

# Menyiapkan server C&C untuk menerima banyak koneksi
def start_server(host, port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)
    print(f"[INFO] Server C&C berjalan di {host}:{port}")
    
    while True:
        client_socket, client_address = server.accept()
        # Mulai thread untuk menangani bot
        bot_thread = threading.Thread(target=handle_bot, args=(client_socket, client_address))
        bot_thread.start()

# Menjalankan server C&C
if __name__ == "__main__":
    start_server("0.0.0.0", 8080)  # Ganti dengan IP yang sesuai untuk server C&C
