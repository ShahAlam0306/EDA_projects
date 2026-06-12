# IPL Match Analysis (Exploratory Data Analysis)

## Project Overview

This project performs Exploratory Data Analysis (EDA) on Indian Premier League (IPL) match data to uncover trends related to:

- Match-winning teams
- Toss decisions
- Toss impact on match outcomes
- Winning methods (Runs/Wickets)
- Player performances
- Top scorers and bowlers
- Venue analysis
- Custom cricket insights

The project uses Python libraries such as Pandas, NumPy, Matplotlib, Seaborn, and Plotly for data analysis and visualization.

---

## Objectives

The main goals of this analysis are:

1. Identify the most successful IPL teams.
2. Analyze toss decision patterns.
3. Determine whether winning the toss affects match results.
4. Explore common match-winning methods.
5. Identify top-performing players.
6. Find the highest individual batting scores.
7. Analyze bowling performances.
8. Study venue trends and match distribution.

---

## Dataset Features

Key columns used in the analysis:

- match_id
- venue
- toss_winner
- toss_decision
- match_winner
- won_by
- margin
- player_of_the_match
- top_scorer
- highscore
- best_bowling
- best_bowling_figure

---

## Libraries Used

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px