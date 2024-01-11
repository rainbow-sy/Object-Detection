import torch
import torch.nn as nn

a=torch.tensor(9.4)
a=torch.clamp(a,3,9)
print(a)

