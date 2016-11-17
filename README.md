# cidr-list

[![Build Status](https://travis-ci.org/mpicard/cidr_list.svg?branch=master)](https://travis-ci.org/mpicard/cidr_list)

Convert CIDR to list of IPs.


# Installation

If you don't use `pipsi`, you're missing out.
Here are [installation instructions](https://github.com/mitsuhiko/pipsi#readme).

Simply run:

    $ pipsi install cidr-list

Or with pip

    $ pip install cidr-list


# Usage

To use it:

    $ cidr-list --help
    $ cidr-list 10.10.10.0/30
    > 10.10.10.0,10.10.10.1,10.10.10.2,10.10.10.3
    $ cidr-list 10.10.10.0/30 --range
    > 10.10.10.0-10.10.10.3
    $ cidr-list 10.10.10.0/30 --file output.txt
    $ cidr-list 10.10.10.0/30 --seperator :
    > 10.10.10.0:10.10.10.1:10.10.10.2:10.10.10.3
