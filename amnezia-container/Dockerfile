FROM debian:bookworm-slim

RUN apt-get update && apt-get install -y \
    build-essential dkms \
    git procps iproute2 iptables wireguard-tools curl ca-certificates sudo bash

RUN git clone https://github.com/amnezia-vpn/amneziawg-linux-kernel-module /tmp/amnezia-mod
WORKDIR /tmp/amnezia-mod
RUN make && make install || true

RUN mkdir -p /etc/wireguard

WORKDIR /app
COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

ENV WG_PATH=/etc/wireguard
ENTRYPOINT ["/app/entrypoint.sh"]
