import socket
import time

def send_udp_packet(ip, port, payload, delay_ms):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(payload, (ip, port))
    data, _ = sock.recvfrom(1024)
    sock.close()
    return data

def main():
    file_path = "payload.txt"
    ip_dst = "192.168.1.1"
    port_dst = 7099
    delay_ms = 100


    with open(file_path, 'r') as file:
        for line in file:
            hex_payload = bytes.fromhex(line.strip())
            
            # Send payload to the drone
            data_dst1 = send_udp_packet(ip_dst, port_dst, hex_payload, delay_ms)
            print(hex_payload)
            print(f"Received data from {ip_dst}:{port_dst}: {data_dst1.decode('utf-8')}")
            time.sleep(delay_ms / 1000)  # Convert delay to seconds


if __name__ == "__main__":
    main()