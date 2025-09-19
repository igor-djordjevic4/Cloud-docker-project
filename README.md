# FastAPI Project Setup

Ovaj dokument opisuje kako da pokrenete FastAPI projekat i pripremite razvojno okruženje.

---

## 1. Instalacija Python i virtualnog okruženja

1. Preuzmite i instalirajte Python (preporučena verzija: **3.11+**).
2. Kreirajte virtualno okruženje u root folderu projekta:
   ```bash
   python -m venv .venv
## 2. Instalacija potrebnih paketa
pip install fastapi uvicorn sqlalchemy pydantic python-dotenv

## 3. Za pokretanje i debugovanje FastAPI projekta u VS Code, kreirajte .vscode/launch.json fajl sa sledećim sadržajem:

```bash
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Module",
            "type": "debugpy",
            "request": "launch",
            "module": "uvicorn",
            "args": ["app.main:app", "--reload"]
        }
    ]
}
