# 2‑Week Build‑Focused ML Plan — India‑Industry frameworks
## Assumptions
- Time: 3–4 hrs/day  
- Frameworks: Python, scikit‑learn, PyTorch, TensorFlow/Keras, Hugging Face, Spark (optional), FastAPI, Docker, MLflow/ONNX

---

## Week 1 — Core builds (one per day)
- [ ] Day 1 — Tabular pipeline (scikit‑learn + joblib)  
  - Dataset chosen (CSV/UCI)  
  - Pipeline: Imputer → Encoder → Scaler → Model (RandomForest or XGBoost via sklearn API)  
  - Cross‑val, metrics, joblib export, notebook + README

- [ ] Day 2 — Production PyTorch model  
  - Dataset/DataLoader, model class, train/val loop, lr scheduler, checkpoint (state_dict)  
  - inference script, notebook + README

- [ ] Day 3 — Keras / TensorFlow model  
  - Functional API model, compile, fit, EarlyStopping, ModelCheckpoint, TensorBoard logging  
  - saved_model export, inference script, README

- [ ] Day 4 — NLP with Hugging Face  
  - Fine‑tune pretrained model (DistilBERT/BERT) for classification (Trainer or PyTorch loop)  
  - Save model + tokenizer, evaluation report, README

- [ ] Day 5 — Large‑data preprocessing (Spark ML or Dask)  
  - Scalable feature extraction on sampled dataset, export feature table for modeling, README

- [ ] Day 6 — Reproducibility & experiment logging  
  - YAML/JSON config, fixed seeds, requirements.txt, MLflow or CSV experiment logs

- [ ] Day 7 — Transfer learning (CV)  
  - Fine‑tune pretrained CNN (ResNet/MobileNet) in PyTorch or Keras, augmentations, checkpointing, README

---

## Week 2 — Production readiness, tooling, demo
- [ ] Day 8 — Serving + Docker  
  - Wrap one model in FastAPI, pydantic input validation, health endpoint, Dockerfile

- [ ] Day 9 — Model optimization (ONNX / quantization)  
  - Convert model to ONNX, run latency test, try post‑training quantization

- [ ] Day 10 — CI & tests  
  - Unit tests for transforms, smoke training test, GitHub Actions workflow to run tests

- [ ] Day 11 — Monitoring & logging  
  - Integrate simple metrics export (Prometheus client or MLflow metrics), add /metrics endpoint

- [ ] Day 12 — Take‑home mini challenge  
  - 2–3 hr task: improve a model (feature, augmentation, hyperparam), commit changes, update README

- [ ] Day 13 — Docs & talking points  
  - One‑page README per project, 3 talking points (problem → approach → results), sample requests

- [ ] Day 14 — Final demo & release  
  - Record 3–5 min demo (screen/GIF) for one project, tag release, cleanup

---

## Deliverables (end of 2 weeks)
- [ ] Projects: scikit‑learn, PyTorch, TensorFlow/Keras, Hugging Face, Spark sample  
- [ ] Dockerized FastAPI demo (one model)  
- [ ] ONNX conversion / quantization example  
- [ ] CI workflow + basic tests  
- [ ] README per project, experiment logs, demo recording

---

## Daily mini‑habits (15–45 min)
- [ ] Timed coding problem (DS/algos) — 2×/week  
- [ ] Read one API snippet or example for PyTorch/TF/HF — daily quick review  
- [ ] Log experiment results & keep one‑page cheatsheet for common commands

---
