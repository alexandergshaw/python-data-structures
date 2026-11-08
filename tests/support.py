import contextlib
import importlib.util
import io
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load_answer(module, filename):
    path = ROOT / "assignments" / module / filename
    spec = importlib.util.spec_from_file_location(f"{module}_{path.stem}", path)
    loaded = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(loaded)
    return loaded
