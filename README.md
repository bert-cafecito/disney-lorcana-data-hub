# Disney Lorcana Data Hub

A centralized repository for collecting, analyzing, and exploring Disney Lorcana card data from various sources. Perfect for data enthusiasts, data scientists, and machine learning practitioners looking to explore structured datasets and gain insights into the Disney Lorcana universe.

## Directory Structure

``` plaintext
├── README.md               <- Overview of the project and setup instructions.
├── data/                   <- Raw and processed data files (CSV, JSON, etc.).
│   ├── raw/                <- Raw data from scraping or other sources.
│   └── processed/          <- Cleaned and preprocessed data ready for analysis.
│
├── notebooks/              <- Jupyter Notebooks for data exploration and ML.
│   ├── exploration/        <- EDA (Exploratory Data Analysis) notebooks.
│   ├── visualization/      <- Notebooks focused on visualizing card trends.
│   └── machine_learning/   <- ML models and experiments.
│
├── scripts/                <- Python scripts for data collection and processing.
│   ├── clean_data.py       <- Preprocess raw data into clean datasets.
│   └── utils/              <- Helper utilities.
│
├── requirements.txt        <- List of Python dependencies.
└── LICENSE                 <- MIT or Apache 2.0 license.
```

## Usage

### Note on Development Container

This project includes a `.devcontainer` configuration for Visual Studio Code. If you are using VS Code, you can open the project in a development container to ensure a consistent development environment. The container will automatically install the required dependencies specified in the `requirements.txt` file.

### Prerequisites

Ensure you have the following installed:

- Docker
- Visual Studio Code with the Dev Containers extension

### Instructions

1. Clone the repository:
    ```sh
    git clone https://github.com/bert-cafecito/disney-lorcana-data-hub.git
    cd disney-lorcana-data-hub
    ```

2. **Reopen in Container:**
    - Press `F1` and select `>Dev Containers: Rebuild Container`.

3. **Start Jupyter Notebook:**
    ```sh
    jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser --allow-root
    ```

4. **Access Jupyter Notebook:**
    Open your browser and navigate to `http://localhost:8888`.

5. **Explore Notebooks:**
    - Navigate to the `notebooks/` directory to explore the available Jupyter Notebooks.

## Changelog

This project maintains a [changelog](CHANGELOG.md) to document all notable changes. Please refer to it for detailed information on updates and modifications.

## Contributing

Contributions are welcome and encouraged! To get started, please read the [contributing guidelines](CONTRIBUTING.md) to learn how you can contribute to this project.

## Support

If you would like to support this project or me, you can do so in the following ways:

### Reporting Issues

If you find a bug or have a feature request, please open an issue on the [GitHub Issues](https://github.com/bert-cafecito/disney-lorcana-data-hub/issues) page. Provide as much detail as possible to help us understand and resolve the issue quickly.

### Contributing

If you would like to contribute to the project, please read the [contributing guidelines](CONTRIBUTING.md) to learn how you can help. We appreciate all contributions, whether they are big or small.

### Follow Me on Social Media

- [**Bluesky**](https://bsky.app/profile/bert-cafecito.bsky.social)
- [**Dev Community**](https://dev.to/bert-cafecito)
- [**GitHub**](https://github.com/bert-cafecito)


### Star the Repository

If you find this project useful, please consider starring the repository on GitHub. Starring a repository helps increase its visibility and lets others know that the project is valuable. It also provides motivation and support to the maintainers to continue improving the project.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.