from netmiko import ConnectHandler
from pprint import pprint
import paramiko

paramiko.transport.Transport._preferred_kex = (
    'diffie-hellman-group14-sha1',
    'diffie-hellman-group1-sha1',
)

paramiko.transport.Transport._preferred_keys = (
    'ssh-rsa',
)

device_ip = "10.0.15.61"
username = "admin"
password = "cisco"

device_params = {
    "device_type": "cisco_ios",
    "host": device_ip,
    "username": username,
    "password": password,
    'port': 22,
    'conn_timeout': 20,
    'timeout': 30,
}


def gigabit_status():
    ans = ""
    with ConnectHandler(**device_params) as ssh:
        up = 0
        down = 0
        admin_down = 0
        result = ssh.send_command("show ip interface brief", use_textfsm=True)
        interface_status_list = []
        for status in result:
            if status["interface"].startswith("GigabitEthernet"):
                interface_status_list.append(f"{status['interface']} {status['status']}")
                if status["status"] == "up":
                    up += 1
                elif status["status"] == "down":
                    down += 1
                elif status["status"] == "administratively down":
                    admin_down += 1
        ans = (
            ", ".join(interface_status_list)
            + f" -> {up} up, {down} down, {admin_down} administratively down"
        )
        pprint(ans)
        return ans
