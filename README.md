# 📊 Quote Scraper & Visualizer

This is a comprehensive **Data Analysis & GUI Application** built with Python. It scrapes quote data from [quotes.toscrape.com](http://quotes.toscrape.com), processes it using Pandas, and provides interactive visualizations through a Tkinter interface.

## 🚀 Features

* **Web Scraping:** Fetches quotes, authors, and tags dynamically using `BeautifulSoup` and `requests`.
* **Data Filtering:** Allows filtering quotes by specific tags (e.g., 'love', 'inspirational').
* **Data Visualization:**
    * 📊 **Bar Chart:** Top 10 authors with the most quotes.
    * 🍰 **Pie Chart:** Distribution of the top 5 tags.
    * 📈 **Line Chart:** Analysis of quote lengths.
    * 🔥 **Heatmap:** Correlation between authors and tags using `Seaborn`.
* **Data Export:** Saves scraped data to CSV format.

## 🛠️ Libraries Used

* **Tkinter:** User Interface (GUI).
* **BeautifulSoup4 & Requests:** Web Scraping.
* **Pandas:** Data manipulation and analysis.
* **Matplotlib & Seaborn:** Advanced data visualization.

## ⚙️ Installation & Usage

1.  Clone the repository:
    ```bash
    git clone [https://github.com/KULLANICI-ADIN/REPO-ADIN.git](https://github.com/KULLANICI-ADIN/REPO-ADIN.git)
    ```
2.  Install the required libraries:
    ```bash
    pip install beautifulsoup4 requests pandas matplotlib seaborn
    ```
3.  Run the application:
    ```bash
    python main.py
    ```
4.  Click **"Scrape & Save Data"** to fetch data, then use the plotting buttons to visualize insights.

---
Author: Zeynep Gürbüz
