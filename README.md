# 🚀 NexusView

![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-Apache-green)

---

## 📌 Overview

**NexusView** is a lightweight Python library designed for Data Scientists and Jupyter Notebook users.

It allows you to seamlessly:

- 🌐 Render live websites
- 📺 Embed YouTube videos  
directly inside your notebook environment.

👉 No need to switch tabs — view everything inside your notebook.

---

## ✨ Features

- 🌐 **Website Rendering**  
  Render any valid website inside a notebook cell

- 📺 **YouTube Integration**  
  Automatically extract and embed YouTube videos from URLs

- ⚙️ **Customizable Display**  
  Control width, height, and layout

- 🧠 **Smart Error Handling**  
  Custom exceptions for invalid inputs

- 📝 **Logging System**  
  Track execution with detailed logs

- ⚡ **Lightweight**  
  Built using standard Python libraries

---

## 📦 Installation

Install using pip:

```bash
pip install nexusview
```

---

## 🧑‍💻 Usage

### 📺 Render YouTube Video

```python
from nexusview.youtube import render_youtube_video

render_youtube_video("https://youtu.be/your_video_id")
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
nexusview/
│
├── logger.py
├── custom_exception.py
├── youtube.py
├── site.py
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

- ✅ GitHub Actions
- ✅ Multi-OS testing
- ✅ PyPI publishing pipeline

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

👉 Star the repository  
👉 Share with others  

---
