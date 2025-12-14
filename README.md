# data_generator_app
Lightweight Streamlit application to generate synthetic time-series data and export it as CSV.

Designed as a simple data generation and frontend interface.

---

## Context

Given a user need to generate CSV files filled with data representing the evolution of a measure over time:

<img width="247" height="253" alt="image" src="https://github.com/user-attachments/assets/a33e52c4-2b3a-46b4-a628-4a8ddddad67c" />

The aim of this project is to allow users to:
* Parameterize measure name, data frequency, time duration and start time
* Visualize the generated dataframe through a lightweight web interface
* Download a `csv` file containing timestamps, measure name and generated values

<img width="1200" height="600" alt="image" src="https://github.com/user-attachments/assets/ddb0c3a8-948b-49b7-aeff-1985bcbd7c0d" />

---

## App description :
* `app.py` - streamlit script responsible for the web interface and user interactions
* `data_generator.py` - data generation logic and computation functions

---

## How to run it :
To use the script locally, clone the repository using the git clone command, then set up a virtual environment:

```bash
python3 -m venv env
source env/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

You can then test the app with:

```bash
streamlit run app/app.py --server.port 8000
```

You can now reach `http://localhost:8000/` in your browser to use the app :
* Setup parameters (measure name, frequency, time duration, start time)
* Press "rerun" button to rerun the random compute_data function (it won't reset your parameters)
* Finally press "download" button to download csv file in your local download folder

You should now have everything needed to run the application locally. If you want to learn how to deploy it on an Ubuntu server using systemd, feel free to contact me directly (see GitMews on GitHub). 
