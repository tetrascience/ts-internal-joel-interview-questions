## Data Lake Transaction Processing Interview
#
# Background:
# You're working with a data lake that stores customer transaction data. The current
# schema is rigid, using a predefined structure for data stored in files. As the business
# evolves, new fields need to be added, existing fields might change types, and some
# fields may become obsolete.
#
# The interview has 3 stages:
#
# Stage 1: Load transactions1.json and implement get_store_dollar_totals()
#   - Parse the JSON file and create Transaction objects
#   - Track store dollar totals incrementally (don't iterate transactions list after loading)
#   - Run: python stage1-test.py
#
# Stage 2: Add transactions2.json and implement get_store_item_totals() and get_item_total()
#   - Load additional transaction data (same schema as stage 1)
#   - Track item counts per store incrementally
#   - Run: python stage2-test.py
#
# Stage 3: Handle schema evolution with transactions3.json and transactions4.json
#   - transactions3.json: replaces items_count with an items[] array (no tax field)
#   - transactions4.json: adds tax field back, still uses items[] array
#   - Update your schema and aggregation logic to handle both formats
#   - Run: python stage3-test.py

import json
from dataclasses import dataclass
from typing import Dict, Optional, List
from datetime import datetime

# Hint: You'll need to handle schema evolution in later stages
@dataclass
class TransactionSchema:
  transaction_id: str
  customer_id: str
  timestamp: datetime
  amount: float
  store_id: str
  payment_method: Optional[str] = None
  # TODO: Add fields for items_count, tax, and items as needed

# Hint: Use module-level dictionaries to track running totals
# store_dollar_totals = {}

def add_transaction_data(path: str):
  """Read transaction data from JSON file and update running totals.

  Hint: Parse each transaction, create a TransactionSchema object,
  and update your running totals in the same pass.
  """
  transactions = []

  # TODO: Implement loading and aggregation

  return transactions

def get_store_dollar_totals() -> Dict[str, float]:
  """Return total dollars (amount + tax) per store.

  This should NOT iterate the transactions list - use pre-computed totals.
  """
  # TODO: Implement
  pass

def get_store_item_totals() -> Dict[str, int]:
  """Return total item count per store.

  This should NOT iterate the transactions list - use pre-computed totals.
  """
  # TODO: Implement
  pass

def get_item_total() -> int:
  """Return the total number of items across all stores."""
  # TODO: Implement
  pass


# Uncomment and add more files as you progress through stages:
# transactions = add_transaction_data("./data/transactions1.json")
# transactions = add_transaction_data("./data/transactions2.json")
# transactions = add_transaction_data("./data/transactions3.json")
# transactions = add_transaction_data("./data/transactions4.json")
