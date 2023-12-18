import os
from pathlib import Path

ROOT = Path.cwd()
BRANCH = os.environ["GITHUB_REF_NAME"]
RUN_ID = os.environ["GITHUB_RUN_ID"]
VERSION = ROOT.joinpath("version.txt").read_text().strip()


if __name__ == '__main__':
    print(f"branch {BRANCH}")
    print(f"name=run_id {RUN_ID}")
    print(f"name=version {VERSION}")







