# Airline Booking Market Demand Dashboard

A simple and interactive Streamlit web app that visualizes airline demand trends using Google Trends data. This tool helps analyze the popularity of specific airline routes over time, providing quick insights for decision-making.

---

## Features

* Visualizes search trends for any airline route.
* Generates basic demand insights (min, max, latest values).
* Displays raw data in an easy-to-read table.
* Built with **Streamlit** and **Pytrends**.

---

## Tech Stack

* Python 3.x
* Streamlit
* Pytrends
* Pandas
* Matplotlib

---

## Installation

1. **Clone the repository:**

```bash
git clone https://github.com/duttaSubhajit/airline-demand-dashboard.git
cd airline-demand-dashboard
```

2. **Create a virtual environment (optional but recommended):**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

---

## How to Run

```bash
streamlit run airline.py
```

The app will open in your default browser at `http://localhost:8501`

---

## How to Use

1. Enter the **Origin City** (e.g., Sydney).
2. Enter the **Destination City** (e.g., Melbourne).
3. Click **Get Market Demand**.
4. View the demand trend chart, read the auto-generated insights, and explore the raw data.

---

## Example Output

* Line Chart: Visualizes how search interest changes over time.
* Insights: "The search demand for Flights from Sydney to Melbourne has fluctuated between 12 and 79 over the past 3 months. The latest demand index is 55."
* Raw Data: Tabular view of Google Trends data.

---

## Limitations

* Uses Google search trend data as a **proxy** for real airline demand.
* Cannot provide real-time booking data or actual flight prices.

---

## Future Improvements

* Integration with real airline data APIs like Skyscanner or AviationStack.
* Predictive analytics using machine learning.
* Save and compare trends over time.

---

## Contribution

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

---

## License

This project is open-source and available under the [MIT License](LICENSE).

---

## Acknowledgements

* [Streamlit](https://streamlit.io/)
* [Pytrends](https://github.com/GeneralMills/pytrends)
* [Matplotlib](https://matplotlib.org/)


