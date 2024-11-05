import torch
print(torch.cuda.get_arch_list())
print(torch.__version__)
print(torch.cuda.get_device_properties(0))

print(torch.randn(1, device="cuda"))