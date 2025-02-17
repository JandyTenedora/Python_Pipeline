# E-commerce Data Pipeline Project

## Overview

This project is an end-to-end data pipeline designed to process raw e-commerce data from multiple sources, transform and validate the data, and store it in a cloud-based reporting system. The pipeline leverages Python for data ingestion and processing, dbt for data transformation and modeling, and Terraform for infrastructure setup.

## Project Structure

- **app**: Contains the main application code for data ingestion and log processing.
  - **log_processor**: Handles log processing tasks.
    - `log_processor.py`: Main script for processing event logs.
  - **data_ingestion**: Handles data ingestion tasks.
    - `data_ingestor.py`: Abstract base class for data ingestion.
- **infra**: Contains Terraform scripts for infrastructure setup.
  - `main.tf`: Main Terraform configuration file.
- **README.md**: Project documentation.

## Components

### Data Ingestion

- **DataIngestor**: An abstract base class for ingesting data from various sources. It includes methods for parsing and validating data, logging progress, and ingesting data into the destination.

### Log Processing

- **LogProcessor**: A class for processing event logs. It reads log files, applies processing functions, and extracts insights such as the number of events per user and the most common event types.

### Infrastructure Setup

- **Terraform**: Used to provision cloud infrastructure, including BigQuery datasets and tables, and Firestore databases.

## Setup Instructions

### Prerequisites

- Python 3.x
- pip
- Terraform
- Google Cloud SDK (for BigQuery and Firestore)

### Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/JandyTenedora/ecommerce-data-pipeline.git
   cd ecommerce-data-pipeline
   ```
2. Install Python dependencies:
   ```sh
   pip install -r requirements.txt
   ```

3. Initialize and apply Terraform configuration: 
   ```sh
   cd infra
   terraform init
   terraform apply   
   ```

### Running the Pipeline

1. Navigate to the `app` directory:
   ```sh
   cd app
   ```
   
2. Navigate to the `app` directory:
   ```sh
   python log_processor/log_processor.py
   ```

### Usage
#### Log Processor
The log processor reads a JSON log file, processes the logs, and extracts insights. The main script is log_processor.py, which can be executed as follows:
   ```sh
   python log_processor/log_processor.py
   ```
#### Data Ingestor
The data ingestor is an abstract base class that can be extended to ingest data from various sources. Implement the parse_data and validate_data methods to create a custom ingestor. 

### Infrastructure 
The infrastructure is managed using Terraform. The main configuration file is main.tf, which provisions BigQuery datasets and tables, and Firestore databases.