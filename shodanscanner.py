import shodan
import socket
from pprint import pprint as pp
import json
from openpyxl import Workbook
from openpyxl import styles
import argparse

api = shodan.Shodan('')


parser = argparse.ArgumentParser(
    prog='shodanfinder',
    description='Simple script to bulk scan IPs on Shodan',
    epilog='made by aerodiduch. https://github.com/aerodiduch'
)

parser.add_argument(
    '-f', '--file', help='File containing IP address to scan. Input must be one IP per line. '
)

parser.add_argument(
    '-t', '--target', help='Scan a single target, e.g: -t 200.100.20.10'
)

parser.add_argument(
    '-o', '--output', help='Name of the output file without extension. Default value is "results".'
)

args = parser.parse_args()



def load_data(filename):
    hosts = []
    with open(filename, 'r') as fh:
        for line in fh:
            hosts.append(
                line.replace('\n', '')
                )
    return hosts


def save_data(data, workbook, filename):
    ws = workbook.active
    
    if 'ports' in data:
        ports = ", ".join([str(port) for port in data['ports']])
    else:
        ports = '----'
    
    if 'domains' in data:
        domains = ", ".join([str(domain) for domain in data['domains']])
    else:
        domains = '----'
        
    if 'vulns' in data:
        vulns = ", ".join([str(vuln) for vuln in data['vulns']])
    else:
        vulns = '----'
    
    
    font = styles.Font(bold=True)
    headers = ws['A1':'I1']
    for column in headers[0]:
        column.font = font

    ws.append(
        [data['ip_str'], data['isp'], data['asn'], data['city'], ports, '', vulns, data['last_update'], domains]
    )
    workbook.save(f'{filename}.xlsx')



if __name__ == '__main__':
    wb = Workbook()
    wb.active.append(
        ['IP', 'ISP', 'ASN', 'LOCATION', 'PORTS', 'PRODUCTS', 'CVEs', 'LAST UPDATED', 'DOMAINS']
    )
    
    if args.file:
        output_name = args.output if args.output is not None else 'results'
        data = load_data(args.file)
        for host in data:
            host_info = api.host(host)
            save_data(host_info, wb, output_name)
