from scapy.all import sniff
import json

def packet_callback(packet):
    data = {
        "src_ip": packet.src if hasattr(packet, "src") else "Unknown",
        "dst_ip": packet.dst if hasattr(packet, "dst") else "Unknown",
        "protocol": packet.proto if hasattr(packet, "proto") else "Unknown",
        "packet_length": len(packet)
    }
    print(json.dumps(data, indent=4))

# Capture live packets
sniff(prn=packet_callback, count=10)
