import pandas as pd
import numpy as np

df = pd.DataFrame({'name': ['Paul','Lozik','Neon','Sano'],'age': ['41','32','34','31']})
expected_name = df.name[0]
print(expected_name)