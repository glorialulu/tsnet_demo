# TSNet Demo

This repository contains a demonstration of the TSNet package for transient simulation in water distribution networks. The provided Jupyter notebooks guide you through the process of setting up and running transient simulations using various network models.

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/glorialulu/tsnet_demo/HEAD)

## Getting Started

### Prerequisites

- Python 3.7
- Jupyter Notebook
- TSNet package
- Matplotlib

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/tsnet_demo.git
    cd tsnet_demo
    ```

2. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

### Running the Notebooks

1. Start Jupyter Notebook:
    ```sh
    jupyter notebook
    ```

2. Open any of the 9 notebooks and follow the instructions to run the cells.

## Contents

- `1_TNet1_workshop_script_getting_started.ipynb`: Getting started with TSNet.
- `2_TNet2_workshop_burst.ipynb`: Simulating a burst event.
- `3_TNet2_workshop_pump.ipynb`: Simulating a pump shutoff.
- `4_TNet3_workshop_burst_w_leak.ipynb`: Simulating a burst with a background leak.
- `5_TNet3_workshop_script_friction_models.ipynb`: Demonstrating different friction models.
- `6_TNet3_workshop_script_surge_tanks.ipynb`: Simulating with and without surge tanks.
- `7_TNet3_workshop_script_time_step.ipynb`: Selecting the appropriate time step.
- `8_TNet3_workshop_script_events_comparison.ipynb`: Comparing different transient events.
- `9_TNet3_workshop_script_advanced.ipynb`: Advanced simulation techniques.

### Network Files

- `networks/Tnet1.inp`
- `networks/Tnet2.inp`
- `networks/Tnet3.inp`

## License

This project is licensed under the MIT License.
