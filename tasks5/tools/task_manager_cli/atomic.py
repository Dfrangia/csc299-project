import os
import tempfile
import shutil


def atomic_write(filepath: str, content: str) -> None:
    dirname = os.path.dirname(filepath) or "."
    with tempfile.NamedTemporaryFile(mode='w', dir=dirname, delete=False) as tmp:
        tmp.write(content)
        tmp_path = tmp.name
    try:
        shutil.move(tmp_path, filepath)
    except Exception:
        os.unlink(tmp_path)
        raise

