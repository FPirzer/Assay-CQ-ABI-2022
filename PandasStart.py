import pandas as pd
import numpy as np

dataframe1 = pd.DataFrame(
    np.random.randn(4, 6),
    index=("Row1", "Row2", "Row3", "Row4"),
    columns=("Coloum1", "Coloum2", "Coloum3", "Coloum4", "Coloum5", "Coloum6"),
)
print(dataframe1, "\n")

print(dataframe1.sort_values("Coloum3"), "\n")
print(dataframe1.describe())
print(dataframe1.transpose().describe())
