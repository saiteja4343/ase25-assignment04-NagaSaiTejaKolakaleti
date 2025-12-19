# SmartCater 

This is a prototype for SmartCater, an ingredient-ordering service for catering. The prototype focuses on meal search functionality.

## What This Does

Users can search for meals in three ways:
- By meal name (e.g., "chicken")
- By ingredient (e.g., "lettuce")
- By category (e.g., "vegan", "gluten-free", "quick meals")

The program includes sample meals and demonstrates all three search types.

## Requirements

- Python 3.x

## How to Run

1. Make sure you have Python installed
2. Open terminal in the project folder
3. Run the program:

```python
python smart_cater.py
```

or 

```python
python3 smart_cater.py
```

The demo will automatically run and show search results for different queries.

## Project Structure

```
ase25-assignment04-NagaSaiTejaKolakaleti/
├── README.md # This file
├── smart_cater.py # Main implementation
└── requirements/
    ├── functional.md # All functional requirements
    ├── nonfunctional.md # All non-functional requirements
    ├── selected.md # Selected FR and NFR with justification
    └── nfr_explanation.md # How code meets the NFR
```

## Implementation Details

The code uses two main classes:
- **Meal**: Stores meal name, ingredients list, and category
- **MealCatalog**: Manages the meal collection and provides search methods

All data is stored in memory using Python lists. No database is needed for this prototype.