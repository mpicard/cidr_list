# -*- coding: utf-8 -*-
from netaddr import IPNetwork
import click


@click.command()
@click.argument('cidr')
@click.option('--seperator', '-s', default=',', help='List seperator.')
@click.option('--file', '-f', default=False, help='txt file output path.')
@click.option('--range/--no-range', default=False, help='Output first and last IP Addresses')
def main(cidr, seperator, file, range):
    """
    Convert CIDR to list of IPs
    """
    ip = IPNetwork(cidr)

    string = seperator.strip().join([str(i) for i in ip])

    if range:
        string = '{}-{}'.format(ip[0], ip[-1])

    if file:
        with open(file, 'w') as f:
            f.write(string)
    else:
        click.echo(string)
