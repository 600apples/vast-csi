import os
import sys
from pathlib import Path
import fileinput

ROOT = Path.cwd()
BRANCH = os.environ["GITHUB_REF_NAME"]
SHA = os.environ["GITHUB_SHA"][:7]
VERSION = ROOT.joinpath("version.txt").read_text().strip().lstrip("v")
CHART = ROOT / "charts" / "vastcsi" / "Chart.yaml"

if __name__ == '__main__':
    is_beta = BRANCH.startswith("beta")

    release_name_template = "helm-{{ .Version }}"
    pages_branch = "gh_pages_beta" if is_beta else "gh-pages"
    skip_upload = "true" if is_beta else "false"
    version = f"{VERSION}-beta.{SHA}" if is_beta else f"{VERSION}-{SHA}"

    for line in fileinput.input(CHART, inplace=True):
        if line.startswith("version:"):
            line = line.replace(line, f"version: {version}\n")
        sys.stdout.write(line)

    ROOT.joinpath("releaser-config.yaml").open("w").write(
        f"""
            pages-branch: {pages_branch}
            release-name-template: {release_name_template}
        """)
