# DesktopApp

**Cross‑platform Desktop Application (Electron + Python) — Educational Portfolio Project**

> *Short:* A minimal, well‑structured Electron app that integrates Python for backend/data processing. Built as an educational project to demonstrate desktop app architecture, cross-language integration, and secure testing practices.

---

## 📌 Overview

DesktopApp is a cross‑platform desktop application scaffolded with the Electron framework for the UI layer and Python for backend processing tasks. This repository is a **learning / portfolio** project designed to showcase how to structure a hybrid desktop app, how to call Python from an Electron front end, and how to keep development and testing safe and ethical.

> ⚠️ **Important (Ethics & Scope):**
> This project is for **educational purposes only**. It does **not** include or condone any unauthorized data-capturing or surveillance features. Any real data collection must be opt‑in and clearly documented with user consent.

---

## 🎯 Purpose (Why this project exists)

- Demonstrate an Electron + Python integration pattern suitable for desktop tools.
- Showcase clean separation between UI (Electron/JavaScript) and backend logic (Python).
- Provide an example of how to design and test potentially sensitive features **ethically** in isolated lab environments (VMs/snapshots).
- Act as a portfolio piece: clear README, example scripts, and instructions to run locally.

---

## 🛠️ Technologies

- **Electron** — Desktop shell & UI
- **JavaScript / Node.js** — Frontend and inter-process logic
- **Python** — Backend processing scripts (called from the Electron app)
- `child_process` / IPC — For bridging Electron ↔ Python

---

## ✨ Key Features (Portfolio-friendly)

- Clean project structure and modular code to highlight architecture skills
- Example integration: Electron calls a Python script and displays processed results
- Cross‑platform packaging-ready structure (notes on packaging for Windows/macOS/Linux)
- Accessibility and UX considerations (keyboard shortcuts, clear dialogs)
- Privacy-first design: any telemetry or logging is **opt-in only** and documented

---

## 🔒 Ethics & Safe Testing

If you’re studying security and analysis, follow safe practices:

- Use an isolated Virtual Machine (VirtualBox/VMware) and create snapshots before testing.
- Avoid connecting the test VM to production networks when running untrusted code.
- Do not include or distribute code that captures user input (keystrokes) without explicit consent.
- Document any simulated data flows you use for demonstration purposes.

---

## ⚙️ How to run (development)

1. Install Node.js and Python (recommended versions listed in `env.md` or `requirements.txt`).
2. Install dependencies:

```bash
npm install
pip install -r requirements.txt
```

3. Start app in development mode:

```bash
npm start
```

4. Example: From the UI, click **Run Analysis** to trigger a Python script that returns processed output shown in the app window.

---

## 🧪 Testing / Packaging notes

- **Packaging:** Use `electron-builder` or `electron-forge` to create platform builds. Keep large binary artifacts out of Git; use Releases or Git LFS if needed.
- **Testing:** For security experiments, prefer simulated datasets and explicit consent flows. Keep all sensitive testing inside an isolated lab.

---

## 📁 Recommended `.gitignore` (short)

```
node_modules/
dist/
build/
*.exe
*.dll
*.pdb
*.log
.env
```

---

## 🧾 Files in this repo

- `main.js` — Electron main process entry
- `renderer/` — Frontend UI code
- `python/` — Python scripts used for data processing (examples only)
- `requirements.txt` — Python dependencies
- `package.json` — Node/Electron dependencies and scripts
- `README.md` — This file

---

## 🧭 Contribution & License

This repository is meant to be a portfolio/demo. If you accept contributions, state expectations (code style, tests, no privacy-invasive features). Add a license (e.g., MIT) or change as desired.

---

## 📬 Contact

Include your preferred contact or portfolio link (e.g., your email or personal website) so reviewers can find more of your work.

---

# DesktopApp (สำหรับ Portfolio — ภาษาไทย)

DesktopApp เป็นโปรเจกต์ตัวอย่างสำหรับ portfolio ที่แสดงการผสาน Electron (UI) กับ Python (Backend) โดยเน้นสถาปัตยกรรมที่ชัดเจนและแนวทางการทดสอบที่ปลอดภัย

## จุดประสงค์

- แสดงทักษะการออกแบบแอปเดสก์ท็อปข้ามแพลตฟอร์ม
- แสดงการเรียกใช้งาน Python จาก Electron ผ่าน IPC/child_process
- แสดงความรับผิดชอบด้านจริยธรรมและความเป็นส่วนตัวเมื่อทำงานกับข้อมูลที่อ่อนไหว
- เป็นตัวอย่างผลงานที่จัดทำเป็น portfolio พร้อม README และตัวอย่างสคริปต์

## วิธีรัน (ย่อ)

```bash
npm install
pip install -r requirements.txt
npm start
```

## หมายเหตุด้านจริยธรรม

โปรเจกต์นี้ใช้เพื่อการศึกษาเท่านั้น และจะ **ไม่** ดักจับหรือส่งข้อมูลการพิมพ์ของผู้ใช้โดยไม่ได้รับความยินยอม

## เทคโนโลยี

- Electron — สำหรับ UI และ Desktop shell
- JavaScript / Node.js — Frontend และ logic ของ app
- Python — Backend processing
- child_process / IPC — สำหรับเชื่อมต่อ Electron ↔ Python

---

## ไฟล์สำคัญใน repo

- `main.js` — entry ของ Electron main process
- `renderer/` — code frontend UI
- `python/` — สคริปต์ Python สำหรับประมวลผลข้อมูล
- `requirements.txt` — dependencies ของ Python
- `package.json` — dependencies และ script ของ Node/Electron
- `README.md` — ไฟล์นี้