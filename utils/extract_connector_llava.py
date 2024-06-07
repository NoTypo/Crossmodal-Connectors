import glob
import os
import torch
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-m", "--model", help="Path to llava checkpoint")
args = ap.parse_args()

checkpoint = torch.load(args.model)

mm_tensors = [k for k, v in checkpoint.items() if k.startswith("model.mm_projector")]

projector = {name: checkpoint[name] for name in mm_tensors}
torch.save(projector, f"{args.model}/llava.projector")
