# Expected results for each stage of the interview
# These are cumulative totals after loading each set of transaction files

from typing import Dict, TypedDict

class Results(TypedDict):
  store_dollars: Dict[str, float]
  store_items: Dict[str, int]
  total_items: int

# Stage 1: After loading transactions1.json only
transactions_1_expected: Results = {
  "store_dollars": {
    "S001": 375.5,
    "S002": 89.99,
    "S003": -250.0
  },
  "store_items": {
    "S001": 7,
    "S002": 1,
    "S003": 0
  },
  "total_items": 8
}

# Stage 2: After loading transactions1.json + transactions2.json
transactions_2_expected: Results = {
  "store_dollars": {
    "S001": 805.28,
    "S002": 280.01,
    "S003": -36.55000000000001,
    "S004": 612.54,
    "S005": 544.1899999999999,
    "S007": 156.92
  },
  "store_items": {
    "S001": 10,
    "S002": 2,
    "S003": 2,
    "S004": 12,
    "S005": 13,
    "S007": 5
  },
  "total_items": 44
}

# Stage 3 intermediate: After loading transactions1-3.json
transactions_3_expected: Results = {
  "store_dollars": {
    "S001": 1061.76,
    "S002": 485.25,
    "S003": 58.93999999999998,
    "S004": 1427.4699999999998,
    "S005": 1145.11,
    "S007": 444.87
  },
  "store_items": {
    "S001": 13,
    "S002": 4,
    "S003": 4,
    "S004": 19,
    "S005": 21,
    "S007": 10
  },
  "total_items": 71
}

# Stage 3 final: After loading all 4 transaction files
transactions_4_expected: Results = {
  "store_dollars": {
    "S001": 1318.24,
    "S002": 690.49,
    "S003": 154.42999999999998,
    "S004": 2242.3999999999996,
    "S005": 1746.03,
    "S007": 773.6199999999999
  },
  "store_items": {
    "S001": 16,
    "S002": 6,
    "S003": 6,
    "S004": 26,
    "S005": 29,
    "S007": 15
  },
  "total_items": 98
}
