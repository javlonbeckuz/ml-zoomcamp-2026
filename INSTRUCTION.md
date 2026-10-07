# ML Zoomcamp: what to do after each lesson

This guide answers 3 questions:

1. What do I do after each video?
2. Where do I put the result?
3. How do I submit the homework?

Every lesson's video link and what to do is in the tables in section 2. To tick off watched videos: `videos.html`.

---

## 0. One-time setup: connect to GitHub

Skip if the repo is already on GitHub. Otherwise run once in PowerShell:

```
cd C:\Users\User\ml-zoomcamp\ml-zoomcamp-2026
gh config set git_protocol https
gh auth setup-git
gh repo create ml-zoomcamp-2026 --public --source=. --push
```

After that `./save.ps1` pushes your work to GitHub.

---

## 1. The 4-step loop for every lesson

| Step | What you do | Where | Time |
|---|---|---|---|
| 1. Watch | Watch the video. If there is code, pause and type it yourself | `XX-module/lesson.ipynb` | during the video |
| 2. Task | Check the table in section 2: 👀 means nothing to do, 💻 means do the "Task" | `XX-module/lesson.ipynb` | 5–15 min |
| 3. Notes (optional) | 2–3 lines: what it is, why it matters | `XX-module/notes.md` | 3 min |
| 4. Save | Once at the end of the day | PowerShell: `./save.ps1 "2.4 validation"` | 1 min |

### How to organize lesson.ipynb

For each lesson add a Markdown heading cell, then code cells:

```
## 2.4 Setting up the validation framework      ← Markdown cell (M key)
[code]                                          ← code from the lesson
### Task                                        ← Markdown cell
[code]                                          ← your own task
```

That way you can find any lesson quickly a month later.

### Rules

- Don't copy Alexey's notebook. Type the code yourself.
- Stuck? Try on your own for 20 minutes, then ask the tutor (below) or Claude Code for a hint.
- Pandas 3: `df['col'].fillna(x, inplace=True)` doesn't work. Write `df['col'] = df['col'].fillna(x)`.
- Course materials: `C:\Users\User\ml-zoomcamp\course\XX-module\` (each lesson has notes in a .md file).

### Course tutor

Click the blue **Ask** button in the bottom-right corner of Jupyter and type your question (Enter sends, Shift+Enter adds a new line, "New chat" starts over). It answers from the course notes, cites the lesson, and gives hints instead of homework solutions.

You can also ask from inside a notebook cell:

```
%ask why do we use log1p on the price?
```

For a long question or an error message, put `%%ask` on the first line of the cell and the text below it. `%ask reset` starts a new conversation. It runs on Qwen; the key is in `.env`. It only works when Jupyter is started from the Desktop "ML Zoomcamp" shortcut.

---

## 2. What to do in each lesson, by module

Legend:

- **👀 Watch only**: watch the video, write nothing.
- **💻 Write code**: while watching, type the code yourself in `XX-module/lesson.ipynb`, then do the "Task".
- **⏭ Skip**: not required.
- **📤 Homework**: watch the Summary video, then solve the homework and submit its GitHub link in the form.

---

### Module 1: Introduction to ML

| Lesson | What to do | Task |
|---|---|---|
| [1.1 Introduction to Machine Learning](https://www.youtube.com/watch?v=Crm_5n4mvmg&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR&index=2) | 👀 Watch only | Nothing to write. Get the idea of features (X) and target (y) |
| [1.2 ML vs Rule-Based Systems](https://www.youtube.com/watch?v=CeukwyUdaz8&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR&index=3) | 👀 Watch only | Understand rules (if/else) vs ML |
| [1.3 Supervised Machine Learning](https://www.youtube.com/watch?v=j9kcEuGcC2Y&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR&index=4) | 👀 Watch only | Remember g(X) ≈ y: regression, classification, ranking |
| [1.4 CRISP-DM](https://www.youtube.com/watch?v=dCa3JvmJbr0&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR&index=5) | 👀 Watch only | Understand the 6 CRISP-DM stages |
| [1.5 Model Selection Process](https://www.youtube.com/watch?v=OH_R0Sl9neM&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR&index=6) | 💻 Write code | Split an array of 20 numbers 60/20/20 with `np.random.permutation` |
| [1.6 Setting up the Environment](https://www.youtube.com/watch?v=pqQFlV3f9Bo&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR) | ⏭ Skip | Environment is already set up (uv + Jupyter) |
| [1.7 Introduction to NumPy](https://www.youtube.com/watch?v=Qa0-jYtRdbY&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR&index=7) | 💻 Write code | Type the lesson's NumPy code yourself. Extra: 3×3 random matrix, column means |
| [1.8 Linear Algebra Refresher](https://www.youtube.com/watch?v=zZyKUeOR4Gg&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR&index=8) | 💻 Write code | `X.T @ X`, `np.linalg.inv`. This is (XᵀX)⁻¹Xᵀy from OLS |
| [1.9 Introduction to Pandas](https://www.youtube.com/watch?v=0j3XK5PsnxA&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR&index=9) | 💻 Write code | Apply the lesson's operations to `data/car_fuel_efficiency_2026.csv` |
| [1.10 Summary](https://www.youtube.com/watch?v=VRrEEVeJ440&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR&index=10) | 👀 + 📤 Homework | 1) Questions: [homework.md](https://github.com/DataTalksClub/machine-learning-zoomcamp/blob/main/cohorts/2026/homework/01-intro/homework.md) 2) Solve in `01-intro/homework.ipynb` 3) `./save.ps1 "hw01"` 4) Submit the GitHub link in the [hw01 form](https://courses.datatalks.club/ml-zoomcamp-2026/homework/hw01) (section 4) |

---

### Module 2: Regression (car prices)

| Lesson | What to do | Task |
|---|---|---|
| [2.1 Car price prediction project](https://www.youtube.com/watch?v=vM3SqPNlStE&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR&index=12) | 👀 Watch only | Understand the target (price) and how error is measured |
| [2.2 Data preparation](https://www.youtube.com/watch?v=Kd74oR4QWGM&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR&index=13) | 💻 Write code | Clean column names with `str.lower().str.replace(' ', '_')` |
| [2.3 Exploratory data analysis](https://www.youtube.com/watch?v=k6k8sQ0GhPM&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR&index=14) | 💻 Write code | Price histogram, then the same after `np.log1p` |
| [2.4 Setting up the validation framework](https://www.youtube.com/watch?v=ck0IfiPaQi0&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR&index=15) | 💻 Write code | 60/20/20 split, `seed=42`. Check the size of all three parts |
| [2.5 Linear regression](https://www.youtube.com/watch?v=Dn1eTQLsOdA&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR&index=16) | 💻 Write code | Compute w0 + Σwᵢxᵢ for one car with a loop |
| [2.6 Linear regression: vector form](https://www.youtube.com/watch?v=YkyevnYyAww&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR&index=17) | 💻 Write code | Rewrite the same with `X.dot(w)` |
| [2.7 Training linear regression: Normal equation](https://www.youtube.com/watch?v=hx6nak-Y11g&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR&index=18) | 💻 Write code | Write `train_linear_regression(X, y)` yourself |
| [2.8 Baseline model for car price prediction project](https://www.youtube.com/watch?v=SvPpMMYtYbU&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR&index=19) | 💻 Write code | 5 numeric columns, `fillna(0)`, first model |
| [2.9 Root Mean Squared Error (RMSE)](https://www.youtube.com/watch?v=0LWoFtbzNUM&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR&index=20) | 💻 Write code | Write `rmse(y, y_pred)` |
| [2.10 Computing RMSE on validation data](https://www.youtube.com/watch?v=rawGPXg2ofE&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR&index=21) | 💻 Write code | `prepare_X(df)` function, RMSE on validation |
| [2.11 Feature engineering](https://www.youtube.com/watch?v=-aEShw4ftB0&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR&index=22) | 💻 Write code | Add an `age` column. How much did RMSE change? |
| [2.12 Categorical variables](https://www.youtube.com/watch?v=sGLAToAAMa4&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR&index=23) | 💻 Write code | Manual one-hot for the 5 most frequent values |
| [2.13 Regularization](https://www.youtube.com/watch?v=91ve3EJlHBc&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR&index=24) | 💻 Write code | XᵀX + r·I. This is Ridge regression |
| [2.14 Tuning the model](https://www.youtube.com/watch?v=lW-YVxPgzQw&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR&index=25) | 💻 Write code | Loop over r = [0, 0.001, 0.01, 0.1, 1, 10], find the best r |
| [2.15 Using the model](https://www.youtube.com/watch?v=KT--uIJozes&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR&index=26) | 💻 Write code | Train on train+val, predict one car's price, `np.expm1` |
| [2.16 Car price prediction project summary](https://www.youtube.com/watch?v=_qI01YXbyro&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR&index=27) | 👀 + 📤 Homework | 1) Questions: [homework.md](https://github.com/DataTalksClub/machine-learning-zoomcamp/blob/main/cohorts/2026/homework/02-regression/homework.md) 2) Solve in `02-regression/homework.ipynb` 3) `./save.ps1 "hw02"` 4) Submit the GitHub link in the [hw02 form](https://courses.datatalks.club/ml-zoomcamp-2026/homework/hw02) (section 4) |

Transfer exercise (`transfer/02-regression.ipynb`): apply the same method to other data, e.g. apartment prices.

---

### Module 3: Classification (customer churn)

| Lesson | What to do | Task |
|---|---|---|
| [3.1 Churn prediction project](https://www.youtube.com/watch?v=0Zw04wdeTQo&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR) | 👀 Watch only | Understand churn and how a model saves the business money |
| [3.2 Data preparation](https://www.youtube.com/watch?v=VSGGU9gYvdg&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR) | 💻 Write code | `pd.to_numeric(..., errors='coerce')`, fill missing values |
| [3.3 Setting up the validation framework](https://www.youtube.com/watch?v=_lwz34sOnSE&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR) | 💻 Write code | 60/20/20 with `train_test_split` |
| [3.4 EDA](https://www.youtube.com/watch?v=BNF1wjBwTQA&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR) | 💻 Write code | Overall churn rate, list of categorical columns |
| [3.5 Feature importance: Churn rate and risk ratio](https://www.youtube.com/watch?v=fzdzPLlvs40&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR) | 💻 Write code | Risk ratio per group with `groupby` |
| [3.6 Feature importance: Mutual information](https://www.youtube.com/watch?v=_u2YaGT6RN0&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR) | 💻 Write code | Rank columns with `mutual_info_score` |
| [3.7 Feature importance: Correlation](https://www.youtube.com/watch?v=mz1707QVxiY&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR) | 💻 Write code | `corrwith` for numeric columns |
| [3.8 One-hot encoding](https://www.youtube.com/watch?v=L-mjQFN5aR0&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR) | 💻 Write code | `DictVectorizer(sparse=False)` |
| [3.9 Logistic regression](https://www.youtube.com/watch?v=7KFE2ltnBAg&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR) | 💻 Write code | Write `sigmoid` by hand and plot it |
| [3.10 Training logistic regression with Scikit-Learn](https://www.youtube.com/watch?v=hae_jXe2fN0&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR) | 💻 Write code | Train `LogisticRegression`, accuracy |
| [3.11 Model interpretation](https://www.youtube.com/watch?v=OUrlxnUAAEA&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR) | 💻 Write code | Print coefficients with column names via `zip` (compare with logit and odds ratios) |
| [3.12 Using the model](https://www.youtube.com/watch?v=Y-NGmnFpNuM&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR) | 💻 Write code | Compute churn probability for one customer |
| [3.13 Summary](https://www.youtube.com/watch?v=Zz6oRGsJkW4&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR) | 👀 + 📤 Homework | 1) Questions: [homework.md](https://github.com/DataTalksClub/machine-learning-zoomcamp/blob/main/cohorts/2026/homework/03-classification/homework.md) 2) Solve in `03-classification/homework.ipynb` 3) `./save.ps1 "hw03"` 4) Submit the GitHub link in the [hw03 form](https://courses.datatalks.club/ml-zoomcamp-2026/homework/hw03) (section 4) |

---

### Module 4: Evaluation metrics

| Lesson | What to do | Task |
|---|---|---|
| [4.1 Evaluation metrics: session overview](https://www.youtube.com/watch?v=gmg5jw1bM8A&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR) | 👀 Watch only | Understand why accuracy is not enough |
| [4.2 Accuracy and dummy model](https://www.youtube.com/watch?v=FW_l7lB0HUI&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR) | 💻 Write code | Loop over thresholds 0–1, plot accuracy |
| [4.3 Confusion table](https://www.youtube.com/watch?v=Jt2dDLSlBng&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR) | 💻 Write code | Compute TP, TN, FP, FN by hand |
| [4.4 Precision and Recall](https://www.youtube.com/watch?v=gRLP_mlglMM&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR) | 💻 Write code | Compute precision and recall |
| [4.5 ROC Curves](https://www.youtube.com/watch?v=dnBZLk53sQI&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR) | 💻 Write code | Compute TPR and FPR by hand, plot the ROC curve |
| [4.6 ROC AUC](https://www.youtube.com/watch?v=hvIQPAwkVZo&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR) | 💻 Write code | `roc_auc_score` |
| [4.7 Cross-Validation](https://www.youtube.com/watch?v=BIIZaVtUbf4&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR) | 💻 Write code | Pick the C parameter with `KFold` |
| [4.8 Summary](https://www.youtube.com/watch?v=-v8XEQ2AHvQ&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR) | 👀 + 📤 Homework | 1) Questions: [homework.md](https://github.com/DataTalksClub/machine-learning-zoomcamp/blob/main/cohorts/2026/homework/04-evaluation/homework.md) 2) Solve in `04-evaluation/homework.ipynb` 3) `./save.ps1 "hw04"` 4) Submit the GitHub link in the [hw04 form](https://courses.datatalks.club/ml-zoomcamp-2026/homework/hw04) (section 4) |

---

### Module 5: Deployment

In this module code lives in `.py` files: `05-deployment/train.py`, `predict.py`, `Dockerfile`.

| Lesson | What to do | Task |
|---|---|---|
| [5.1 Intro / Session overview](https://www.youtube.com/watch?v=agIFak9A3m8&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR) | 👀 Watch only | Understand how a model reaches the user |
| [5.2 Saving and loading the model](https://www.youtube.com/watch?v=EJpqZ7OlwFU&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR) | 💻 Write code | Move the notebook model into `train.py`, save to `model.bin` |
| [5.3 Web services: introduction to Flask](https://www.youtube.com/watch?v=W7ubna1Rfv8&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR) | 💻 Write code | Simple service with a `/ping` endpoint |
| [5.4 Serving the churn model with Flask](https://www.youtube.com/watch?v=Q7ZWPgPnRz8&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR) | 💻 Write code | `predict.py` service, test it with `requests` |
| [5.5 Python virtual environment: Pipenv](https://www.youtube.com/watch?v=BMXh8JGROHM&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR) | 👀 Watch only | The course uses Pipenv, you use uv. `uv add` = `pipenv install` |
| [5.6 Environment management: Docker](https://www.youtube.com/watch?v=wAtyYZ6zvAs&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR) | 💻 Write code | Write a `Dockerfile`, `docker build` and `docker run` |
| [5.7 Deployment to the cloud: AWS Elastic Beanstalk (optional)](https://www.youtube.com/watch?v=HGPJ4ekhcLg&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR) | ⏭ Skip | Optional. If you want, deploy to your DigitalOcean VPS instead of AWS |
| [5.8 Summary](https://www.youtube.com/watch?v=sSAqYSk7Br4&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR) | 👀 + 📤 Homework | 1) Questions: [homework.md](https://github.com/DataTalksClub/machine-learning-zoomcamp/blob/main/cohorts/2026/homework/05-deployment/homework.md) 2) Solve in `05-deployment/homework.ipynb` 3) `./save.ps1 "hw05"` 4) Submit the GitHub link in the [hw05 form](https://courses.datatalks.club/ml-zoomcamp-2026/homework/hw05) (section 4) |

---

### Module 6: Decision trees and XGBoost (credit scoring)

| Lesson | What to do | Task |
|---|---|---|
| [6.1 Credit risk scoring project](https://www.youtube.com/watch?v=GJGmlfZoCoU&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR) | 👀 Watch only | Understand how a credit scoring model makes decisions |
| [6.2 Data cleaning and preparation](https://www.youtube.com/watch?v=tfuQdI3YO2c&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR) | 💻 Write code | Turn coded values into text with `map` |
| [6.3 Decision trees](https://www.youtube.com/watch?v=YGiQvFbSIg8&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR) | 💻 Write code | `DecisionTreeClassifier`, read the rules with `export_text` |
| [6.4 Decision tree learning algorithm](https://www.youtube.com/watch?v=XODz6LwKY7g&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR) | 💻 Write code | Find the best split by hand on a 10-row table |
| [6.5 Decision trees parameter tuning](https://www.youtube.com/watch?v=XJaxwH50Qok&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR) | 💻 Write code | AUC heatmap over `max_depth` and `min_samples_leaf` |
| [6.6 Ensemble learning and random forest](https://www.youtube.com/watch?v=FZhcmOfNNZE&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR) | 💻 Write code | `n_estimators` from 10 to 200, AUC plot |
| [6.7 Gradient boosting and XGBoost](https://www.youtube.com/watch?v=xFarGClszEM&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR) | 💻 Write code | Train with `xgb.DMatrix` and a `watchlist` |
| [6.8 XGBoost parameter tuning](https://www.youtube.com/watch?v=VX6ftRzYROM&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR) | 💻 Write code | Tune `eta`, `max_depth`, `min_child_weight` one at a time |
| [6.9 Selecting the best model](https://www.youtube.com/watch?v=lqdnyIVQq-M&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR) | 💻 Write code | Compare the 3 models on test, make a table |
| [6.10 Summary](https://www.youtube.com/watch?v=JZ6sRZ_5j_c&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR) | 👀 + 📤 Homework | 1) Questions: [homework.md](https://github.com/DataTalksClub/machine-learning-zoomcamp/blob/main/cohorts/2026/homework/06-trees/homework.md) 2) Solve in `06-trees/homework.ipynb` 3) `./save.ps1 "hw06"` 4) Submit the GitHub link in the [hw06 form](https://courses.datatalks.club/ml-zoomcamp-2026/homework/hw06) (section 4) |

---

### Module 8: Deep learning (clothing images)

Note: TensorFlow may need a separate environment. Ask Claude Code before starting.

| Lesson | What to do | Task |
|---|---|---|
| [8.1 Fashion classification](https://www.youtube.com/watch?v=it1Lu7NmMpw&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR) | 👀 Watch only | Understand where image classification is useful |
| [8.2 TensorFlow and Keras](https://www.youtube.com/watch?v=R6o_CUmoN9Q&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR) | 💻 Write code | Load one image and turn it into a numpy array |
| [8.3 Pre-trained convolutional neural networks](https://www.youtube.com/watch?v=qGDXEz-cr6M&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR) | 💻 Write code | Classify your own image with Xception |
| [8.4 Convolutional neural networks](https://www.youtube.com/watch?v=BN-fnYzbdc8&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR) | 👀 Watch only | Understand convolution and pooling |
| [8.5 Transfer learning](https://www.youtube.com/watch?v=WKHylqfNmq4&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR) | 💻 Write code | Add your own layers on top of a pre-trained model |
| [8.6 Adjusting the learning rate](https://www.youtube.com/watch?v=2gPmRRGz0Hc&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR) | 💻 Write code | 3 learning rates, results table |
| [8.7 Checkpointing](https://www.youtube.com/watch?v=NRpGUx0o3Ps&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR) | 💻 Write code | Save the best model automatically |
| [8.8 Adding more layers](https://www.youtube.com/watch?v=bSRRrorvAZs&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR) | 💻 Write code | Add an inner Dense layer, compare results |
| [8.9 Regularization and dropout](https://www.youtube.com/watch?v=74YmhVM6FTM&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR) | 💻 Write code | Compare dropout 0.2 / 0.5 / 0.8 |
| [8.10 Data augmentation](https://www.youtube.com/watch?v=aoPfVsS3BDE&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR) | 💻 Write code | Add rotation and zoom |
| [8.11 Training a larger model](https://www.youtube.com/watch?v=_QpDGJwFjYA&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR) | 💻 Write code | Retrain with a larger image size |
| [8.12 Using the model](https://www.youtube.com/watch?v=cM1WHKae1wo&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR) | 💻 Write code | Predict a photo from your phone |
| [8.13 Summary](https://www.youtube.com/watch?v=mn0BcXJlRFM&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR) | 👀 + 📤 Homework | 1) Questions: [homework.md](https://github.com/DataTalksClub/machine-learning-zoomcamp/blob/main/cohorts/2026/homework/08-deep-learning/homework.md) 2) Solve in `08-deep-learning/homework.ipynb` 3) `./save.ps1 "hw08"` 4) Submit the GitHub link in the [hw08 form](https://courses.datatalks.club/ml-zoomcamp-2026/homework/hw08) (section 4) |

---

### Module 9: Serverless

| Lesson | What to do | Task |
|---|---|---|
| [9.1 Introduction to Serverless](https://www.youtube.com/watch?v=JLIVwIsU6RA&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR) | 👀 Watch only | Understand serverless vs VPS |
| [9.2 AWS Lambda](https://www.youtube.com/watch?v=_UX8-2WhHZo&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR) | 💻 Write code | "Hello" Lambda function (AWS free tier) |
| [9.3 TensorFlow Lite](https://www.youtube.com/watch?v=OzZA4mSBE0Q&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR) | 💻 Write code | Convert the module 8 model to `.tflite` |
| [9.4 Preparing the code for Lambda](https://www.youtube.com/watch?v=XXBUivsHhec&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR) | 💻 Write code | `lambda_function.py` |
| [9.5 Preparing a Docker image](https://www.youtube.com/watch?v=y4_YQjfOsDo&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR) | 💻 Write code | Dockerfile for Lambda |
| [9.6 Creating the lambda function](https://www.youtube.com/watch?v=kBch5oD5BkY&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR) | 💻 Write code | Create the function on AWS and test it |
| [9.7 API Gateway: exposing the lambda function](https://www.youtube.com/watch?v=wyZ9aqQOXvs&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR) | 💻 Write code | Expose the function via a URL |
| [9.8 Summary](https://www.youtube.com/watch?v=bu3nPiHCNLU&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR) | 👀 + 📤 Homework | 1) Questions: [homework.md](https://github.com/DataTalksClub/machine-learning-zoomcamp/blob/main/cohorts/2026/homework/09-serverless/homework.md) 2) Solve in `09-serverless/homework.ipynb` 3) `./save.ps1 "hw09"` 4) Submit the GitHub link in the [hw09 form](https://courses.datatalks.club/ml-zoomcamp-2026/homework/hw09) (section 4) |

---

### Module 10: Kubernetes

| Lesson | What to do | Task |
|---|---|---|
| [10.1 Overview](https://www.youtube.com/watch?v=mvPER7YfTkw&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR) | 👀 Watch only | Understand the architecture: gateway and model service |
| [10.2 TensorFlow Serving](https://www.youtube.com/watch?v=deXR2fThYDw&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR) | 💻 Write code | Run the model in TF Serving Docker |
| [10.3 Creating a pre-processing service](https://www.youtube.com/watch?v=OIlrS14Zi0o&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR) | 💻 Write code | `gateway.py` service |
| [10.4 Running everything locally with Docker-compose](https://www.youtube.com/watch?v=ZhQQfpWfkKY&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR) | 💻 Write code | Run both together with `docker-compose.yaml` |
| [10.5 Introduction to Kubernetes](https://www.youtube.com/watch?v=UjVkpszDzgk&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR) | 👀 Watch only | Understand Pod, Deployment, Service |
| [10.6 Deploying a simple service to Kubernetes](https://www.youtube.com/watch?v=PPUCVRIV9t8&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR) | 💻 Write code | Local cluster with `kind`, simple service |
| [10.7 Deploying TensorFlow models to Kubernetes](https://www.youtube.com/watch?v=6vHLMdnjO2w&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR) | 💻 Write code | Deploy the model to the cluster |
| [10.8 Deploying to EKS](https://www.youtube.com/watch?v=89jxeddZtC0&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR) | ⏭ Skip | Optional. Watch only if you want |
| [10.9 Summary](https://www.youtube.com/watch?v=J5LMRTIu4jY&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR) | 👀 + 📤 Homework | 1) Questions: [homework.md](https://github.com/DataTalksClub/machine-learning-zoomcamp/blob/main/cohorts/2026/homework/10-kubernetes/homework.md) 2) Solve in `10-kubernetes/homework.ipynb` 3) `./save.ps1 "hw10"` 4) Submit the GitHub link in the [hw10 form](https://courses.datatalks.club/ml-zoomcamp-2026/homework/hw10) (section 4) |

---

## 3. End of module: transfer exercise

When a module is done, set aside 1–2 hours:

1. Open a new notebook in `transfer/`: `transfer/03-bank-churn.ipynb`
2. Apply the module's method to new data (Kaggle, data.egov.uz or a HEAD client).
3. End the notebook with a 3-line conclusion: result, problem, what it means for the business.
4. Write its name in the "Transfer project" column of README.md.

---

## 4. Doing and submitting the homework

### Doing it

1. Open the questions: `course/cohorts/2026/homework/XX-module/homework.md`
2. Work in `XX-module/homework.ipynb`. One Markdown heading per question: `## Q1`, `## Q2`...
3. Under each question write your answer in Markdown: `Answer: 9000`
4. At the end: Kernel → "Restart Kernel and Run All Cells". It must run without errors.

### Saving and getting the link

1. In PowerShell: `./save.ps1 "hw2 done"`
2. On GitHub open your repo → `02-regression` → `homework.ipynb`
3. Copy the link from the browser address bar.

### Submitting

1. https://courses.datatalks.club/ml-zoomcamp-2026/ → the right Homework
2. Fill in the form:

| Field | What to enter |
|---|---|
| Questions | The option closest to your result |
| Reflection | One practical idea from the module |
| Homework URL | GitHub link to homework.ipynb |
| Learning in public | LinkedIn post links (up to 7, each gives points) |
| Time spent | Hours spent on videos and homework |

3. Click "Submit". You can change answers until the deadline.
4. Mark the module ✅ in README.md and run `./save.ps1` again.

### Deadline

Deadline: Tuesday 04:00 Tashkent time. In practice, submit by Monday 23:00.

---

## 5. Weekly rhythm

| Day | What |
|---|---|
| Tuesday | New module: first half of the videos and tasks |
| Thursday | Second half and notes.md |
| Saturday | Homework |
| Sunday | Transfer exercise and LinkedIn post |
| Monday night | Submit |

---

## 6. Common problems

| Problem | Fix |
|---|---|
| Jupyter "Server Connection Error" | The black window was closed. Reopen "ML Zoomcamp" on the Desktop |
| "Action disabled" in an HTML file | Click "Trust HTML" in Jupyter or open the file in Chrome |
| `ModuleNotFoundError` | In PowerShell: `uv add <library>` |
| Code from the video gives a different result | Check the pandas 3 difference (rule in section 1) |
| No "Ask" button, or `UsageError: Line magic function %ask not found` | Jupyter was not started from `start.bat`. Close it and reopen "ML Zoomcamp" on the Desktop |
| `save.ps1` doesn't push | Do the GitHub setup in section 0 |
