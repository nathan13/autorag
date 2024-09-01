import torch

if torch.cuda.is_available():
    print("CUDA está disponível.")
    print(f"Usando GPU: {torch.cuda.get_device_name(0)}")
else:
    print("CUDA não está disponível. Usando CPU.")

