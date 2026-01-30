"""Stage 1 Test: Validates get_store_dollar_totals() after loading transactions1.json"""

import sys
from results import transactions_1_expected

# Import the candidate's solution from main.py
from main import add_transaction_data, get_store_dollar_totals

def test_stage1():
  """Test that store dollar totals match expected values after loading transactions1.json"""

  # Load the first transaction file
  add_transaction_data("./data/transactions1.json")

  # Get the actual results
  actual_store_dollars = get_store_dollar_totals()
  expected_store_dollars = transactions_1_expected["store_dollars"]

  # Validate results
  passed = True

  print("=" * 60)
  print("Stage 1 Test: get_store_dollar_totals()")
  print("=" * 60)

  # Check if function returns None
  if actual_store_dollars is None:
    print("❌ FAIL: get_store_dollar_totals() returned None")
    print("   Hint: Make sure to return the store_dollar_totals dictionary")
    print("=" * 60)
    return False

  # Check if all expected stores are present
  for store_id, expected_amount in expected_store_dollars.items():
    if store_id not in actual_store_dollars:
      print(f"❌ FAIL: Missing store {store_id}")
      passed = False
    elif abs(actual_store_dollars[store_id] - expected_amount) > 0.01:
      print(f"❌ FAIL: Store {store_id}")
      print(f"   Expected: ${expected_amount:.2f}")
      print(f"   Actual:   ${actual_store_dollars[store_id]:.2f}")
      passed = False
    else:
      print(f"✓ PASS: Store {store_id} = ${actual_store_dollars[store_id]:.2f}")
  
  # Check for unexpected stores
  for store_id in actual_store_dollars:
    if store_id not in expected_store_dollars:
      print(f"❌ FAIL: Unexpected store {store_id}")
      passed = False
  
  print("=" * 60)
  if passed:
    print("✓ Stage 1 PASSED!")
    print("=" * 60)
    return True
  else:
    print("❌ Stage 1 FAILED")
    print("=" * 60)
    return False


if __name__ == "__main__":
  success = test_stage1()
  sys.exit(0 if success else 1)

