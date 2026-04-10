# Advent of Code 2023 — Python Solutions

Complete Python solutions for all 25 days of [Advent of Code 2023](https://adventofcode.com/2023), written by **Steve de Rose**.

---

## Overview

[Advent of Code](https://adventofcode.com/) is an annual programming challenge that runs through December, with a new two-part puzzle released each day from December 1 to 25. This repository contains solutions for every puzzle of the 2023 edition, each implemented in a single, self-contained Python script.

---

## Repository Structure

```
AdventOfCode/
├── day_01.py       # Solution for Day 1
├── day_02.py       # Solution for Day 2
│   ...
├── day_25.py       # Solution for Day 25
├── input_01.txt    # Puzzle input for Day 1
├── input_02.txt    # Puzzle input for Day 2
│   ...
└── input_25.txt    # Puzzle input for Day 25
```

Each `day_XX.py` script reads its corresponding `input_XX.txt` file from the same directory and prints the answers for Part 1 and Part 2.

---

## Prerequisites

- **Python 3.10+** (required for `math.lcm` and structural pattern matching)
- The following third-party packages:

| Package | Used in |
|---------|---------|
| [NumPy](https://numpy.org/) | Days 1, 3, 4, 10, 11, 14, 17 |
| [Shapely](https://shapely.readthedocs.io/) | Day 18 |

Install dependencies with pip:

```bash
pip install numpy shapely
```

---

## Running a Solution

From the repository root, run any day's solution with:

```bash
python day_XX.py
```

For example:

```bash
python day_01.py
```

Each script expects its input file (`input_XX.txt`) to be present in the current working directory.

---

## Puzzle Solutions

### Day 1 — Trebuchet?!

Recover calibration values from a document where each line encodes a two-digit number. Part 1 considers only digit characters; Part 2 also treats spelled-out words (`one`, `two`, …, `nine`) as valid digits.

**Approach:** NumPy array indexing to find the leftmost/rightmost occurrence of each digit pattern in every line.

---

### Day 2 — Cube Conundrum

An Elf shows you handfuls of coloured cubes drawn from a bag. Part 1 finds which games are possible given a limited supply of red, green, and blue cubes. Part 2 finds the minimum cube counts needed for each game.

**Approach:** Parse each reveal set and track the per-colour maximums; compute validity and product accordingly.

---

### Day 3 — Gear Ratios

An engine schematic is a 2-D grid of digits, symbols, and dots. Part 1 sums all part numbers (numbers adjacent to any symbol). Part 2 sums the gear ratios: for every `*` symbol adjacent to exactly two part numbers, multiply those numbers.

**Approach:** NumPy grid with neighbour scanning; a dictionary keyed by `*` positions collects adjacent numbers for gear ratio computation.

---

### Day 4 — Scratchcards

Each scratchcard lists winning numbers and numbers you have. Part 1 scores cards by powers of two. Part 2 uses a cascade rule where winning cards create copies of subsequent cards.

**Approach:** Set intersection to count matches; NumPy accumulation for the card-copy cascade.

---

### Day 5 — If You Give A Seed A Fertilizer

A series of mapping stages converts seed numbers to locations. Part 1 processes individual seeds; Part 2 treats the seed list as ranges and finds the minimum location.

**Approach:** Iterative range splitting as each mapping stage is applied, avoiding expansion of the full integer ranges.

---

### Day 6 — Wait For It

Toy boat races: holding the button charges speed, releasing it lets the boat travel. Count the number of whole-millisecond hold times that beat the record distance. Part 2 treats all race figures as one large number.

**Approach:** Solve the resulting quadratic inequality analytically to find the winning hold-time range in O(1).

---

### Day 7 — Camel Cards

Rank hands of five cards using poker-like hand types. Part 1 uses standard ordering; Part 2 treats `J` as a wild joker that maximises hand strength.

**Approach:** Encode hand type and card values into a numeric score for sorting; joker logic promotes the rarest card group.

---

### Day 8 — Haunted Wasteland

Navigate a network of nodes following a left/right instruction pattern. Part 1 finds the step count from `AAA` to `ZZZ`. Part 2 starts simultaneously from all `**A` nodes and finds when all paths reach a `**Z` node.

**Approach:** BFS/trace per starting node; Least Common Multiple of individual cycle lengths gives the answer for Part 2.

---

### Day 9 — Mirage Maintenance

Extrapolate the next (and previous) value in sequences by repeatedly computing differences until all zeros.

**Approach:** Recursive difference computation; accumulate last (or first) elements back up the stack.

---

### Day 10 — Pipe Maze

A 2-D grid of pipe segments contains a single large loop. Part 1 finds the furthest point along the loop. Part 2 counts tiles enclosed by the loop.

**Approach:** BFS to trace the loop; ray-casting / winding number on the resulting path matrix to count interior points.

---

### Day 11 — Cosmic Expansion

A 2-D image of galaxies expands: empty rows and columns double (Part 1) or grow by a factor of one million (Part 2). Sum the Manhattan distances between every pair of galaxies.

**Approach:** Identify empty rows/columns, adjust galaxy coordinates by a scaling multiplier, then sum pairwise distances.

---

### Day 12 — Hot Springs

Each row of a spring condition record contains damaged (`#`), operational (`.`), and unknown (`?`) springs, plus a list of contiguous damaged-group sizes. Count the number of valid arrangements. Part 2 unfolds each record fivefold.

**Approach:** Recursive dynamic programming with `functools.cache` (memoisation); bottom-up placement of each group.

---

### Day 13 — Point of Incidence

Each pattern of ash (`.`) and rocks (`#`) has a line of reflection — either horizontal or vertical. Part 1 finds the exact mirror line; Part 2 finds the mirror line with exactly one smudge corrected.

**Approach:** Compare rows/columns around each candidate mirror axis; count differences to distinguish exact vs. one-smudge reflection.

---

### Day 14 — Parabolic Reflector Dish

Round rocks (`O`) slide in a direction until stopped by cube rocks (`#`) or the edge. Load is the sum of distances from the south edge. Part 1 tilts north once; Part 2 runs one billion tilt cycles (N/W/S/E).

**Approach:** In-place sliding along NumPy array rows/columns; cycle detection on the serialised grid state to shortcut the billion iterations.

---

### Day 15 — Lens Library

A custom HASH algorithm maps strings to box numbers (0–255). Part 1 sums the HASH of each step in the initialisation sequence. Part 2 simulates a lens-box system with `=` (insert/replace) and `-` (remove) operations, then computes the total focusing power.

**Approach:** Direct simulation with ordered lists per box; use the HASH function for routing.

---

### Day 16 — The Floor Will Be Lava

A beam of light enters a grid of mirrors (`/`, `\`) and splitters (`|`, `-`). Count energised tiles. Part 1 uses a fixed entry point; Part 2 tries every edge tile and direction to find the maximum.

**Approach:** BFS/DFS propagation tracking `(position, direction)` pairs; visited-set deduplication.

---

### Day 17 — Clumsy Crucible

Find the path through a city grid that minimises total heat loss, subject to constraints on straight-line run lengths. Part 1 allows 1–3 consecutive steps in one direction; Part 2 (ultra crucible) requires 4–10.

**Approach:** Dijkstra's algorithm with state `(position, direction, consecutive_steps)`.

---

### Day 18 — Lavaduct Lagoon

A digging machine follows a series of directional instructions to carve a lagoon. Part 1 uses short distances encoded in the instruction text; Part 2 decodes much larger distances from hexadecimal colour values.

**Approach:** Shoelace formula (Gauss's area formula) to compute polygon area, combined with Pick's theorem to count interior integer points.

---

### Day 19 — Aplenty

Machine parts with four ratings (`x`, `m`, `a`, `s`) are routed through named workflows of conditional rules until accepted or rejected. Part 1 sums the ratings of all accepted parts. Part 2 counts distinct rating combinations that lead to acceptance.

**Approach:** Recursive interval splitting: propagate 4-D rating ranges through the workflow tree, splitting on each condition.

---

### Day 20 — Pulse Propagation

A network of flip-flop and conjunction modules propagates low/high pulses. Part 1 counts low and high pulses after 1 000 button presses. Part 2 finds the number of presses until the `rx` module receives a single low pulse.

**Approach:** Simulate pulse propagation with a queue; detect periods of the conjunction modules feeding `rx` and compute their LCM.

---

### Day 21 — Step Counter

Starting from a fixed position in a garden grid, count reachable plots in exactly N steps. Part 1 uses N = 64 on a finite grid; Part 2 uses N = 26 501 365 on an infinitely tiling grid.

**Approach:** BFS for Part 1; for Part 2, observe that the answer is a quadratic function of the number of full grid widths traversed and apply Lagrange interpolation.

---

### Day 22 — Sand Slabs

Simulate bricks of sand falling and coming to rest. Part 1 counts bricks that can be safely disintegrated (are not the sole support of any other brick). Part 2 sums, for each brick, how many others would fall if it were removed.

**Approach:** Let bricks settle by checking occupied positions; build a support graph (which bricks rest on which) then analyse support sets.

---

### Day 23 — A Long Walk

Find the longest hike through a maze. Part 1 treats slope tiles as one-way; Part 2 ignores slopes, making the graph undirected.

**Approach:** Compress the grid into a weighted graph of junctions; exhaustive DFS with backtracking to find the longest path.

---

### Day 24 — Never Tell Me The Odds

Hailstones travel in straight lines with constant velocity. Part 1 counts pairs whose 2-D paths intersect within a test area (ignoring time). Part 2 finds the initial position and velocity of a rock thrown to hit every hailstone.

**Approach:** Analytic line-intersection for Part 1; numerical Newton–Raphson root-finding (Jacobian-based) for Part 2.

---

### Day 25 — Snowverload

Find three edges in an undirected graph whose removal splits it into exactly two connected components, then return the product of the two component sizes.

**Approach:** Probabilistic Monte Carlo edge-frequency method: sample many random shortest paths; the three edges on the minimum cut appear most frequently and are used as the cut candidates.

---

## Author

**Steve de Rose** — Solutions written in December 2023.
