# 🧭 Task Tracker CLI

Jednoduchá **CLI aplikace v Pythonu** pro správu úkolů přímo z příkazové řádky.  
Projekt jsem vytvořil jako trénink objektově orientovaného programování a práce se soubory (JSON).

---

## 🚀 Funkce

- Přidávání, mazání a úprava úkolů  
- Označení úkolu jako **done** nebo **in progress**  
- Výpis všech úkolů nebo jen podle stavu  
- Data se ukládají do souboru `data/tasks.json`  
- Při dalším spuštění se úkoly znovu načtou  

---

## 💻 Ukázka použití

```bash
# Přidání nového úkolu
python3 main.py add "Napsat README"

# Úprava popisu úkolu
python3 main.py update 1 "Napsat README pro Task Tracker"

# Označení jako hotové
python3 main.py done 1

# Označení jako rozpracované
python3 main.py progress 2

# Výpis všech úkolů
python3 main.py list-all

# Výpis hotových úkolů
python3 main.py list-done
```
---

## Struktura projektu
```bash
task-tracker/
│
├── task_tracker/
│   ├── main.py          # hlavní vstupní bod aplikace (CLI logika)
│   ├── models.py        # třídy Task a TaskManager
│   ├── storage.py       # ukládání/načítání JSON dat
│   ├── utils.py         # parser argumentů a menu
│   ├── constants.py     # cesty k souborům apod.
│
├── data/
│   └── tasks.json       # automaticky vytvořený datový soubor
│
├── README.md
├── .gitignore
└── requirements.txt
```
---

## Instalace a spuštění
1. Naklonuj repozitář
```bash
git clone https://github.com/heysmtk/task-tracker.git
cd task-tracker-cli/task_tracker
```
2. Spusť první příkaz
```bash
python3 main.py add "Koupit kafe"
```
---

## License
MIT License

Copyright (c) 2025 Tomáš Smutek

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
