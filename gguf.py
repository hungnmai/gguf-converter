import os
import typer
from fastapi import FastAPI
from huggingface_hub import snapshot_download

app = typer.Typer()

fast_app = FastAPI()


@app.command()
def main(
    model_name: str,
    methods: str = typer.Option(
        default="q4_0",
        help="Define methods to convert. "
        "For example: q2_k, q3_k_m, q4_0, q4_k_m, q5_0, q5_k_m, q6_k, q8_0 "
        "Use comma to separate methods.",
    ),
    local_dir: str = typer.Option(default="./original_model/", help="dir to store model from huggingface-hub"),
    quantized_dir: str = typer.Option(default="./quantized_model/", help="dir to store quantized model"),
) -> None:
    # download model from huggingface-hub to base_model
    snapshot_download(
        repo_id=model_name,
        local_dir=local_dir,
        cache_dir=local_dir,
        local_dir_use_symlinks=False,
    )
    if not os.path.exists(quantized_dir):
        os.makedirs(quantized_dir)

    original_model = os.path.join(quantized_dir, "FP16.gguf")
    if not os.path.exists(original_model):
        command = f"python llama.cpp/convert-hf-to-gguf.py {local_dir} --outtype f16 --outfile {original_model}"

        os.system(command)
    list_methods = [method.strip() for method in methods.split(",")]
    for m in list_methods:
        filename = f"{m.upper()}.gguf"
        output_file = os.path.join(quantized_dir, filename)
        quantized_quantize = f"llama.cpp/quantize {original_model} {output_file} {m}"
        os.system(quantized_quantize)
        print(f"Quantized model saved to: {output_file}")


if __name__ == "__main__":
    # model_name = "Qwen/Qwen1.5-1.8B"
    app()
