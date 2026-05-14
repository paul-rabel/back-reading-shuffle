# back-reading-shuffle

This program shuffles a list of teaching assistants and assigns two unique TAs for each person to backread.

It now supports workload balancing: if some TAs have more submissions than others, the script tries to distribute total backreading work as evenly as possible.

Run:
```bash
python3 pair_selector.py
```

## Inputs

- `ta_workload.csv`: two columns where column 1 is TA name and column 2 is workload count (for example, number of HWs).

Example `ta_workload.csv`:
```csv
name,workload
name1 ,3
name2 ,8
name3 ,5
```

## Output

- `backreading.xlsx` with one row per TA and two assigned review targets.
