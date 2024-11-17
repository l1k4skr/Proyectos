"""

mensaje -> segmento -> paquete -> trama -> bits
- Segmento: TCP
- Paquete: IP
- Trama: Ethernet (MAC)

clases:
- Frame
    - Data
    - Header
    - Trailer
- Packet:
    - Data 
- Segment
"""
class Router:
    def __init__(self):
        self.connections = []
        
    def connect_client(self, client):
        self.connections.append(client)
    
    def send_message(self, frame, client):
        for connection in self.connections:
            # Router section
            if connection.mac == client.mac:
                pass
            else:
                mac_connection = connection
                break
            
        ## Change this when the router is implemented
        ip_connection = mac_connection
        ## Change this when the router is implemented
        print("Cliente: 2")
        ip_connection.receive_message(frame)

class Frame:
    def __init__(self, segment, mac_origin, mac_destination):
        self.data = segment
        self.mac_origin = mac_origin
        self.mac_destination = mac_destination
    def __str__(self):
        return f"Trama: {self.data}\n mac origen: {self.mac_origin}\n mac destino: {self.mac_destination}"
        
class Packet:
    def __init__(self, segment, ip_origin, ip_destination):
        self.data = segment
        self.ip_origin = ip_origin
        self.ip_destination = ip_destination
    def __str__(self):
        return f"Paquete: {self.data}\n ip origen: {self.ip_origin}\n ip destino: {self.ip_destination}"
        
class Segment:
    def __init__(self, data, port_origin, port_destination):
        self.data = data
        self.port_origin = port_origin
        self.port_destination = port_destination
    def __str__ (self):
        return f"Segmento: {self.data}\n puerto origen: {self.port_origin}\n puerto destino: {self.port_destination}"
    
class Client:
    def __init__(self, ip, mac, port):
        self.ip = ip
        self.mac = mac
        self.open_port = port
        
    def send_message(self, message, port_destination, client, router):
        
        print(f"Creando segmento con mensaje {message}...")
        
        segment = Segment(message, self.open_port, port_destination)
        print(f"segmento creado: {segment}\n")
        packet = Packet(segment, self.ip, client.ip)
        print(f"Paquete creado: {packet}\n")
        frame = Frame(packet, self.mac, client.mac)
        print(f"Trama creada: {frame}\n")
        print(f"Enviando mensaje desde {self.ip} a {client.ip}")
        
        router.send_message(frame, client)
    def receive_message(self, frame):
        
        frame = frame # Mac
        print(f"Frame recibido por {frame}")
        packet = frame.data # IP
        print(f"Paquete: {packet}")
        segment = packet.data # TCP
        print(f"Segmento: {segment}")
        print(f"Mensaje: {segment.data}")
        
        print("\n")
        return frame
    
    
mensaje = "Hola mundo"

# Equipo origen
mac = "ff:ff:ff:ff:ff:ff"
ip = "10.10.10.10"
puerto = 80


# Equipo destino
ip_destino = "10.10.10.11"
mac_destino = "ff:ff:ff:ff:ff:f1"
puerto_destino = 80

if __name__ == "__main__":
    cliente1 = Client(ip, mac, puerto)
    cliente2 = Client(ip_destino, mac_destino, puerto_destino)
    router = Router()
    router.connect_client(cliente1)
    router.connect_client(cliente2)
    print("Cliente 1:")
    cliente1.send_message(mensaje, puerto_destino, cliente2, router)

