# 🚀 NexusView

[![PyPI version](https://img.shields.io/pypi/v/nexusview-musharraf.svg)](https://pypi.org/project/nexusview-musharraf/)
[![Python versions](https://img.shields.io/pypi/pyversions/nexusview-musharraf.svg)](https://pypi.org/project/nexusview-musharraf/)
[![License](https://img.shields.io/github/license/Musharraf-Bubere/NexusView.svg)](https://github.com/Musharraf-Bubere/NexusView/blob/main/LICENSE)

---

## 📌 Overview

**NexusView** is a lightweight Python library designed for Data Scientists and Jupyter Notebook users.

It allows you to seamlessly:

- 🌐 Render live websites  
- 📺 Embed YouTube videos  

👉 directly inside your notebook environment without switching tabs.

---

## ✨ Features

- 🌐 **Website Rendering**  
  Render any valid website inside Jupyter Notebook

- 📺 **YouTube Integration**  
  Automatically extract and embed YouTube videos from URLs

- ⚙️ **Customizable Display**  
  Control width and height of embedded content

- 🧠 **Smart Error Handling**  
  Custom exceptions for invalid URLs

- 📝 **Logging System**  
  Track execution and debug easily

- ⚡ **Lightweight & Fast**  
  Built using standard Python libraries

---

## 📦 Installation

Install from PyPI:

```bash
pip install nexusview-musharraf
```

---

## 🧑‍💻 Usage

### 📺 Render YouTube Video

```python
from nexusview.youtube import render_youtube_video

render_youtube_video("https://youtu.be/dQw4w9WgXcQ")
```

---

### 🌐 Render Website

```python
from nexusview.site import render_site

render_site("https://example.com")
```

---

## 📁 Project Structure

```
NexusView/
│
├── .github/workflows/
│   ├── ci.yml
│   └── python-publish.yml
│
├── src/
│   └── nexusview/
│       ├── __init__.py
│       ├── logger.py
│       ├── custom_exception.py
│       ├── youtube.py
│       └── site.py
│
├── tests/
│   ├── unit/
│   └── integration/
│
├── setup.py
├── setup.cfg
├── pyproject.toml
├── tox.ini
├── requirements.txt
├── requirements_dev.txt
├── README.md
```

---

## ⚙️ Requirements

- Python >= 3.8

---

## 🧪 Testing

Run tests using:

```bash
tox
```

---

## 🔄 CI/CD

This project includes:

- ✅ GitHub Actions (CI pipeline)
- ✅ Multi-OS testing (Linux, Windows)
- ✅ Multiple Python versions (3.8, 3.9)
- ✅ Automated PyPI publishing

---

## 🧠 How It Works

### YouTube Rendering

- Extracts video ID using regex  
- Generates embed URL  
- Displays using HTML iframe  

---

### Website Rendering

- Validates URL using `urllib`  
- Checks HTTP response (200 OK)  
- Displays using Jupyter `IFrame`

---

## ⚠️ Limitations

Some websites may not render due to:

```
X-Frame-Options security policy
```

Examples:

- Google ❌  
- Some secure websites ❌  

---

## 📜 License

This project is licensed under the **Apache License**.

---

## 👨‍💻 Author

**Musharraf Bubere**

- GitHub: https://github.com/Musharraf-Bubere

---

## ⭐ Support

If you like this project:

- ⭐ Star the repository  
- 🍴 Fork it  
- 📢 Share with others  

---

## 🚀 Future Improvements

- Add more content renderers (PDF, images, etc.)
- Add validation utilities
- Improve UI/UX rendering
- Add documentation website

---