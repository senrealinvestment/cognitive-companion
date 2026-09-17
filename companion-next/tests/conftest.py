import socket

import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--live", action="store_true", help="Opt in to the hosted nonmedical smoke"
    )


@pytest.fixture(autouse=True)
def block_network_unless_live(request, monkeypatch):
    if request.node.get_closest_marker("integration") and request.config.getoption(
        "--live"
    ):
        return

    def forbidden(*args, **kwargs):
        raise AssertionError("Network forbidden in offline tests")

    monkeypatch.setattr(socket.socket, "connect", forbidden)
    monkeypatch.setattr(socket.socket, "connect_ex", forbidden)
    monkeypatch.setattr(socket, "create_connection", forbidden)
