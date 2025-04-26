import socket

def iniciar_sniffer_dns():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('0.0.0.0', 53))
    print("Sniffer DNS iniciado. Aguardando consultas...")

    while True:
        data, addr = sock.recvfrom(512)
        print(f"Consulta DNS recebida de {addr[0]}")

if __name__ == "__main__":
    try:
        iniciar_sniffer_dns()
    except PermissionError:
        print("Permissão negada: execute como administrador/root.")
    except KeyboardInterrupt:
        print("\nSniffer encerrado.")
