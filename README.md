# LLM Parametre Testi — M2 MacBook Air (16 GB) Üzerinde MPS (float16)

**Test Sahibi:** [@cengizali07](https://github.com/cengizali07)  
**Cihaz:** Apple M2 MacBook Air  
**RAM:** 16 GB  
**GPU Backend:** Metal Performance Shaders (MPS)  
**Model Formatı:** `float16` (half precision)  
**Amaç:** 1B ila 20B arası modellerin yüklenme süresi ve başarım limitlerini test etmek.

---

 Test Sonuçları

| Model Parametresi | Süre (s) | Durum   |
|--------------------|---------|---------|
| 1000M              | 1.07    | ✅ Başarılı |
| 2000M              | 2.04    | ✅ Başarılı |
| 3000M              | 3.14    | ✅ Başarılı |
| 4000M              | 4.18    | ✅ Başarılı |
| 5000M              | 5.21    | ✅ Başarılı |
| 6000M              | 6.28    | ✅ Başarılı |
| 7000M              | 7.40    | ✅ Başarılı |
| 8000M              | 8.54    | ✅ Başarılı |
| 9000M              | 10.22   | ✅ Başarılı |
| 10000M             | 11.28   | ✅ Başarılı |
| 11000M             | 15.88   | ✅ Başarılı |
| 12000M             | 37.63   | ✅ Başarılı |
| 13000M             | 277.64  | ✅ Başarılı |
| 14000M             | 394.90  | ✅ Başarılı |
| 15000M             | 441.55  | ✅ Başarılı |
| 16000M             | 532.00  | ✅ Başarılı |
| 17000M             | 631.71  | ✅ Başarılı |
| 18000M             | 670.17  | ✅ Başarılı |
| 19000M             | 743.34  | ✅ Başarılı |
| 20000M             | —       | ❌ Başarısız (MPS Out of Memory) |

---

## Bellek Hatası Detayı

MPS backend out of memory (MPS allocated: 18.13 GB, max allowed: 18.13 GB).
Tried to allocate 512.00 KB on private pool.


MPS, GPU belleğini tam kapasite kullanmaz. Bu sınırı kaldırmak için:

bash
export PYTORCH_MPS_HIGH_WATERMARK_RATIO=0.0

Uyarı: Bu ayar sistem dengesini bozabilir. Dikkatli kullanılmalıdır.

Kullanılan Araçlar

 Python 3.13.5
 PyTorch (MPS backend aktif)
 Sistem: macOS-14.3.1-arm64-arm-64bit-Mach-O
 PyTorch Sürüm: 2.7.1
 MPS Kullanılabilir: True


Bu testte gerçek bir dil modeli (LLM) yerine, torch.nn.Linear katmanlarından oluşan sentetik (dummy) bir model kullanılmıştır.
Bu testte, farklı boyutlarda yapay (sentetik) modeller kullanılarak Apple M2 MacBook Air (16 GB) cihazında 
MPS (Metal Performance Shaders) backend ile bellek limiti ve hesaplama süresi ölçülmüştür.


Amaç:
Gerçek modellerin (örneğin LLaMA, GPT, BLOOM) GPU'da nasıl davrandığını test etmek yerine:

M2 MacBook Air gibi sınırlı GPU belleğine sahip cihazlarda
Farklı büyüklükteki (parametre sayısına göre) yapay modellerin
Bellek kullanımı ve işleme süresini
MPS (Metal Performance Shaders) backend ile ölçmeyi amaçlar.


Kullanılan Araçlar

 Python 3.13.5
 PyTorch (MPS backend aktif)
 Sistem: macOS-14.3.1-arm64-arm-64bit-Mach-O
 PyTorch Sürüm: 2.7.1
 MPS Kullanılabilir: True
 
✅ 1000M parametre (float32) için test başarılı. Süre: 2.07s, Katman: 3807
✅ 2000M parametre (float32) için test başarılı. Süre: 4.17s, Katman: 7614
✅ 3000M parametre (float32) için test başarılı. Süre: 219.23s, Katman: 11421
✅ 4000M parametre (float32) için test başarılı. Süre: 552.06s, Katman: 15229
❌ 5000M parametre (float32) için test başarısız: MPS backend out of memory (MPS allocated: 18.13 GB, other allocations: 384.00 KB, max allowed: 18.13 GB). Tried to allocate 1024.00 KB on private pool. Use PYTORCH_MPS_HIGH_WATERMARK_RATIO=0.0 to disable upper limit for memory allocations (may cause system failure).
❌ 6000M parametre (float32) için test başarısız: MPS backend out of memory (MPS allocated: 18.13 GB, other allocations: 384.00 KB, max allowed: 18.13 GB). Tried to allocate 1024.00 KB on private pool. Use PYTORCH_MPS_HIGH_WATERMARK_RATIO=0.0 to disable upper limit for memory allocations (may cause system failure).
❌ 7000M parametre (float32) için test başarısız: MPS backend out of memory (MPS allocated: 18.13 GB, other allocations: 384.00 KB, max allowed: 18.13 GB). Tried to allocate 1024.00 KB on private pool. Use PYTORCH_MPS_HIGH_WATERMARK_RATIO=0.0 to disable upper limit for memory allocations (may cause system failure).
❌ 8000M parametre (float32) için test başarısız: MPS backend out of memory (MPS allocated: 18.13 GB, other allocations: 384.00 KB, max allowed: 18.13 GB). Tried to allocate 1024.00 KB on private pool. Use PYTORCH_MPS_HIGH_WATERMARK_RATIO=0.0 to disable upper limit for memory allocations (may cause system failure).
zsh: killed     python 32bitstress.py

