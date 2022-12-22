import time
import numpy as np

for i, x in enumerate(np.random.rand(10)):
  print(f"{i+1}th wait, waiting for {x} seconds...")
