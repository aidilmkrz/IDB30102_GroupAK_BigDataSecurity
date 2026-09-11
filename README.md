# IDB30102 - Research Methodology
## A Comparative Evaluation of k-Anonymity and Differential Privacy in Big Data Systems

---

### 📌 Course & Project Information
* **Course Code:** IDB30102
* **Course Name:** Research Methodology
* **Project Title:** A Comparative Evaluation of k-Anonymity and Differential Privacy in Big Data Systems
* **Group Name / ID:** GROUP AK
* **Assigned Research Area:** Big Data Security & Data Privacy

---

### 👥 Group Members
| Name | Student ID | Role / Contribution |
| :--- | :---: | :--- |
| **Muhammad Aidil Mukhriz Bin Khairol Afandi** | 52215226072 | Literature Review & Framework Design |
| **Nurul Nadia Binti Khairuddin** | 52215226154 | Methodology & Architecture Diagram |
| **Nadiah Izzati Binti Noor Aziddin** | 52215226024 | Data Preparation & System Evaluation |
| **Haiqal Imanshah Bin Hazmad Balkish** | 52215125083 | Source Code Implementation & Documentation |

---

### 📖 Project Overview

#### **Research Problem**
1. **Inconsistent Evaluation Standards (PS1):** $k$-Anonymity and Differential Privacy are frequently evaluated in literature using different metrics, experimental setups, and datasets, making direct comparative assessment difficult.
2. **Lack of Benchmarking Criteria (PS2):** There is limited consistent comparison between the two techniques using unified criteria such as accuracy, re-identification risk, and execution time under identical conditions.

#### **Research Aim**
To conduct a direct, standardized comparative evaluation of $k$-Anonymity and Differential Privacy in big data systems based on three key performance metrics: **classification accuracy**, **re-identification risk**, and **execution time**.

#### **Research Objectives**
1. **RO1:** To review existing literature on $k$-Anonymity and Differential Privacy techniques in big data systems.
2. **RO2:** To implement $k$-Anonymity and Differential Privacy using a custom Python implementation (`anonymization_framework.py`) on the UCI Adult Census Income dataset.
3. **RO3:** To evaluate and compare both techniques against the original, unprotected dataset using accuracy, re-identification risk, and execution time as primary metrics.

#### **Implementation Scope**
The evaluation framework processes raw tabular data through two privacy-preserving techniques alongside an unprotected baseline:
* **Baseline (Raw Data):** Unprotected original dataset.
* **$k$-Anonymity ($k=3$):** Applies quasi-identifier generalization (age range categorization, marital-status grouping) and suppression.
* **Differential Privacy ($\epsilon=1.0$):** Injects calibrated Laplace noise into numerical attributes to provide formal privacy guarantees.

---

### 🔬 Methodology & System Architecture

#### **Research Methodology & Development Model**
This study adopts a data-driven research approach following the **CRISP-DM (Cross-Industry Standard Process for Data Mining)** framework, comprising 6 phases:
1. **Business Understanding:** Define research problems, trade-off scope, and evaluation criteria.
2. **Data Understanding:** Analyze UCI Adult Census Income dataset attributes and quasi-identifiers.
3. **Data Preparation:** Preprocess tabular features and construct anonymization transformation functions.
4. **Modelling:** Treat $k$-Anonymity and Differential Privacy as separate comparison treatments.
5. **Evaluation:** Benchmark accuracy, re-identification risk, and processing time against baseline.
6. **Deployment:** Document comparative results, findings, and maintain GitHub repository.

#### **System Architecture Workflow**
```text
[ UCI Adult Benchmark Dataset ]
│
┌───────────────────────┼───────────────────────┐
▼ ▼ ▼
┌──────────────┐ ┌─────────────────────┐ ┌──────────────┐
│ Baseline │ │ k-Anonymity │ │ Differential │
│ (Raw Data) │ │ (k=3 Generalization)│ │ Privacy │
└──────┬───────┘ └──────────┬──────────┘ │ (ε=1.0 Noise)│
│ │ └──────┬───────┘
▼ ▼ ▼
┌──────────────┐ ┌─────────────────────┐ ┌──────────────┐
│ Metrics │ │ Metrics │ │ Metrics │
│ Eval Engine │ │ Eval Engine │ │ Eval Engine │
└──────┬───────┘ └──────────┬──────────┘ └──────┬───────┘
│ │ │
└────────────────────────┼───────────────────────┘
▼
[ Comparative Evaluation ]
(Accuracy, Re-ID, Time)
│
▼
[ Comparative Results ]
```
---

### 🧪 Evaluation Plan & Metrics

* **Baseline:** Original unmodified UCI Adult dataset (100% Re-ID risk, zero privacy noise).
* **Dataset / Test Environment:**
* *Dataset:* UCI Adult Census Income Benchmark Dataset (`adult_sample.csv`).
* *Environment:* Python 3.8+ running local execution environment.
* **Evaluation Metrics:**
* **Classification Accuracy (%):** Evaluates data utility retained after privacy treatment.
* **Re-Identification Risk (%):** Measures residual vulnerability to linkage attacks.
* **Execution Time (ms):** Measures computational performance and algorithm latency.

---

### 💻 Technical Stack

* **Programming Language:** Python 3.8+
* **Libraries:** `pandas`, `numpy`, `math`, `time`
* **Benchmark Dataset:** UCI Adult Census Income Dataset (`adult_sample.csv`)
* **Environment:** VS Code / Jupyter Notebook / Git & GitHub

---

### 📂 Repository Structure

* 📄 [README.md](./README.md) — *Comprehensive project overview and instructions*
* 📁 [01_Research_Papers/](./01_Research_Papers/) — *Primary literature resources and references*
* 📁 [02_Literature_Review/](./02_Literature_Review/) — *Literature review synthesis and matrix*
* 📁 [03_Architecture_and_Flowchart/](./03_Architecture_and_Flowchart/) — *System architecture & CRISP-DM flowcharts*
* 📁 [04_Source_Code/](./04_Source_Code/) — *Custom Python implementation (anonymization_framework.py)*
* 📁 [05_Data_or_Sample_Input/](./05_Data_or_Sample_Input/) — *Benchmark datasets (adult_sample.csv)*
* 📁 [06_Results_or_Expected_Output/](./06_Results_or_Expected_Output/) — *Metric evaluation logs, output figures, and tables*
* 📁 [07_References/](./07_References/) — *Reference citations formatted in APA 7th Edition*

---

### 🚀 Getting Started & Running the Code

#### **1. Installation**
Ensure Python 3.8+ is installed, then install required dependencies:
```bash
pip install pandas numpy
```
#### **2. Execution**
Navigate to the `04_Source_Code/` directory and execute the main anonymization engine:
```bash
python main_anonymizer.py
```

---

### **📊 Summary of Results**
Preliminary benchmarking on the sample input dataset yielded the following performance metrics:

| **Technique / Treatment** | **Accuracy (%)** | **Re-ID Risk (%)** | **Execution Time (ms)** |
| :--- | :---: | :--- | :--- |
| Baseline (Raw Data) | 33.33% | 100.00% | 285.66 ms |
| k-Anonymity ($k=3$) | 33.33% | 60.00% | 114.34 ms |
| Differential Privacy ($\epsilon=1.0$) | 33.33% | 90.00% | 110.57 ms |

---

### **📜 Acknowledgments & Citation**
This project is submitted to Dr. Delina Beh Mei Yin in partial fulfillment of the requirements for IDB30102 Research Methodology, Bachelor of Cybersecurity Technology with Honours, University of Kuala Lumpur (UniKL).
