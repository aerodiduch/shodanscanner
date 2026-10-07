# shodanscanner

[![License: MIT](https://img.shields.io/github/license/aerodiduch/shodanscanner)](LICENSE) ![Python](https://img.shields.io/badge/python-3776AB?logo=python&logoColor=white) ![Shodan API](https://img.shields.io/badge/API-Shodan-B80000)

[English](README.md)

Consulta en Shodan una lista de direcciones IP de una sola vez y vuelca lo que encuentra en un Excel: proveedor, ASN, ciudad, puertos abiertos, CVE, última actualización y dominios, una fila por IP.

## Instalación

Necesitás Python 3 y una API key de Shodan, que está en https://account.shodan.io/.

```sh
git clone https://github.com/aerodiduch/shodanscanner
cd shodanscanner
python -m venv venv
source venv/bin/activate        # en Windows: venv\Scripts\activate
pip install -r requirements.txt
```

La primera vez que lo corrés te pide la API key y la guarda en un archivo `.env` en la misma carpeta. Para cambiarla después, editá ese archivo.

## Uso

```sh
python shodanscanner.py -f mis_ips.txt -o datos_ip
```

- `-f`: un archivo de texto con una IP por línea.
- `-o`: nombre del Excel, sin la extensión (por defecto `results`). El `.xlsx` lo agrega solo.

Muestra una barra de avance y, al final, la lista de IP de las que Shodan no tenía datos. El Excel tiene estas columnas: IP, ISP, ASN, LOCATION, PORTS, PRODUCTS, CVEs, LAST UPDATED, DOMAINS.

## Limitaciones

- `-t` (una sola IP) aparece en la ayuda pero todavía no está conectado. Para una IP, usá un archivo con una línea.
- La columna PRODUCTS queda vacía.

## Licencia

MIT, ver [LICENSE](LICENSE).
