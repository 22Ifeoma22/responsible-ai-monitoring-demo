# responsible-ai-monitoring-demo
Responsible AI Monitoring Demo A showcase project demonstrating automated monitoring, auditing, and reporting of machine learning models for fairness, bias, and drift using GitHub Actions. Includes explainability checks (SHAP/LIME), fairness audits (Fairlearn/Aequitas), and automated evidence logging for compliance and governance.
![RAI Monitoring](https://github.com/22Ifeoma22/responsible-ai-monitoring-demo/actions/workflows/monitoring.yml/badge.svg)
## Demo Evidence
Each run produces:
- Fairness audit: [CSV artifact]
- Explainability: SHAP summary plot
- Model performance: JSON report
- Governance log: commit SHA + timestamp
