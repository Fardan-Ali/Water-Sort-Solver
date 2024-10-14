# Water Sort Puzzle Solver

A Python program that solves the **Water Sort Puzzle**, a logic game where the goal is to sort colored water in tubes until each tube contains water of only one color.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [Contact](#contact)

## Overview

The **Water Sort Puzzle Solver** is a Python-based tool designed to solve Water Sort puzzles using a Greedy Best First Search Algorithm. Each puzzle consists of several tubes (of varying quantity), each containing mixed colors of water. The objective is to sort the water so that each tube contains water of only one color.
The program asks you to input the initial state of the puzzle and outputs an efficient step-by-step solution.

Here's an example puzzle:

![image](https://github.com/user-attachments/assets/36a200ed-f4e9-406c-812a-f826e126fd5f)


## Features
- Solves any valid Water Sort puzzle with any number of tubes and colors.
- Provides a step-by-step solution.
- Detects invalid or unsolvable puzzle configurations.
- Efficient GBFS search algorithm for quick solutions.

## Installation

### Prerequisites:
- Python 3.x
- Recommended: A virtual environment (optional)

### Steps:
Simply download the python file or clone this repository to your local machine:

```bash
git clone https://github.com/username/water-sort-solver.git
cd water-sort-solver
```

## Usage
To use the Water Sort Solver, you need to input the initial state of the puzzle. You must enter the number of tubes, and the colours in each tube **from bottom to top**. For an empty tube, simply type 'em' or 'empty'. The code will provide you with abbreviations for all colours.

Example Input:

```
Enter the number of starting tubes: 3
...        
What's in tube 1? re re ye re
What's in tube 2? ye ye re ye
What's in tube 3? em
```

The program will then output the steps to solve the puzzle, for example:

```
Move from tube 2 to tube 3
Move from tube 1 to tube 2
Move from tube 1 to tube 3
Move from tube 2 to tube 1
Move from tube 2 to tube 3

Puzzle solved in 5 steps!
```


## Contributing
Contributions/Additions are welcome. Here's how you can contribute:

1.  Fork the repository.
2.  Create a feature branch: git checkout -b feature/my-new-feature.
3.  Commit your changes: git commit -m 'Add new feature'.
4.  Push to the branch: git push origin feature/my-new-feature.
5.  Open a pull request.

## Contact
For questions, feedback, or suggestions, feel free to reach out.
