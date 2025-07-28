from pyVim import connect
from pyVmomi import vim

class VCenterConnection:
    def __init__(self, host, user, password, port=443, disable_ssl_verification=True):
        self.host = host
        self.user = user
        self.password = password
        self.port = port
        self.disable_ssl_verification = disable_ssl_verification
        self.si = None

    def connect(self):
        try:
            if self.disable_ssl_verification:
                self.si = connect.SmartConnectNoSSL(
                    host=self.host,
                    user=self.user,
                    pwd=self.password,
                    port=self.port
                )
            else:
                self.si = connect.SmartConnect(
                    host=self.host,
                    user=self.user,
                    pwd=self.password,
                    port=self.port
                )
        except Exception as e:
            print(f"Failed to connect to {self.host}: {e}")
            raise

    def disconnect(self):
        if self.si:
            connect.Disconnect(self.si)
            self.si = None
