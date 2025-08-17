import os
import pandas as pd
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from fairlearn.metrics import MetricFrame, selection_rate, true_positive_rate, false_positive_rate

def main():
    print(">>> Loading dataset...")
    adult = fetch_openml("adult", version=2, as_frame=True)
    df = adult.frame

    y = (df["class"] == ">50K").astype(int)
    X = df.drop(columns=["class"])
    A = X["sex"]  # sensitive attribute

    cat_cols = X.select_dtypes(include=["object", "category"]).columns.tolist()
    X = pd.get_dummies(X, columns=cat_cols, drop_first=True)

    X_train, X_test, y_train, y_test, A_train, A_test = train_test_split(
        X, y, A, test_size=0.25, random_state=42, stratify=y
    )

    print(">>> Training RandomForest...")
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)

    acc = accuracy_score(y_test, y_pred)
    print(f"Accuracy: {acc:.3f}")

    metrics = {
        "selection_rate": selection_rate,
        "tpr": true_positive_rate,
        "fpr": false_positive_rate,
    }
    mf = MetricFrame(metrics=metrics, y_true=y_test, y_pred=y_pred, sensitive_features=A_test)
    print(mf.by_group)

    os.makedirs("artifacts", exist_ok=True)
    mf.by_group.to_csv("artifacts/fairness_audit.csv")
    print("Audit results saved → artifacts/fairness_audit.csv")

if __name__ == "__main__":
    main()
