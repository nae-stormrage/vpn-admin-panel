import os
import subprocess
import random

WG_PATH = os.getenv("WG_PATH")
WG_DEFAULT_ADDRESS = os.getenv("WG_DEFAULT_ADDRESS")
WG_DEVICE = os.getenv("WG_DEVICE")
WG_PORT = os.getenv("WG_PORT")
WG_PERSISTENT_KEEPALIVE = os.getenv("WG_PERSISTENT_KEEPALIVE")

JC = int(os.getenv("JC", random.randint(3, 10)))
JMIN = int(os.getenv("JMIN", 50))
JMAX = int(os.getenv("JMAX", 1000))
S1 = int(os.getenv("S1", random.randint(15, 150)))
S2 = int(os.getenv("S2", random.randint(15, 150)))
H1 = int(os.getenv("H1", random.randint(1, 2_147_483_647)))
H2 = int(os.getenv("H2", random.randint(1, 2_147_483_647)))
H3 = int(os.getenv("H3", random.randint(1, 2_147_483_647)))
H4 = int(os.getenv("H4", random.randint(1, 2_147_483_647)))

def generate_keys():
    private_key = subprocess.check_output(["wg", "genkey"]).decode().strip()
    public_key = subprocess.check_output(["wg", "pubkey"], input=private_key.encode()).decode().strip()
    return private_key, public_key

def create_vpn_user(username: str):
    private_key, public_key = generate_keys()
    config_path = os.path.join(WG_PATH, f"{username}.conf")
    octet = str(random.randint(2, 254))
    address = WG_DEFAULT_ADDRESS.replace("x", octet)

    config_content = f"""
[Interface]
PrivateKey = {private_key}
Address = {address}/24
ListenPort = {WG_PORT}
PostUp = iptables -t nat -A POSTROUTING -s {address}/24 -o {WG_DEVICE} -j MASQUERADE
PostDown = iptables -t nat -D POSTROUTING -s {address}/24 -o {WG_DEVICE} -j MASQUERADE
PersistentKeepalive = {WG_PERSISTENT_KEEPALIVE}

# AmneziaWG obfuscation
JC = {JC}
JMIN = {JMIN}
JMAX = {JMAX}
S1 = {S1}
S2 = {S2}
H1 = {H1}
H2 = {H2}
H3 = {H3}
H4 = {H4}

[Peer]
PublicKey = <SERVER_PUBLIC_KEY>
AllowedIPs = 0.0.0.0/0
"""

    with open(config_path, "w") as f:
        f.write(config_content.strip())

    return {"username": username, "private_key": private_key, "public_key": public_key, "config_file": f"/configs/{username}.conf"}
