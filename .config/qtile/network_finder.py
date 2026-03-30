import os

def get_network_interface():
    interfaces = os.listdir('/sys/class/net/')
    physical_interfaces = [i for i in interfaces if i != 'lo' and not i.startswith('vbox')]
    
    if not physical_interfaces:
        return "None"

    return physical_interfaces[0]

if __name__ == "__main__":
    print(get_network_interface())