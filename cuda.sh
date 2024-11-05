pip install torch --index-url https://download.pytorch.org/whl/cu118
2.0.1+cu118
_CudaDeviceProperties(name='NVIDIA H100 80GB HBM3', major=9, minor=0, total_memory=81082MB, multi_processor_count=132)
tensor([-0.9087], device='cuda:0')

pip install --pre torch --index-url https://download.pytorch.org/whl/nightly/cu118
2.1.0.dev20230810+cu118
_CudaDeviceProperties(name='NVIDIA H100 80GB HBM3', major=9, minor=0, total_memory=81082MB, multi_processor_count=132)
tensor([-0.6681], device='cuda:0')

pip install --pre torch --index-url https://download.pytorch.org/whl/nightly/cu121
2.1.0.dev20230810+cu121
_CudaDeviceProperties(name='NVIDIA H100 80GB HBM3', major=9, minor=0, total_memory=81082MB, multi_processor_count=132)
tensor([0.1740], device='cuda:0')