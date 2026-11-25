# Automated Resume Screening Tool

An industry-oriented ML/NLP candidate screening system that ingests multi-format resumes (`.pdf`, `.docx`, `.txt`), extracts skills, years of experience, and education, computes TF-IDF + cosine similarity against a Job Description, flags must-have skill gaps, ranks candidates with human-readable explanations, and exposes results via a **FastAPI** backend and **Next.js + Tailwind CSS** recruiter dashboard.

---

## Problem Statement
Recruiters and HR teams often receive hundreds of resumes per open role. Manual screening is slow, inconsistent, and prone to missing qualified candidates or overlooking critical must-have gaps.

## Industry Relevance
- **HR Tech & ATS Platforms**: Implements document ingestion, skill taxonomy normalization, vector similarity scoring, and transparent ranking explanations.
- **Data Science / ML & NLP Roles**: Demonstrates TF-IDF vectorization (`scikit-learn`), cosine similarity, regex information extraction, and multi-factor weighted scoring.
- **Backend & Full-Stack Roles**: Exposes production-style FastAPI endpoints, Pydantic validation, automated `pytest` tests, CSV/PNG reporting, and a Next.js TypeScript recruiter UI.

---

## Features
- **Multi-Format Resume Extraction**: Parses `.pdf`, `.docx`, and `.txt`/`.md` resumes (`src/extractor.py`).
- **Skill Taxonomy & Experience Parsing**: Normalizes aliases (`sklearn` → `scikit-learn`, `postgres` → `postgresql`, `js` → `javascript`), detects degrees, and extracts years of experience (`src/skill_extractor.py`).
- **Explainable Hybrid Scoring**: Combines Must-Have Skill Coverage (45%), TF-IDF Cosine Similarity (30%), Nice-to-Have Skills (15%), and Experience Match (10%) (`src/scorer.py`).
- **Must-Have Gap Flagging**: Explicitly flags missing required skills so recruiters know *why* a candidate is Shortlisted, Borderline, or Rejected.
- **FastAPI REST API + Swagger UI**: Upload resumes, run sample simulations, fetch JSON results, and export CSV reports (`api/app.py`).
- **Next.js Recruiter Dashboard**: Interactive TypeScript + Tailwind CSS dashboard (`apps/web/app/page.tsx`).
- **Reports & Visualization**: Generates `outputs/screening_report.csv`, `outputs/screening_report.json`, and `images/candidate_ranking_chart.png`.

---

## Tech Stack
- **Language**: Python 3.11+
- **ML / NLP**: `scikit-learn` (`TfidfVectorizer`, `cosine_similarity`), `pandas`, `numpy`, `re`
- **Document Parsing**: `pdfplumber`, `pypdf`, `python-docx` (with built-in pure-Python fallbacks)
- **Backend API**: `FastAPI`, `Uvicorn`, `Pydantic`, `python-multipart`
- **Frontend Dashboard**: Next.js (App Router), React, TypeScript, Tailwind CSS (`apps/web/`)
- **Reporting & Testing**: `matplotlib`, `pytest`, `httpx`

---

## Folder Structure
```text
Automated-Resume-Screening-Tool/
├── api/                     # FastAPI REST backend (app.py)
├── apps/web/                # Next.js + TypeScript + Tailwind recruiter dashboard
├── data/                    # Sample job_description.json
├── docs/                    # Architecture diagram & scoring notes
├── images/                  # Generated Matplotlib candidate ranking chart
├── outputs/                 # Generated screening_report.csv & screening_report.json
├── resumes/                 # Sample & uploaded resumes (.pdf, .docx, .txt)
├── src/                     # Modular ML/NLP pipeline (extractor, cleaner, scorer, etc.)
├── tests/                   # Automated pytest unit & API tests
├── .gitignore               # Ignores venv, __pycache__, node_modules, .next
├── main.py                  # CLI virtual simulation & report runner
└── requirements.txt         # Python dependencies
```

---

## How to Run

### 1. Setup Python Environment
```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

pip install -r requirements.txt
```

### 2. Run CLI Virtual Simulation
Generates synthetic `.pdf`, `.docx`, and `.txt` resumes if missing, runs the ML/NLP pipeline, and exports CSV/JSON/PNG outputs:
```bash
python main.py --seed-samples
```

### 3. Run FastAPI Backend
```bash
uvicorn api.app:app --reload
```
Open `http://127.0.0.1:8000/docs` for interactive Swagger documentation.

### 4. Run Next.js Recruiter Dashboard (Optional UI)
```bash
cd apps/web
npm install
npm run dev
```
Open `http://localhost:3000`.

### 5. Run Automated Tests
```bash
pytest -v
```

---

## Sample Output
- Ranked console summary with decision (`Shortlisted`, `Borderline`, `Rejected`), must-have skill gaps, and natural-language explanations.
- `outputs/screening_report.csv` for HR spreadsheet review.
- `images/candidate_ranking_chart.png` visualizing candidate scores against the shortlist cutoff.

---

## Learning Outcomes
- Built an end-to-end NLP document ingestion and TF-IDF ranking pipeline.
- Designed explainable scoring instead of opaque black-box rejections.
- Built and tested a FastAPI backend alongside a typed Next.js recruiter dashboard.
