import pytest
from src.connection import VCenterConnection

# Replace with your vCenter details
VCENTER_HOST = "your_vcenter_host"
VCENTER_USER = "your_vcenter_user"
VCENTER_PASSWORD = "your_vcenter_password"

@pytest.fixture(scope="module")
def vcenter_connection():
    connection = VCenterConnection(
        host=VCENTER_HOST,
        user=VCENTER_USER,
        password=VCENTER_PASSWORD
    )
    connection.connect()
    yield connection
    connection.disconnect()

def test_get_server_time(vcenter_connection):
    server_time = vcenter_connection.si.CurrentTime()
    assert server_time is not None
    print(f"vCenter server time: {server_time}")
