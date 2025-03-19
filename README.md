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

- `1_TNet1_getting_started.ipynb`: Getting started with TSNet.
- `2_TNet2_pump_shutoff.ipynb`: Simulating a pump shutoff.
- `3_TNet3_burst_leak.ipynb`: Simulating a burst with a background leak.
- `4_TNet3_time_step.ipynb`: Selecting the appropriate time step.
- `5_TNet3_results.ipynb`: Importing an existing result object
- `6_TNet3_surge_tanks.ipynb`: Simulating with and without surge tanks.
- `7_TNet3_friction_models.ipynb`: Demonstrating different friction models.



### Network Files

- `networks/Tnet1.inp`
- `networks/Tnet2.inp`
- `networks/Tnet3.inp`

## License

This project is licensed under the MIT License.
