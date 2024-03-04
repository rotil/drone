import socket
import binascii
import time

def send_payload(hex_payload, ip, port, iterations, delay_ms):
    payload = binascii.unhexlify(hex_payload.replace(" ", ""))
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as udp_socket:
        for _ in range(iterations):
            print("Sending payload:", hex_payload)
            udp_socket.sendto(payload, (ip, port))
            time.sleep(delay_ms / 1000)  # Convert delay to seconds

def main():
    hex_payload = "EF000400"
    ip = "192.168.1.1"
    port = 8800
    iterations = 10000
    delay_ms = 90

    try:
        send_payload(hex_payload, ip, port, iterations, delay_ms)
    except Exception as e:
        print("An error occurred: {}".format(e))

if __name__ == "__main__":
    main()
