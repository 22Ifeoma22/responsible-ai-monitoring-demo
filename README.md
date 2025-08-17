# responsible-ai-monitoring-demo
Responsible AI Monitoring Demo A showcase project demonstrating automated monitoring, auditing, and reporting of machine learning models for fairness, bias, and drift using GitHub Actions. Includes explainability checks (SHAP/LIME), fairness audits (Fairlearn/Aequitas), and automated evidence logging for compliance and governance.
![RAI Monitoring](https://github.com/22Ifeoma22/responsible-ai-monitoring-demo/actions/workflows/monitoring.yml/badge.svg)
## Demo Evidence
Each run produces:
- Fairness audit: [CSV artifact]
- Explainability: SHAP summary plot
- Model performance: JSON report
- Governance log: commit SHA + timestamp
##  Evidence Showcase: Responsible AI Monitoring

This project demonstrates how **governance evidence** can be automated using GitHub Actions.  
Every run of the monitoring workflow produces a set of auditable artifacts that can be downloaded from the **Actions → Artifacts** tab.  

###  What gets produced
- **Fairness Audit** (`fairness_audit.csv`)  
  - Group metrics including **selection rate, true positive rate (TPR), false positive rate (FPR)** broken down by sensitive attributes (e.g., sex, race).  

- **Explainability Report** (`shap_summary.png`)  
  - SHAP summary plot showing which features drive predictions the most, for transparency and interpretability.  

- **Performance Report** (`model_performance.json`)  
  - Standard ML metrics (**accuracy, F1, precision, recall**) for tracking overall model quality.  

- **Governance Log** (`run_log.json`)  
  - Automatically records:
    - Commit SHA  
    - UTC timestamp of run  
    - Dataset used  
    - Sensitive attributes audited  
    - Paths to all generated artifacts  

###  Example Workflow Output
![RAI Monitoring](https://github.com/22Ifeoma22/responsible-ai-monitoring-demo/actions/workflows/monitoring.yml/badge.svg)

 With each commit, the workflow automatically runs **fairness, explainability, and performance checks** and stores results as artifacts — ensuring traceability, compliance, and accountability in the ML lifecycle.
