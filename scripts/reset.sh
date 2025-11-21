#!/usr/bin/env bash
# Reset repository to last committed state (macOS/Linux)
set -euo pipefail
cd "$(dirname "$0")/.."
git restore --source=HEAD --worktree --staged -S .
git.clean_output=$(git clean -fdx)
echo "Repo reset to last commit."
