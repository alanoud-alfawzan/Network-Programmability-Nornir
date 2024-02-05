import os 
import csv
from rich.table import Table
from rich import print as rp
from rich.console import Console
from nornir import InitNornir
from nornir_netmiko import netmiko_send_command


nr = InitNornir(config_file="./config.yaml")

# Header row for the CSV file
header = [
    "Hostname",
    "Interface",
    "CRC Error",
    "Link Status",
    "Protocol Status",
    "MAC Address",
]

# Rich Table creation
table = Table(title="Network Devices Informations \n")
table.add_column("Hostname", justify="left", style="cyan", no_wrap=True)
table.add_column("Interface", justify="center", style="yellow", no_wrap=True)
table.add_column("CRC Error", justify="center", style="red")
table.add_column("Link Status", justify="center", style="yellow")
table.add_column("Protocol Status", justify="center", style="yellow")
table.add_column("MAC Address", justify="center", style="yellow")

rp(f"[gold3] \n Starting Collect Information... Please Wait !!! \n [/gold3]")

# Create function to run nornir task
def crc_error(task):
    output = task.run(
        task=netmiko_send_command, command_string="show interfaces", use_textfsm=True
    )
    data = output.result
    hostname = task.host.name
    # Write the data to the CSV file
    with open("./Devices_informations.csv", "a", newline="") as csvfile:
        wr = csv.writer(csvfile)
        for v in data:
            wr.writerow(
                [
                    hostname,
                    v["interface"],
                    v["crc"],
                    v["link_status"],
                    v["protocol_status"],
                    v["mac_address"],
                ]
            )
            table.add_row(
                hostname,
                v["interface"],
                v["crc"],
                v["link_status"],
                v["protocol_status"],
                v["mac_address"],
            )

# Create the csv file and write the header row, if not it's not exists
if not os.path.isfile("./Devices_informations.csv"):
    with open("./Devices_informations.csv", 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header)
# Run nornir task
my_results = nr.run(task=crc_error)

# Display rich table
console = Console()
console.print(table)

rp(
    "[green] \n We Are Done, All Information Was Saved In (Devices_informations.csv) File. [/green]"
)
