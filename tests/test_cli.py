# -*- coding: utf-8 -*-
import pytest
import mock
from netaddr import IPNetwork
from click.testing import CliRunner
from cidr_list import cli

@pytest.fixture
def runner():
    return CliRunner()

@pytest.fixture
def mock_open(request):
    m = mock.patch('__builtin__.open', mock.mock_open())
    m.start()
    request.addfinalizer(m.stop)

def test_cli(runner):
    arg = '10.10.10.0/28'
    ip = IPNetwork(arg)
    result = runner.invoke(cli.main, [arg])
    assert result.exit_code == 0
    assert not result.exception
    assert result.output.strip() == ','.join([str(i) for i in ip])

def test_cli_with_seperator(runner):
    arg = '10.10.10.0/30'
    ip = IPNetwork(arg)
    result = runner.invoke(cli.main, [arg, '-s :'])
    assert result.exit_code == 0
    assert not result.exception
    assert result.output.strip() == ':'.join([str(i) for i in ip])

def test_cli_with_range(runner):
    arg = '10.10.10.0/30'
    ip = IPNetwork(arg)
    result = runner.invoke(cli.main, [arg, '--range'])
    assert result.exit_code == 0
    assert not result.exception
    assert result.output.strip() == '{}-{}'.format(ip[0], ip[-1])


def test_cli_with_file(runner, mock_open):
    arg = '10.10.10.0/30'
    ip = IPNetwork(arg)
    result = runner.invoke(cli.main, [arg, '-f output.txt'])
    assert result.exit_code == 0
    assert not result.exception
    assert result.output.strip() == ""

