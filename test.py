import json
from autosw import app
from autosw.commands import format_interface

test_args = {
    "switcher": "10.188.0.6",
    "interface": "Ethernet0/0/17",
    "traffic_policy": "25M",
    "public_ip": "1.1.1.1"
}

client = app.test_client()

def test_before():
    rv = client.post("/before", data=json.dumps(test_args))
    assert rv.data == "ok"


def test_up():
    rv = client.post("/up", data=json.dumps(test_args))
    assert rv.data == "ok"


def test_down():
    rv = client.post("/down", data=json.dumps(test_args))
    assert rv.data == "ok"

def test_interface_format():
    assert format_interface("NET-4I14-10237-Ethernet0/0/24") == "Ethernet0/0/24"
    assert format_interface("NET-4I14-10237-Gia0/0/1") == "GigabitEthernet0/0/1"
    assert format_interface("HL-C04(1-1)-00300-G0/0/1") == "GigabitEthernet0/0/1"


if __name__ == "__main__":
    test_interface_format()
    test_before()
    test_up()
    test_down()
