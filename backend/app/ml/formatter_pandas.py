import pandas as pd
from typing import Any


def report_for_seasons(data: Any):
    df = pd.DataFrame(data)
    df.columns = pd.Series(["DAT_S", "PASS_BK"])
    return df


def report_for_dynamic(data: Any):
    df = pd.DataFrame(data)
    df.columns = pd.Series(["DAT_S", "PASS_BK", "DTD"])
    return df
