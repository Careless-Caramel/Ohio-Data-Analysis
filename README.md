# 🛢️ Ohio Data Analysis using Flask and SQLite3

A **Flask web application** to analyze **Ohio oil & gas production data** stored in a **SQLite3 database**.  
The project demonstrates how to build a simple web app with Flask that queries a converted Excel dataset and provides aggregated results.

---

## 📊 Dataset

The original dataset is an Excel file:  
[`20210309_2020_1-4.xls`](https://github.com/Careless-Caramel/Ohio-Data-Analysis/blob/main/20210309_2020_1%20-%204.xls)

It was converted into a SQLite3 database file:  

```
20210309_2020_1-4.xls  ➝  data.sqlite3
```

---

## 🚀 Features

- ⚡ Simple **Flask web interface**  
- 🗂️ Database queries with **SQLite3**  
- 📈 Aggregates **OIL, GAS, and BRINE production** by API Well Number  
- 🖥️ Results displayed in HTML templates (`index.html` and `submit.html`)  
- 🌐 Runs locally on port **8080**  

---

## 🛠️ Dependencies

- `Flask`
- `sqlite3` (Python standard library)
- `os` (Python standard library)

Install dependencies using:

```bash
pip install -r requirements.txt
```

---

## ⚙️ Installation

1. Clone this repository:

```bash
git clone https://github.com/Careless-Caramel/Ohio-Data-Analysis.git
cd Ohio-Data-Analysis
```

2. Install requirements:

```bash
pip install -r requirements.txt
```

3. Ensure the SQLite database file `data.sqlite3` is present in the project directory.  
   - Convert the provided Excel dataset if needed.  

4. Run the Flask app:

```bash
python app.py
```

5. Open your browser and go to:

```
http://127.0.0.1:8080/
```

---

## ▶️ Usage

### 1️⃣ Web Form

- Enter an **API WELL NUMBER** in the form on the homepage.  
- The app queries the SQLite database and returns:  
  - Total **OIL** produced  
  - Total **GAS** produced  
  - Total **BRINE** produced  

### 2️⃣ Demo

https://github.com/Careless-Caramel/Ohio-Data-Analysis/assets/86556401/7c1fca59-1ebf-47b5-9c36-60ffe53ee938

---

## 📂 Project Structure

```bash
Ohio-Data-Analysis/
│
├── app.py             # Flask application
├── data.sqlite3       # SQLite database (converted from Excel)
├── templates/
│   ├── index.html     # Home page form
│   └── submit.html    # Result page
├── requirements.txt   # Python dependencies
└── README.md          # Project documentation
```

---

## 🤝 Contributing

1. Fork the repository  
2. Create a new branch (`git checkout -b feature-name`)  
3. Commit your changes (`git commit -m "Added new feature"`)  
4. Push to your branch (`git push origin feature-name`)  
5. Open a Pull Request  

---

## 👩‍💻 About

This project demonstrates how to:  
- Convert Excel datasets into **SQLite3** databases  
- Query structured data with **Flask** web apps  
- Build lightweight, interactive data analysis tools 🚀
