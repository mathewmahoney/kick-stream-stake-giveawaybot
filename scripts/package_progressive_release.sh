#!/usr/bin/env bash

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
RELEASE_DIR="${REPO_ROOT}/release/progressive"
ZIP_PATH="${REPO_ROOT}/release/progressive-release.zip"

FILES=(
  "progressive.html"
  "ice_logo.png"
  "ice_overlay.jpg"
)

rm -rf "${RELEASE_DIR}"
mkdir -p "${RELEASE_DIR}"

for file in "${FILES[@]}"; do
  cp "${REPO_ROOT}/${file}" "${RELEASE_DIR}/${file}"
done

rm -f "${ZIP_PATH}"
(
  cd "${RELEASE_DIR}"
  zip -q -r "${ZIP_PATH}" .
)

echo "Created release package at: ${ZIP_PATH}"
