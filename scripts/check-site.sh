#!/usr/bin/env bash
set -eu

site_dir="${1:-public}"

if grep -Eiq 'javascript:|<script|<style|<iframe|on[a-z]+[[:space:]]*=' data/talks.json; then
  echo "unsafe executable HTML pattern found in curated talk data" >&2
  exit 1
fi

for expected in index.html presentations.html CNAME; do
  if [[ ! -f "${site_dir}/${expected}" ]]; then
    echo "missing generated file: ${site_dir}/${expected}" >&2
    exit 1
  fi
done

html_count="$(find "${site_dir}" -type f -name '*.html' | wc -l | tr -d ' ')"
if [[ "${html_count}" != "2" ]]; then
  echo "expected exactly two generated HTML routes; found ${html_count}" >&2
  find "${site_dir}" -type f -name '*.html' -print >&2
  exit 1
fi

for forbidden in bacher planning projects.md 404.md _data _layouts _includes; do
  if [[ -e "${site_dir}/${forbidden}" ]]; then
    echo "source-only or retired path leaked into output: ${site_dir}/${forbidden}" >&2
    exit 1
  fi
done

if find "${site_dir}" -type f \( -name '*.md' -o -name '*.toml' -o -name '*.js' \) -print | grep -q .; then
  echo "source or production JavaScript leaked into generated output" >&2
  exit 1
fi

echo "validated generated site boundary in ${site_dir}"
