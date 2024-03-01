## GGUF converter

----

This repository helps the conversion of Large Language Models (LLMs) into GGUF format.

### Install llama.cpp

#### step 1. Clone llama.cpp Repository

```shell
git submodule update --init --recursive
```
<br>

#### step 2. Create environment

```shell
conda  create -n gguf python=3.10
```

<br>

#### step 3. Activate environment

```shell
conda activate gguf
```

<br>

#### step 4. Install dependencies and llama.cpp

```shell
cd llama.cpp &&  make && pip install -r requirements.txt
```
<br>


### Convert Models

To convert Model to GGUF format, run file **gguf.py** with arguments:

* _--model-name_: Specify the model you want to convert
* _--methods_:  Define methods to convert. For example: q2_k, q3_k_m, q4_0, q4_k_m, q5_0, q5_k_m, q6_k, q8_0 Use comma to
  separate methods. default q4_0
* _--local-dir:_ dir to store model from huggingface-hub, default: ./original_model/
* _--quantized-dir_: dir to store quantized model, default: ./quantized_model/

For example:

```shell
python gguf.py "Qwen/Qwen1.5-1.8B" --methods "q4_0"

```