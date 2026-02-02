TOPSIS Decision Support System

This repository contains a comprehensive implementation of the TOPSIS (Technique for Order Preference by Similarity to Ideal Solution) method, designed to support multi-criteria decision-making problems.
The project showcases how the TOPSIS algorithm can be applied through multiple interfaces, making it practical for both technical and non-technical users.
📌 Methodology

The decision-making process in this project follows the standard TOPSIS workflow:

Reading decision data from a CSV file

Validating input values, weights, and impacts

Normalizing the decision matrix and applying weights

Determining the ideal best and ideal worst solutions

Computing TOPSIS scores and ranking the alternatives

📂 Project Structure and Components

To improve accessibility and flexibility, the TOPSIS system is implemented in multiple formats.

1️⃣ Command Line Application

Features:

Accepts a CSV file as input

Takes weights and impacts as command-line parameters

Generates a CSV output file with TOPSIS scores and rankings

.

2️⃣ Python Package

Features:

Encapsulates the core TOPSIS logic as a reusable Python module

Can be installed directly using pip

Provides a command-line interface for easy execution

🔗 PyPI Link:
https://pypi.org/project/topsis-bhavana-102303704/

3️⃣ Web Application

Features:

Built using the Flask framework

Allows users to upload CSV files through a browser

Accepts weights, impacts, and an email address as input

Automatically emails the result file to the user after processing

Deployed on the Vercel cloud platform

🌐 Live Web Application:
https://topsis-web-app-chi.vercel.app/

4️⃣ User Interface

The web interface is designed with simplicity in mind, enabling users to perform TOPSIS analysis easily without requiring prior programming knowledge.

🛠 Technologies Used

Python

Flask

Pandas

NumPy

HTML & CSS

SMTP 

GitHub

Vercel

