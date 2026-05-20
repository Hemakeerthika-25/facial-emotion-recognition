import pandas as pd
from sklearn.model_selection import train_test_split

def create_splits(final_df, save_path="data"):
    train_df, temp_df = train_test_split(
        final_df,
        test_size=0.3,
        random_state=42,
        stratify=final_df["label"]
    )
    
    val_df, test_df = train_test_split(
        temp_df,
        test_size=0.5,
        random_state=42,
        stratify=temp_df["label"]
    )
    
    train_df.to_csv(f"{save_path}/train.csv", index=False)
    val_df.to_csv(f"{save_path}/val.csv", index=False)
    test_df.to_csv(f"{save_path}/test.csv", index=False)