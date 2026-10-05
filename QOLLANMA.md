# ML Zoomcamp: har bir darsdan keyin nima qilish kerak

Bu qo'llanma 3 savolga javob beradi:

1. Videodan keyin qanday vazifa bajaraman?
2. Natijani qayerga joylayman?
3. Uy vazifasini qanday topshiraman?

Video havolalari: `videos.html` (Desktop'dagi "ML Zoomcamp videolar" belgisi).

---

## 0. Bir martalik sozlash: GitHub'ga ulash

Repo hali GitHub'ga ulanmagan. PowerShell'da bir marta bajaring:

```
cd C:\Users\User\ml-zoomcamp\ml-zoomcamp-2026
gh config set git_protocol https
gh auth setup-git
gh repo create ml-zoomcamp-2026 --public --source=. --push
```

Shundan keyin `./save.ps1` ishlarni GitHub'ga yuboradi.

---

## 1. Har bir dars uchun 4 qadamli sikl

| Qadam | Nima qilasiz | Qayerga yozasiz | Vaqt |
|---|---|---|---|
| 1. Ko'rish | Videoni ko'ring. Kod bo'lsa, to'xtatib o'zingiz yozing | `XX-modul/lesson.ipynb` | video davomida |
| 2. Vazifa | Quyidagi jadvaldagi "Dars vazifasi"ni bajaring | `XX-modul/lesson.ipynb` | 5–15 daqiqa |
| 3. Konspekt | 2–3 qator: bu nima, nega kerak | `XX-modul/notes.md` | 3 daqiqa |
| 4. Saqlash | Kunning oxirida bir marta | PowerShell: `./save.ps1 "2.4 validation"` | 1 daqiqa |

### lesson.ipynb ni qanday tartiblash

Har bir dars uchun Markdown katak bilan sarlavha qo'ying, keyin kod kataklari:

```
## 2.4 Setting up the validation framework      ← Markdown katak (M tugmasi)
[kod]                                           ← darsdagi kod
### Vazifa                                      ← Markdown katak
[kod]                                           ← o'zingiz bajargan vazifa
```

Shunda bir oydan keyin ham kerakli darsni tez topasiz.

### Qoidalar

- Alexey'ning notebook'idan nusxa ko'chirmang. Kodni o'zingiz yozing.
- Tiqilib qolsangiz: 20 daqiqa o'zingiz urining, keyin Claude Code'dan maslahat so'rang.
- Pandas 3: `df['col'].fillna(x, inplace=True)` ishlamaydi. `df['col'] = df['col'].fillna(x)` deb yozing.
- Kurs materiallari: `C:\Users\User\ml-zoomcamp\course\XX-modul\` (har bir darsning konspekti .md faylda).

---

## 2. Modullar bo'yicha dars vazifalari

Belgilar: 📝 = notes.md ga yozing, 💻 = lesson.ipynb da kod yozing.

### 1-modul: Introduction to ML

| Dars | Dars vazifasi |
|---|---|
| 1.1 What is ML | 📝 HEAD mijozidan bitta misol yozing: features (X) nima, target (y) nima |
| 1.2 ML vs Rules | 📝 Bitta biznes muammosini qoidalar bilan, bittasini ML bilan yechish kerakligini asoslang |
| 1.3 Supervised ML | 📝 g(X) ≈ y. Regressiya, klassifikatsiya, ranking uchun bittadan misol |
| 1.4 CRISP-DM | 📝 6 bosqichni HEAD loyihasiga moslang: har bosqichda mijozdan nima so'raysiz? |
| 1.5 Model selection | 💻 20 ta sonli massivni `np.random.permutation` bilan 60/20/20 ga bo'ling |
| 1.6 Environment | O'tkazib yuboring |
| 1.7 NumPy | 💻 Darsdagi kodni yozing. Qo'shimcha: 3×3 tasodifiy matritsa, ustunlar o'rtachasi |
| 1.8 Linear algebra | 💻 `X.T @ X`, `np.linalg.inv`. 📝 Bu OLS'dagi (XᵀX)⁻¹Xᵀy bilan qanday bog'liq? |
| 1.9 Pandas | 💻 Darsdagi amallarni `data/car_fuel_efficiency_2026.csv` ga qo'llang |
| 1.10 Summary | Uy vazifasi 1 ga o'ting |

### 2-modul: Regression (avtomobil narxi)

| Dars | Dars vazifasi |
|---|---|
| 2.1 Project intro | 📝 Target nima? Xatoni qanday o'lchaymiz? |
| 2.2 Data preparation | 💻 Ustun nomlarini `str.lower().str.replace(' ', '_')` bilan tozalang |
| 2.3 EDA | 💻 Narx gistogrammasi, keyin `np.log1p` dan keyingi gistogramma. 📝 Nega log? |
| 2.4 Validation | 💻 60/20/20 bo'linma, `seed=42`. Uchala qism hajmini tekshiring |
| 2.5 Linear regression | 💻 Bitta avtomobil uchun w0 + Σwᵢxᵢ ni sikl bilan hisoblang |
| 2.6 Vector form | 💻 Shu hisobni `X.dot(w)` bilan qayta yozing |
| 2.7 Normal equation | 💻 `train_linear_regression(X, y)` funksiyasini o'zingiz yozing |
| 2.8 Baseline | 💻 5 ta sonli ustun, `fillna(0)`, birinchi model |
| 2.9 RMSE | 💻 `rmse(y, y_pred)` funksiyasi. 📝 RMSE va R² farqi |
| 2.10 Validation RMSE | 💻 `prepare_X(df)` funksiyasi, validatsiyada RMSE |
| 2.11 Feature engineering | 💻 `age` ustunini qo'shing. RMSE qancha o'zgardi? |
| 2.12 Categorical | 💻 Eng ko'p uchraydigan 5 ta qiymat uchun qo'lda one-hot |
| 2.13 Regularization | 💻 XᵀX + r·I. 📝 Bu Ridge regressiya. Multikollinearlik bilan bog'lang |
| 2.14 Tuning | 💻 r = [0, 0.001, 0.01, 0.1, 1, 10] sikli, eng yaxshi r |
| 2.15 Using the model | 💻 Train+val'da o'rgating, bitta avtomobil narxini bashorat qiling, `np.expm1` |
| 2.16 Summary | Uy vazifasi 2 ga o'ting |

Ko'chirish mashqi (`transfer/02-regression.ipynb`): xuddi shu usulni boshqa ma'lumotga qo'llang, masalan kvartira narxlari.

### 3-modul: Classification (mijoz ketishi, churn)

| Dars | Dars vazifasi |
|---|---|
| 3.1 Churn project | 📝 Bank yoki telekom uchun churn modeli qanday pul tejaydi? |
| 3.2 Data preparation | 💻 `pd.to_numeric(..., errors='coerce')`, bo'sh qiymatlar |
| 3.3 Validation | 💻 `train_test_split` bilan 60/20/20 |
| 3.4 EDA | 💻 Umumiy churn darajasi, kategorik ustunlar ro'yxati |
| 3.5 Churn rate va risk ratio | 💻 `groupby` bilan har guruh uchun risk ratio |
| 3.6 Mutual information | 💻 `mutual_info_score` bilan ustunlarni tartiblang |
| 3.7 Correlation | 💻 Sonli ustunlar uchun `corrwith` |
| 3.8 One-hot encoding | 💻 `DictVectorizer(sparse=False)` |
| 3.9 Logistic regression | 💻 `sigmoid` funksiyasini qo'lda yozing va grafigini chizing |
| 3.10 Training | 💻 `LogisticRegression` bilan o'rgating, accuracy |
| 3.11 Interpretation | 📝 Koeffitsientlarni o'qing. Ekonometrikadagi logit va odds ratio bilan solishtiring |
| 3.12 Using the model | 💻 Bitta mijoz uchun ketish ehtimolini hisoblang |
| 3.13 Summary | Uy vazifasi 3 ga o'ting |

### 4-modul: Evaluation metrics

| Dars | Dars vazifasi |
|---|---|
| 4.1 Overview | 📝 Accuracy nega yetarli emas? |
| 4.2 Accuracy va dummy model | 💻 Threshold 0–1 oralig'ida sikl, accuracy grafigi |
| 4.3 Confusion table | 💻 TP, TN, FP, FN ni qo'lda hisoblang |
| 4.4 Precision va Recall | 💻 Ikkalasini hisoblang. 📝 Bankda FP va FN qancha turadi? |
| 4.5 ROC curves | 💻 TPR va FPR ni qo'lda hisoblab, egri chiziq chizing |
| 4.6 ROC AUC | 💻 `roc_auc_score`. 📝 AUC ni mijozga bitta jumlada tushuntiring |
| 4.7 Cross-validation | 💻 `KFold` bilan C parametrini tanlang |
| 4.8 Summary | Uy vazifasi 4 ga o'ting |

### 5-modul: Deployment

Bu modulda kod `.py` fayllarda bo'ladi: `05-deployment/train.py`, `05-deployment/predict.py`, `05-deployment/Dockerfile`.

| Dars | Dars vazifasi |
|---|---|
| 5.1 Overview | 📝 Model mijozga qanday yetib boradi? Sxema chizing |
| 5.2 Pickle | 💻 Notebook'dagi modelni `train.py` ga ko'chiring, `model.bin` ga saqlang |
| 5.3 Web services | 💻 `/ping` endpoint'i bilan oddiy servis |
| 5.4 Serving the model | 💻 `predict.py` servisi va `requests` bilan sinov |
| 5.5 Virtual environment | 📝 Kurs Pipenv ishlatadi, siz uv. `uv add` = `pipenv install` |
| 5.6 Docker | 💻 `Dockerfile` yozing, `docker build` va `docker run` |
| 5.7 AWS (ixtiyoriy) | 💻 AWS o'rniga DigitalOcean VPS'ingizga joylang |
| 5.8 Summary | Uy vazifasi 5 ga o'ting |

### 6-modul: Decision trees va XGBoost (kredit skoringi)

| Dars | Dars vazifasi |
|---|---|
| 6.1 Credit risk | 📝 Mikromoliya tashkiloti uchun bu model qanday qaror qabul qiladi? |
| 6.2 Data cleaning | 💻 Kodlangan qiymatlarni `map` bilan matnga aylantiring |
| 6.3 Decision trees | 💻 `DecisionTreeClassifier`, `export_text` bilan qoidalarni o'qing |
| 6.4 Learning algorithm | 💻 10 qatorli kichik jadvalda eng yaxshi bo'linishni qo'lda toping |
| 6.5 Tuning | 💻 `max_depth` va `min_samples_leaf` bo'yicha AUC heatmap |
| 6.6 Random forest | 💻 `n_estimators` 10 dan 200 gacha, AUC grafigi |
| 6.7 XGBoost | 💻 `xgb.DMatrix`, `watchlist` bilan o'rgatish |
| 6.8 XGBoost tuning | 💻 `eta`, `max_depth`, `min_child_weight` ni navbat bilan sozlang |
| 6.9 Best model | 💻 3 ta modelni test'da solishtiring, jadval qiling |
| 6.10 Summary | Uy vazifasi 6 ga o'ting |

### 8-modul: Deep learning (kiyim rasmlari)

Eslatma: TensorFlow uchun alohida muhit kerak bo'lishi mumkin. Boshlashdan oldin Claude Code'dan so'rang.

| Dars | Dars vazifasi |
|---|---|
| 8.1 Fashion classification | 📝 Rasm klassifikatsiyasi HEAD mijozlariga qayerda kerak? |
| 8.2 TensorFlow va Keras | 💻 Bitta rasmni yuklab, numpy massivga aylantiring |
| 8.3 Pre-trained models | 💻 Xception bilan o'z rasmingizni tasniflang |
| 8.4 CNN | 📝 Convolution va pooling nima, 3 qatorda |
| 8.5 Transfer learning | 💻 Tayyor model ustiga o'z qatlamingizni qo'shing |
| 8.6 Learning rate | 💻 3 ta learning rate, natijalar jadvali |
| 8.7 Checkpointing | 💻 Eng yaxshi modelni avtomatik saqlang |
| 8.8 More layers | 💻 Ichki Dense qatlam qo'shing, natijani solishtiring |
| 8.9 Dropout | 💻 Dropout 0.2 / 0.5 / 0.8 ni solishtiring |
| 8.10 Augmentation | 💻 Aylantirish va kattalashtirish qo'shing |
| 8.11 Larger model | 💻 Katta rasm o'lchami bilan qayta o'rgating |
| 8.12 Using the model | 💻 Telefoningizdagi rasmni bashorat qiling |
| 8.13 Summary | Uy vazifasi 8 ga o'ting |

### 9-modul: Serverless

| Dars | Dars vazifasi |
|---|---|
| 9.1 Intro | 📝 Serverless va VPS farqi. Qachon qaysi biri arzon? |
| 9.2 AWS Lambda | 💻 "Hello" funksiyasi (AWS free tier) |
| 9.3 TensorFlow Lite | 💻 8-modul modelini `.tflite` ga aylantiring |
| 9.4 Preparing code | 💻 `lambda_function.py` |
| 9.5 Docker image | 💻 Lambda uchun Dockerfile |
| 9.6 Creating lambda | 💻 Funksiyani AWS'da yarating va sinang |
| 9.7 API Gateway | 💻 Funksiyani URL orqali oching |
| 9.8 Summary | Uy vazifasi 9 ga o'ting |

### 10-modul: Kubernetes

| Dars | Dars vazifasi |
|---|---|
| 10.1 Overview | 📝 Arxitektura sxemasi: gateway va model servisi |
| 10.2 TF Serving | 💻 Modelni TF Serving Docker'ida ishga tushiring |
| 10.3 Pre-processing | 💻 `gateway.py` servisi |
| 10.4 Docker compose | 💻 `docker-compose.yaml` bilan ikkalasini birga ishga tushiring |
| 10.5 Kubernetes intro | 📝 Pod, Deployment, Service nima |
| 10.6 Simple service | 💻 `kind` bilan lokal klaster, oddiy servis |
| 10.7 TF models | 💻 Modelni klasterga joylang |
| 10.8 EKS (ixtiyoriy) | O'qib chiqing, majburiy emas |
| 10.9 Summary | Uy vazifasi 10 ga o'ting |

---

## 3. Modul oxirida: ko'chirish mashqi

Har bir modul tugagach, 1–2 soat ajrating:

1. `transfer/` papkasida yangi notebook oching: `transfer/03-bank-churn.ipynb`
2. Modul usulini yangi ma'lumotga qo'llang (Kaggle, data.egov.uz yoki HEAD mijozi).
3. Notebook oxirida 3 qator xulosa yozing: natija, muammo, biznes uchun ma'nosi.
4. README.md dagi "Transfer project" ustuniga nomini yozing.

---

## 4. Uy vazifasini bajarish va topshirish

### Bajarish

1. Savollarni oching: `course/cohorts/2026/homework/XX-modul/homework.md`
2. `XX-modul/homework.ipynb` da ishlang. Har bir savol uchun Markdown sarlavha: `## Q1`, `## Q2`...
3. Har bir savol ostiga javobingizni Markdown'da yozing: `Javob: 9000`
4. Oxirida: Kernel → "Restart Kernel and Run All Cells". Xatosiz ishlashi kerak.

### Saqlash va havola olish

1. PowerShell'da: `./save.ps1 "hw2 done"`
2. GitHub'da repo'ingizni oching → `02-regression` → `homework.ipynb`
3. Brauzer manzil satridagi havolani nusxalang.

### Topshirish

1. https://courses.datatalks.club/ml-zoomcamp-2026/ → kerakli Homework
2. Formani to'ldiring:

| Maydon | Nima yozasiz |
|---|---|
| Savollar | Hisobingizga eng yaqin variant |
| Reflection | Moduldan olgan bitta amaliy g'oya |
| Homework URL | GitHub'dagi homework.ipynb havolasi |
| Learning in public | LinkedIn post havolasi (7 tagacha, har biri ball beradi) |
| Time spent | Video va uy vazifasiga ketgan soatlar |

3. "Submit" ni bosing. Muddat tugaguncha javoblarni o'zgartirsa bo'ladi.
4. README.md da modul holatini ✅ qiling va yana `./save.ps1`.

### Muddat

Topshirish muddati: seshanba, Toshkent vaqti bilan 04:00. Amalda dushanba kechasi 23:00 gacha topshiring.

---

## 5. Haftalik ritm

| Kun | Nima |
|---|---|
| Seshanba | Yangi modul: birinchi yarmi videolari va dars vazifalari |
| Payshanba | Ikkinchi yarmi va notes.md |
| Shanba | Uy vazifasi |
| Yakshanba | Ko'chirish mashqi va LinkedIn post |
| Dushanba kechasi | Topshirish |

---

## 6. Tez-tez uchraydigan muammolar

| Muammo | Yechim |
|---|---|
| Jupyter "Server Connection Error" | Qora oyna yopilgan. Desktop'dagi "ML Zoomcamp" ni qayta oching |
| HTML faylda "Action disabled" | Jupyter'da "Trust HTML" ni bosing yoki faylni Chrome'da oching |
| `ModuleNotFoundError` | PowerShell'da `uv add <kutubxona>` |
| Videodagi kod sizda boshqa natija beradi | Pandas 3 farqini tekshiring (1-bo'limdagi qoida) |
| `save.ps1` push qilmaydi | 0-bo'limdagi GitHub sozlashni bajaring |
