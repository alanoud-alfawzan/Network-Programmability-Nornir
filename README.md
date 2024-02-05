# Network Automation with Nornir

Welcome to the Network Automation task using Nornir! This repository showcases how to automate network tasks, collect data from routers and switches, display results in a rich format, and save them in a CSV file using the Nornir framework.

## Task Overview

Network automation is crucial for managing and maintaining complex network infrastructures. Nornir, a Python automation framework, empowers you to streamline and automate network tasks efficiently. In this task, I demonstrate how to leverage Nornir to gather information from routers and switches, present the results in a visually appealing format, and save them for further analysis.

## Prerequisites

Before getting started, make sure you have the following prerequisites:

- Python installed on your machine.
- Basic knowledge of networking concepts.
- Familiarity with Git for version control.

## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/alanoud-alfawzan/Network-Programmability-Nornir.git
    ```

2. Create a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Update the inventory file with your network device details (`/hosts.yaml`).
2. Run the Nornir script:

    ```bash
    python get_information_using_nornir_netmiko.py
    ```

4. Check the results displayed and find the generated CSV file with name `Devices_informations.csv` at your directory.


## Contributions

Contributions are welcome! If you'd like to enhance, open an issue or submit a pull request. Feel free to share your ideas and feedback.

Happy automating! 🚀🌐
