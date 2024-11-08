# Temperature Graphing Script

This Python script reads temperature, relative humidity, and dew point data from an Excel file and visualizes the data for the last `N` days. The number of days to graph can be specified via a command-line argument.

## Features
- Automatically detects the correct date-time column (`Date-Time (CDT)` or `Date-Time (CST/CDT)`).
- Filters data for a specific number of days (default: last 2 days).
- Plots temperature, relative humidity, and dew point in an easy-to-read graph.
- Supports command-line input for flexibility.

---

## Prerequisites

1. **Python**  
   Ensure Python 3.7 or higher is installed on your machine. Download it from [python.org](https://www.python.org).

2. **Required Libraries**  
   Install the following Python libraries:
   - `pandas` (for data manipulation)
   - `matplotlib` (for plotting graphs)
   - `argparse` (for command-line argument handling)

   Install them via `pip`:
   ```bash
   pip install pandas matplotlib argparse
   ```

---

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/JohnEngates/temperature-graphing-script.git
   ```
   Navigate into the project directory:
   ```bash
   cd temperature-graphing-script
   ```

2. **Prepare Your Excel Data**
   Ensure your Excel file has the required columns, including:
   - `Date-Time (CDT)` or `Date-Time (CST/CDT)`
   - `Temperature (°F) `
   - `RH (%) `
   - `Dew Point (°F) `

   These are the columns the script uses for processing and graphing.

---

## Usage

Run the script with the following command:
```bash
python script_name.py path/to/your/file.xlsx [-d N]
```

### Arguments
- **`path/to/your/file.xlsx`**: Path to the Excel file containing your data.
- **`-d N`** (optional): Number of days to graph. Default is 2 days.

---

## Examples

### Default (Last 2 Days):
```bash
python graphtemps.py temps.xlsx
```
This will graph the last 2 days of data from the `temps.xlsx` file.

### Graphing the Last 3 Days:
```bash
python graphtemps.py temps.xlsx -d 3
```

### Graphing a Single Day:
```bash
python graphtemps.py temps.xlsx -d 1
```

---

## Output
The script generates a graph with three subplots:
1. **Temperature Over Time** (red line)
2. **Relative Humidity Over Time** (blue line)
3. **Dew Point Over Time** (green line)

Each graph is displayed with a labeled x-axis (Date-Time) and y-axis.

---

## Contributing
If you’d like to contribute:
1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature-name"
   ```
4. Push to your branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Issues
If you encounter any issues or have suggestions, feel free to open an issue in the [GitHub repository](https://github.com/JohnEngates/temperature-graphing-script).

---

Feel free to modify this template to fit your specific preferences or repository details!
