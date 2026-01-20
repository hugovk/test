for v in 3.10.0 3.10.{2..9} 3.10.{11..19}; do
    uv run --managed-python --python $v bench.py
done

for v in 3.11.{4..14}; do
    uv run --managed-python --python $v bench.py
done

for v in 3.12.{0..12}; do
    uv run --managed-python --python $v bench.py
done

for v in 3.13.0rc{2..3} 3.13.{0..11}; do
    uv run --managed-python --python $v bench.py
done

for v in 3.14.0a{3..7} 3.14.0b{1..4} 3.14.0rc{1..3} 3.14.{0..2}; do
    uv run --managed-python --python $v bench.py
done

for v in 3.15.0a{1..2}; do
    uv run --managed-python --python $v bench.py
done
