# Web-Services-and-Applications

Author: Francesco Troja

This repository serves as a key resource for the assessments of the **HDip in Computing within ATU University's Data Analytics program**, specifically for the **Web Services and Application** module. It comprises a `JSON` file named `cso.json` and `three Python programs` designed to execute the primary tasks required for the module.

## Task Problem Statement

- **Task 1**: The initial Python script, named `currentweather.py`, retrieves and showcases real-time **weather** data from the Open **Meteo API**. The API can be accessed at this URL: `https://api.open-meteo.com/v1/forecast?latitude=53.82&longitude=-9.5&current=temperature_2m`. The script outputs the current **temperature and wind direction**. Additionally, in the program an additional URL is used, `https://open-meteo.com/`, to obtain and display the current **wind direction**.
- **Task 2**: The program retrieves the dataset for the **exchequer account** (historical series) from the CSO and saves it into a file named `cso.json`
- **Task 3**: The Python program needs to read a file from a repository. It proceeds to replace all occurrences of the text **Andrew** with the **user's specified name**. The program then commits these modifications and pushes the updated file back to the repository.

## How to download the Repository

Access the provided link: [Web-Services-and-Applications](https://github.com/C-3sc0/Web-Services-and-Applications) and select the `<> Code` button. There are two options for accessing the repository:

- Download it as a `ZIP file`;
- Clone the repository using the provided `HTTPS link` and integrate it into your local machine.

## Repository's Content

- A file named **README.md** file;
- The [`currentweather.py`](https://github.com/C-3sc0/Web-Services-and-Applications/blob/main/assignments/currentweather.py) file;
- The [`assignment03-cso.py`](https://github.com/C-3sc0/Web-Services-and-Applications/blob/main/assignments/assignment03-cso.py) file;
- The [`assignment04-github.py`](https://github.com/C-3sc0/Web-Services-and-Applications/blob/main/assignments/assignment04-github.py) file;
- The [`cso.json`](https://github.com/C-3sc0/Web-Services-and-Applications/blob/main/assignments/cso.json) file, containing the exchequer account data;

## Technologies Used

The project utilizes **Python 3** as its primary technology stack. The official Python package can be obtained from the [Python website](https://www.python.org/downloads/) for download and installation. The utilization of Python 3 ensures compatibility with an extensive array of libraries and tools.
The libraries/modules employed in the current codes include:

- Requests (The documentation can be found in the following link: [Requests](https://pypi.org/project/requests/));
- JSON (The documentation can be found in the following link: [JSON](https://matplotlib.org/stable/index.html));
- GitHub  (The documentation can be found in the following link: [Pygithub](https://pygithub.readthedocs.io/en/latest/introduction.html));
- Re (The documentation can be found in the following link: [Re](https://docs.micropython.org/en/latest/library/re.html));

The majority of the required libraries are typically pre-installed in the Python environment. In cases where a library is not present, the `pip command``, serving as the Python package installer, can be employed. To facilitate the installation process, open the terminal and execute the following command:

```python
pip install library_name
```

It's important to substitute "library_name" with the actual name of the library intended for installation.
