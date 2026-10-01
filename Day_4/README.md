#  AI Fluency – Day 4

## Will It Fit, and May I Use It?

Day 4 focuses on **Open LLMs and Local Serving**.

The task explores how to estimate whether an open model will fit on a machine before downloading it, how quantization and context length affect memory usage, and how model licences affect whether a model can legally be used in a particular scenario.

---

## 🎯 Objectives

The main objectives of Day 4 are to:

* Understand model memory requirements
* Calculate model weight memory
* Estimate KV cache memory
* Understand context length
* Understand quantization
* Build a Python memory estimator
* Compare estimated memory with actual Ollama usage
* Read and compare model cards
* Understand open-weight vs open-source models
* Compare model licences
* Check tool-calling support
* Select a suitable model for a given machine and use case

---

## 🧠 Key Concepts

### 1. Model Weights

Model weight memory depends mainly on:

* Number of parameters
* Precision / quantization

The basic formula is:

```text
Weights (GB)
= Parameters (B) × Bytes per Parameter
```

---

### 2. Quantization

Quantization reduces the number of bytes used to store model parameters.

Common formats used in this task include:

| Precision   | Bytes / Parameter |
| ----------- | ----------------: |
| FP16 / BF16 |              2.00 |
| Q8_0        |              1.00 |
| Q6_K        |              0.81 |
| Q5_K_M      |              0.68 |
| Q4_K_M      |              0.57 |
| Q3_K_M      |              0.43 |

Lower precision generally reduces memory usage, but may involve some quality loss.

---

### 3. KV Cache and Context Length

The KV cache grows as context length increases.

Approximate formula:

```text
KV Cache (GB)
= Parameters (B) × Context (K) × 0.02
```

The total estimated memory is:

```text
Total (GB)
= (Weights + KV Cache) × 1.10
```

These values are estimates used to determine whether a model is likely to fit. They are not intended to predict actual memory usage to the exact megabyte.

---

## 🛠️ Technologies & Tools

* Python
* Ollama
* Open LLMs
* GGUF
* Quantization
* Model Cards
* Hugging Face
* GitHub
* Visual Studio Code

---

## 📂 Project Structure

```text
AI_Fluency_Day4/
│
├── README.md
├── analysis.md
├── vram_estimate.py
│
└── screenshots/
    ├── estimator_output.png
    ├── context_output.png
    ├── quantization_output.png
    ├── ollama_list.png
    ├── ollama_ps.png
    └── model_cards/
```

The Day 4 submission requires the estimator script, written analysis, and screenshots of the estimator, context/quantization experiments, Ollama outputs, and model-card/licence pages.

---

# 🧮 Memory Estimation

The Python estimator calculates:

```text
Weights
   +
KV Cache
   +
Runtime Overhead
   ↓
Total Estimated Memory
   ↓
Fits / Does Not Fit
```

The estimator also provides a fit verdict based on the available memory.

```text
fits comfortably
fits, but tight
does NOT fit
```

---

# 📊 Example Estimate

For an 8B model using Q4_K_M with an 8K context:

```text
Parameters      = 8B
Precision       = Q4_K_M
Bytes/parameter = 0.57
Context         = 8K

Weights         ≈ 4.56 GB
KV Cache        ≈ 1.28 GB
Total           ≈ 6.42 GB
```

With 8 GB available memory, the estimate is:

```text
fits, but tight
```

The Day 4 lab provides these values as the expected estimator output.

---

# 🔬 Experiments

## Experiment 1 – Context Length

The same 8B Q4_K_M model is tested at different context lengths.

```text
4K
8K
32K
128K
```

The important observation is:

```text
Context increases
      ↓
KV Cache increases
      ↓
Total memory increases
      ↓
Model may stop fitting
```

The model weights remain unchanged while the KV cache grows with context length.

---

## Experiment 2 – Quantization

The same 8B model is tested using different quantization levels:

```text
Q3_K_M
Q4_K_M
Q5_K_M
Q8_0
FP16
```

The weights change when quantization changes.

For example:

```text
Q3_K_M → lower memory
Q4_K_M → moderate memory
Q5_K_M → higher memory
Q8_0   → higher memory
FP16   → highest memory
```

This demonstrates the trade-off between memory usage and precision.

---

# 💻 Ollama Verification

The theoretical estimates are compared with actual model usage using Ollama.

### Check installed models

```bash
ollama list
```

This shows the model size stored on disk.

### Run a model

```bash
ollama run qwen2.5:1.5b
```

### Check memory usage

In another terminal:

```bash
ollama ps
```

`ollama ps` shows actual memory usage and whether the model is running on CPU, GPU, or a split between them.

---

# 📋 Model Comparison

The task compares four open-model families:

* Qwen
* Mistral
* IBM Granite
* gpt-oss

The comparison includes:

* Full model name and version
* Publisher
* Model size
* Parameters
* Context window
* Licence
* Commercial-use conditions
* Tool-calling support
* GGUF / Ollama availability
* Q4 download size
* Estimated memory
* Whether the model fits the selected machine

The model cards and Ollama pages are used as the sources for this comparison.

---

# ⚖️ Open-Weight vs Open-Source

An important learning from Day 4 is that **open-weight does not automatically mean open-source**.

The exact licence determines:

* Whether commercial use is allowed
* Whether redistribution is allowed
* Whether additional conditions apply

The model card and licence must therefore be checked before selecting a model for a real project.

---

# 🎯 Model Selection

Model selection depends on multiple factors:

```text
Model Size
     +
Quantization
     +
Context Length
     +
Memory
     +
Tool Calling
     +
Licence
     ↓
Suitable Model
```

A model that fits in memory may still be unsuitable if its licence does not permit the intended use.

---

# ⚙️ Setup & Run

## 1. Activate the Python Environment

```bash
.venv\Scripts\activate
```

---

## 2. Run the Memory Estimator

```bash
python vram_estimate.py
```

The estimator calculates:

```text
Weights
KV Cache
Total Memory
Fit Verdict
```

The lab requires changing `AVAILABLE_GB` to match the actual RAM or VRAM available on the machine.

---

## 3. Check Ollama

```bash
ollama list
```

Run a small model:

```bash
ollama run qwen2.5:1.5b
```

Then, from another terminal:

```bash
ollama ps
```

---

# 📸 Screenshots

The `screenshots/` folder contains evidence of the Day 4 experiments.

Recommended screenshots:

```text
screenshots/
│
├── estimator_output.png
├── context_output.png
├── quantization_output.png
├── ollama_list.png
├── ollama_ps.png
│
└── model_cards/
    ├── qwen_model_card.png
    ├── mistral_model_card.png
    ├── granite_model_card.png
    └── gpt_oss_model_card.png
```

The lab specifically requires screenshots of the estimator output, context and quantization runs, Ollama outputs, and model-card/licence pages.

---

# 📚 Learning Workflow

```text
Understand Memory Formula
          ↓
Estimate Model Memory
          ↓
Implement Python Estimator
          ↓
Test Context Length
          ↓
Test Quantization
          ↓
Compare With Ollama
          ↓
Read Model Cards
          ↓
Compare Licences
          ↓
Select Suitable Model
          ↓
Document Findings
```

---

# 🧠 Key Learnings

### Memory

Model memory is affected by weights, KV cache, and runtime overhead.

### Context

Increasing context length increases KV-cache memory even though model weights remain unchanged.

### Quantization

Quantization can significantly reduce memory requirements.

### Reality vs Estimate

The formula provides an estimate. Actual memory can differ because of architecture, runtime settings, context defaults, and overhead.

### Licence

Model size alone is not enough to choose a model. The licence determines whether the model can be used for the intended scenario.

---

# 🚀 Conclusion

Day 4 demonstrates how to make an informed decision about running an open model locally.

Before downloading a model, the important questions are:

```text
Will it fit?
      ↓
What quantization should I use?
      ↓
What context length can I support?
      ↓
Does it actually run within my memory?
      ↓
What licence does it have?
      ↓
Can I legally use it for my intended purpose?
```

The final model choice should therefore consider **memory, quantization, context length, tool-calling capability, and licence conditions together**.

---

## 👩‍💻 Author

**Babitha M**

