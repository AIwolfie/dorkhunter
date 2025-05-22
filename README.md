

# 🔎 DorkHunter

A powerful and simple **CLI tool** to perform **dork-based searches** using **Google** and **DuckDuckGo** search engines. Perfect for reconnaissance, OSINT investigations, and bug bounty hunting!

---

## 📌 Features

- ✅ Google search support via `googlesearch-python`
- ✅ DuckDuckGo support via `duckduckgo-search`
- ✅ Save all results to a file
- ✅ Colored, formatted terminal output
- ✅ Counts unique results
- ✅ Optional search engine selection (`--google`, `--duck`)
- ✅ Simple usage for beginners and pros

---

## ⚙️ Installation

> 🐍 Requires **Python 3.6+**

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/dorkhunter.git
cd dorkhunter
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

If you don’t have `requirements.txt`, just install manually:

```bash
pip install googlesearch-python duckduckgo-search
```

---

## 🚀 Usage

```bash
python3 dorkHunter.py -q "<your dork>" [options]
```

### 🔧 Options

| Flag             | Description                                  |
| ---------------- | -------------------------------------------- |
| `-q`, `--query`  | The dork/search string to query              |
| `-l`, `--limit`  | Number of results per engine (default: 10)   |
| `-o`, `--output` | Save results to a file (e.g., `results.txt`) |
| `--google`       | Use only Google for search                   |
| `--duck`         | Use only DuckDuckGo for search               |

> **Note:** If no engine is specified, both are used by default.

---

### 🧪 Examples

Search for directory listings:

```bash
python3 dorkHunter.py -q 'intitle:"index of" "admin"' -l 20
```

Search using only DuckDuckGo:

```bash
python3 dorkHunter.py -q 'site:.gov confidential' --duck
```

Save output to a file:

```bash
python3 dorkHunter.py -q 'inurl:login.php' -o logins.txt
```

---

## 📁 Output

* Results are displayed with color-coded indexing.
* If `-o` is used, results are saved in plain `.txt` format.
* Duplicate URLs are automatically removed before saving.

---

## 🧰 Dependencies

* [`googlesearch-python`](https://pypi.org/project/googlesearch-python/)
* [`duckduckgo-search`](https://pypi.org/project/duckduckgo-search/)

Install them with:

```bash
pip install googlesearch-python duckduckgo-search
```

---

## ⚠️ Legal Disclaimer

> **DorkHunter is intended for educational and ethical purposes only.**
>
> Misusing this tool for unauthorized access or illegal activity is strictly prohibited. The developer is **not responsible** for any misuse or damage caused by this script.

---

## 🙌 Credits

* Built by [AIwolfie](https://github.com/AIwolfie)
* Inspired by the need for a quick CLI dork searcher for bug bounty and OSINT work.


