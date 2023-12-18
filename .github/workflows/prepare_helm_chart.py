import os
import sys
from pathlib import Path
import fileinput

ROOT = Path.cwd()
BRANCH = os.environ["GITHUB_REF_NAME"]
RUN_ID = os.environ["GITHUB_RUN_ID"][:5]
VERSION = ROOT.joinpath("version.txt").read_text().strip().lstrip("v")
CHART = ROOT / "charts" / "vastcsi" / "Chart.yaml"


if __name__ == '__main__':
    is_beta = BRANCH.startswith("beta")
    if is_beta:
        version = f"{VERSION}-beta.{RUN_ID}"
    else:
        version = f"{VERSION}.{RUN_ID}"

    for line in fileinput.input(CHART, inplace=True):
        if line.startswith("version:"):
            line = line.replace(line, f"version: {version}")
        sys.stdout.write(line)

    print("chart content")
    print(CHART.read_text())





