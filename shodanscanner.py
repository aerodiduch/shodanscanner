import shodan
import socket
from pprint import pprint as pp
import json
from openpyxl import Workbook
from openpyxl import styles
import argparse

api = shodan.Shodan('') #Insert API key.


parser = argparse.ArgumentParser(
    prog='shodanscanner',
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



def load_data(filename: str) -> list:
    '''Loads data from specified target file

    Args:
        filename (str): File containing hosts data

    Returns:
        list: List contaning hosts
    '''
    hosts = []
    with open(filename, 'r') as fh:
        for line in fh:
            hosts.append(
                line.replace('\n', '')
                )
    return hosts


def save_data(data: list, workbook: Workbook, filename: str):
    '''Saves parsed data to output XLSX file.

    Args:
        data (list): API response from Shodan
        workbook (Workbook): Workbook object to write
        filename (str): Output filename
    '''
    
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
    
def request_data(data: list, output_name: str):
    '''Request data to Shodan API

    Args:
        data (list): List of hosts
        output_name (str): Fiilename to write to.
    '''
    print(f'-> Ready to scan {len(data)} hosts...\n')
    for host in data:
        try:
            host_info = api.host(host)
            save_data(host_info, wb, output_name)
        except shodan.APIError as e:
            if 'IP' in e.args[0]:
                print(f'-> No results for {host}')
            continue
    print(f'\n-> Finished scan. Results dumped to "{output_name}.xlsx"')


if __name__ == '__main__':
    wb = Workbook()
    wb.active.append(
        ['IP', 'ISP', 'ASN', 'LOCATION', 'PORTS', 'PRODUCTS', 'CVEs', 'LAST UPDATED', 'DOMAINS']
    )
    
    if args.file:
        output_name = args.output if args.output is not None else 'results'
        data = load_data(args.file)
        request_data(data, output_name)
