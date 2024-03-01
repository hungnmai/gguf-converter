## GGUF converter

----

```shell
git submodule update --init --recursive
```

```shell
conda  create -n gguf python=3.10
```

```shell
conda activate gguf
```

```shell
cd llama.cpp && LLAMA_CUBLAS=1 make && pip install -r requirements.txt
```

Note: remove LLAMA_CUBLAS=1 if your hardware does has GPU