# ujson manylinux toolchain benchmark

Throwaway experiment for [ultrajson/ultrajson#741](https://github.com/ultrajson/ultrajson/issues/741):
does building Linux wheels with the newer manylinux image (gcc 14) give a free
speed-up over the older `manylinux2014` image (gcc 10)?

`benchmark.py` and `sample.json` are copied verbatim from `ultrajson/ultrajson`
`tests/`.

## Committed wheels

Both sets come from the **same CI run and commit** — the "build both variants"
deploy now produces manylinux2014 and manylinux_2_28 wheels side by side — so
they are guaranteed identical source and the only variable is the compiler.

| dir | image | gcc | source |
|-----|-------|-----|--------|
| `wheels/manylinux2014/`  | manylinux2014  | 10.2.1 | hugovk/ultrajson run 27506564289 (commit `b6a55af`) |
| `wheels/manylinux_2_28/` | manylinux_2_28 | 14.2.1 | hugovk/ultrajson run 27506564289 (commit `b6a55af`) |

CPython 3.10–3.14 (incl. free-threaded 3.14t), `x86_64` + `aarch64`.

## What CI does

`.github/workflows/ujson-bench.yml` runs a matrix of
`{ubuntu-latest (x86_64), ubuntu-24.04-arm (aarch64)} × {3.10–3.14, 3.14t}`.
Each job installs the old-toolchain wheel, runs the benchmark, then force-
reinstalls the new-toolchain wheel and runs it again — same interpreter, same
machine, only the `.so` differs. Results are appended to the job summary.

A local aarch64 run (Docker, Python 3.11) showed the newer toolchain mostly
wins on **encode** paths (string-array encode ~2×, UTF-8 encode +50%, dict
encode +23%); decode gains were milder (~3–12%). This CI run checks whether
that holds on x86_64 and across Python versions.
