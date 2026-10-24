import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / ".agents/learning/utility/guide-build/scripts/guide_build.py"


class GuideBuildTests(unittest.TestCase):
    def test_scaffold_then_builds_anchored_excerpt(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            repo = Path(temporary)
            subprocess.run(
                [sys.executable, str(SCRIPT), "scaffold", "--repo", str(repo)],
                check=True,
            )
            (repo / "request.cpp").write_text(
                "// learning:request\nsubmit();\n// learning:end-request\n",
                encoding="utf-8",
            )
            (repo / "guide/lessons/first-lesson.md").write_text(
                "# Request\n\n<!-- excerpt: request.cpp#request -->\n", encoding="utf-8"
            )
            subprocess.run(
                [sys.executable, str(SCRIPT), "build", "--repo", str(repo)], check=True
            )
            self.assertIn(
                "submit();", (repo / "guide/index.html").read_text(encoding="utf-8")
            )

    def test_build_rejects_missing_excerpt(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            repo = Path(temporary)
            subprocess.run(
                [sys.executable, str(SCRIPT), "scaffold", "--repo", str(repo)],
                check=True,
            )
            (repo / "guide/lessons/first-lesson.md").write_text(
                "<!-- excerpt: absent.cpp#request -->\n", encoding="utf-8"
            )
            result = subprocess.run(
                [sys.executable, str(SCRIPT), "build", "--repo", str(repo)],
                capture_output=True,
                text=True,
            )
            self.assertNotEqual(0, result.returncode)
            self.assertIn("missing excerpt source", result.stderr)
