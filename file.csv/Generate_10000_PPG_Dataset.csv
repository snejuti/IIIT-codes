
import os
import numpy as np
import pandas as pd

NUM_SUBJECTS = 10000
FS = 125
DURATION_SEC = 60
N = FS * DURATION_SEC

output_dir = "PPG_10000_Subjects"
os.makedirs(output_dir, exist_ok=True)

master_rows = []

for sid in range(1, NUM_SUBJECTS + 1):

    age = np.random.randint(18, 80)
    height = np.random.randint(150, 191)
    weight = np.random.randint(45, 121)

    bmi = round(weight / ((height/100)**2), 2)

    sbp = np.random.randint(90, 181)
    dbp = np.random.randint(55, 111)

    if sbp < 90 or dbp < 60:
        bp_status = "Low BP"
    elif sbp <= 120 and dbp <= 80:
        bp_status = "Normal"
    else:
        bp_status = "High BP"

    t = np.arange(N) / FS

    hr = np.random.uniform(55, 100)
    f = hr / 60

    ppg = (
        1.0*np.sin(2*np.pi*f*t) +
        0.4*np.sin(4*np.pi*f*t) +
        0.2*np.sin(6*np.pi*f*t)
    )

    baseline = 0.4*np.sin(2*np.pi*0.05*t)
    noise = np.random.normal(0, 0.08, N)

    raw_ppg = ppg + baseline + noise

    subject_id = f"SUB_{sid:05d}"

    pd.DataFrame({
        "Time_s": t,
        "Raw_PPG": raw_ppg
    }).to_csv(
        os.path.join(output_dir, f"{subject_id}.csv"),
        index=False
    )

    master_rows.append([
        subject_id,
        age,
        height,
        weight,
        bmi,
        sbp,
        dbp,
        bp_status
    ])

master = pd.DataFrame(
    master_rows,
    columns=[
        "Subject_ID",
        "Age",
        "Height",
        "Weight",
        "BMI",
        "SBP",
        "DBP",
        "BP_Status"
    ]
)

master.to_csv(
    os.path.join(output_dir, "Master.csv"),
    index=False
)

print("Dataset generation complete.")
