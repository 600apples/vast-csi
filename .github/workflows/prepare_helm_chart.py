import os
from pathlib import Path

ROOT = Path.cwd()
BRANCH = os.environ["GITHUB_REF_NAME"]
RUN_ID = os.environ["GITHUB_RUN_ID"][:5]
VERSION = ROOT.joinpath("version.txt").read_text().strip().lstrip("v")


if __name__ == '__main__':
    is_beta = BRANCH.startswith("beta")
    if is_beta:
        version = f"{VERSION}-beta.{RUN_ID}"
    else:
        version = f"{VERSION}.{RUN_ID}"


    print(f"version: {version}")







