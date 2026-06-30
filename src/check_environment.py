import sys
import torch
import pathlib
print("Python executable:", sys.executable)
print("Pytorch version:", torch.__version__)
print("Data directory exists:", pathlib.Path("MedMNIST_Blood_Path_Organ_128").exists())