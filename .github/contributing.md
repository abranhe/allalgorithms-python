## Contributing

> Please note that this project is released with a [Contributor Code of Conduct](code-of-conduct.md). By participating in this project you agree to abide by its terms.

##  See

- [General Rules](#general-rules)
- [All ▲lgorithms Structure](#all-lgorithms-python-library-structure)
- [Adding new algorithms](#adding-new-algorithms)
- [Style](#style)
- [Adding Documentation](#adding-documentation)

### General Rules

- As much as possible, try to follow the existing format of markdown and code.

### All ▲lgorithms Python Library Structure

- Directories and files are all in lower case letter.
- Files are separated by an underscore (`_`) following the `snake_case` style.
- Directories in documentation are separated by a minus or hyphen (`-`) following `kebeab-case` style.

> We follow this structure

```
├── allalgorithms
│   │── sorting
|   |    │── bubble_sort.py
|   |    └── merge_sort.py
│   └── searches
|        │── binary_search.py
|        └── linear_search.py
├── docs
│   │── sorting
|   |    │── bubble-sort.md
|   |    └── merge-sort.md
│   └── searches
|        │── binary-search.md
|        └── linear-search.md
└── tests
    │── test_searches.py
    └── test_sorting.py
```

### Adding new algorithms

- Make your pull requests to be **specific** and **focused**. Instead of contributing "several algorithms" all at once contribute them all one by one separately (i.e. one pull request for "Binary Search", another one
for "Bubble Sort" and so on).
- Describe what you do in code using **comments**.

### Style

<p id="changelog">Please <b>DO NOT EDIT CHANGELOG</b> on your pull requests, this is must be edited by one of the write access maintainers when they going to drop a new release.</p> 

This repository follow the [PEP8 Style Gide for Python](https://www.python.org/dev/peps/pep-0008/), so make sure you lint your code before adding a new pull request.

Each `.py` file should have the following header. (no for testing files)

```py
# -*- coding: UTF-8 -*-
#
# Binary search works for a sorted array.
# The All ▲lgorithms library for python
#
# Contributed by: Carlos Abraham Hernandez
# Github: @abranhe
#
```

If the algorithm is modified, this should be included there also.

```py
# Contributed by: Carlos Abraham Hernandez
# Github: @abranhe
#
# Modified by: Your Name
# Github: @yourgithubusername
```

If the algorithm have been modified by multiple contributors, that should be included as follow.

```py
# Contributed by: Carlos Abraham Hernandez
# Github: @abranhe
#
# Modifiers:
# Your Name, @yourgithubusername
# Your friend's name, @yourfriendongithub
```

### Adding Documentation

Please make sure if you add an algorithm, you also add the required
documentation for it the `/docs` directory.

Follow some of the examples already added.

If you are modifying an algorithm make sure you add a benchmark using [Repl.it](https://repl.it/) for the maintainers to have it easy to review it.


#### Lastly and not less important:

Make sure you start ⭐️ the project and follow [@abranhe](https://git.io/abranhe)
