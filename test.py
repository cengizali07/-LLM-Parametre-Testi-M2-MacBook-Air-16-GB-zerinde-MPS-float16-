import torch
import time

# test edilen cihaz (MPS)
device = "mps"

def test_model_size(num_params_million):
    hidden_size = 512
    layers = max(1, int((num_params_million * 1_000_000) // (hidden_size * hidden_size * 2)))
    
    try:
        # model'i float16 ile oluştur
        model = torch.nn.Sequential(*[
            torch.nn.Linear(hidden_size, hidden_size).to(torch.float16) for _ in range(layers)
        ]).to(device)

        x = torch.randn(1, hidden_size, dtype=torch.float16).to(device)

        start = time.time()
        for _ in range(10):
            _ = model(x)
        print(f" {num_params_million}M parametre (float16) için test başarılı. Süre: {time.time() - start:.2f}s")
    except Exception as e:
        print(f" {num_params_million}M parametre (float16) için test başarısız: {e}")

# Benchmark için test aralığı
for params in [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000,
               10000,11000, 12000,13000,14000,15000, 16000, 17000, 18000, 19000, 20000]:
    test_model_size(params)
