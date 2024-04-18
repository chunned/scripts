#!/bin/bash
# Configures a WireGuard client file
# Set required variables for the script
OVERLAY_IP=         # Client's VPN IP address 
OVERLAY_SUBNET=     # VPN subnet 
HOME_SUBNET=        # Home network subnet 
WG_SERVER_ADDRESS=  # DNS address or IP of the server, including port. E.g. vpn.domain.com:51820
DNS1=               # Primary DNS server 
DNS2=               # Secondary DNS server

sudo pacman -S wireguard-tools openresolv
mkdir ~/wg && cd ~/wg 
# Generate keys
wg genkey | tee privkey | wg pubkey > pubkey 

# Create client conf file 
touch wg.conf
echo "[Interface]" >> wg.conf
echo "PrivateKey = $(cat privatekey)" >> wg.conf
echo "Address = $OVERLAY_IP/32" >> wg.conf
echo "DNS = $DNS1, $DNS2" >> wg.conf
echo "" >> wg.conf
echo "[Peer]" >> wg.conf
echo "PublicKey = $SERVER_PUBLIC_KEY" >> wg.conf
echo "AllowedIPs = $OVERLAY_SUBNET, $HOME_SUBNET" >> wg.conf
echo "Endpoint = $WG_SERVER_ADDRESS" >> wg.conf 
