# DNG to JPG Image Converter

This repository provides a versatile Python script for effortlessly converting DNG (Digital Negative) images to the widely supported JPEG format.

DNG files, often used by photographers and in professional photography, can now be seamlessly transformed into JPEG images, enhancing their compatibility for sharing, displaying, and printing across a wide range of devices and platforms.

Whether you're a photographer looking to share your work online, a developer working on image processing tools, or simply someone looking to convert DNG files, this repository provides a straightforward solution for transforming DNG images into the more widely supported JPEG format.

# Requirements

- Python 3.11 installed

# Installation

1. Clone the repository:

```shell
git clone https://github.com/hennanlewis/dng2jpg.git
```

Navigate to the project directory:

```shell
cd dng2jpg
```

Set up a virtual environment (optional but recommended):

```shell
python -m venv .env
source .env/bin/activate
```

On windows:
```shell
python -m venv .env
.env\Scripts\activate
```

Install the required dependencies:
```shell
pip install -r requirements.txt
```

To conclude the use of the environment, employ the following code:

```shell
deactivate
```

# Usage

The code has been designed to be short, simple, and easy to understand. For proper functionality, just place your DNG image files in a folder named raw within the same directory level as the `app.py` file, and then run the `app.py` file.

```shell
python app.py
```

# Contributing

Contributions are welcome! If you would like to contribute to this project, please follow these steps:

1. Fork the repository
1. Create a new branch
1. Make your changes
1. Submit a pull request

# License

This project is licensed under the MIT License.
