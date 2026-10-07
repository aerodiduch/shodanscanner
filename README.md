# shodanscanner

[![License: MIT](https://img.shields.io/github/license/aerodiduch/shodanscanner)](LICENSE) ![Python](https://img.shields.io/badge/python-3776AB?logo=python&logoColor=white) ![Shodan API](https://img.shields.io/badge/API-Shodan-B80000)

[Español](README.es.md)

Bulk-checks a list of IP addresses on Shodan and dumps what it finds into an Excel file: ISP, ASN, city, open ports, CVEs, last update and domains, one row per IP.

## Install

You need Python 3 and a Shodan API key, which you'll find at https://account.shodan.io/.

```sh
git clone https://github.com/aerodiduch/shodanscanner
cd shodanscanner
python -m venv venv
source venv/bin/activate        # on Windows: venv\Scripts\activate
pip install -r requirements.txt
```

The first time you run it, it asks for the API key and saves it in a `.env` file in the same folder. To change it later, edit that file.

## Usage

```sh
python shodanscanner.py -f my_ips.txt -o ip_data
```

- `-f`: a text file with one IP per line.
- `-o`: name of the Excel file, without the extension (default `results`). It adds `.xlsx` itself.

It shows a progress bar and, at the end, lists the IPs Shodan had no data for. The Excel has these columns: IP, ISP, ASN, LOCATION, PORTS, PRODUCTS, CVEs, LAST UPDATED, DOMAINS.

## Limitations

- `-t` (a single IP) shows up in the help but isn't wired up yet. For one IP, use a file with one line.
- The PRODUCTS column stays empty.

## License

MIT, see [LICENSE](LICENSE).
