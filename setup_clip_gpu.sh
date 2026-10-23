#!/usr/bin/env bash
set -euo pipefail

project_root="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
torch_backend="${1:-auto}"

if ! command -v uv >/dev/null 2>&1; then
    printf '%s\n' 'Install uv on this server before running this script.' >&2
    exit 1
fi

if [[ ! -x "$project_root/.venv/bin/python" ]]; then
    uv venv --python 3.12 "$project_root/.venv"
fi

# Replace both CPU builds even when their public versions already match.
uv pip install \
    --python "$project_root/.venv/bin/python" \
    --torch-backend "$torch_backend" \
    --reinstall-package torch \
    --reinstall-package torchvision \
    -r "$project_root/requirements-clip.txt" \
    pip

"$project_root/.venv/bin/python" - <<'PY'
import torch
import torchvision

if not torch.cuda.is_available():
    raise SystemExit(
        f"CUDA is unavailable: torch={torch.__version__}, CUDA build={torch.version.cuda}. "
        "Check the NVIDIA driver and, if necessary, choose a compatible backend "
        "with bash setup_clip_gpu.sh cu128 (or cu126)."
    )
print(f"PyTorch: {torch.__version__}; torchvision: {torchvision.__version__}")
print(f"CUDA build: {torch.version.cuda}")
print(f"GPU: {torch.cuda.get_device_name(0)}")
print("GPU environment ready. No CLIP model or inference has been run.")
PY
