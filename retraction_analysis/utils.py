from pathlib import Path

import pandas as pd


def get_retractions() -> pd.DataFrame:
    retractions_file = Path(__file__).parents[1] / "data" / "retractions.csv"
    breakpoint()
    return pd.read_csv(retractions_file)
