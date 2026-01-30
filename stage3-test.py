"""Stage 3 Test: Validates schema evolution handling with all 4 transaction files"""

import sys
from results import transactions_4_expected

# Import the candidate's solution from main.py
from main import add_transaction_data, get_store_dollar_totals, get_store_item_totals, get_item_total

def test_stage3():
  """Test handling of schema evolution across all 4 transaction files"""
  
  # Load all transaction files (with different schemas)
  add_transaction_data("./data/transactions1.json")  # items_count, no tax
  add_transaction_data("./data/transactions2.json")  # items_count, no tax
  add_transaction_data("./data/transactions3.json")  # items array, no tax
  add_transaction_data("./data/transactions4.json")  # items array, with tax
  
  passed = True
  
  print("=" * 60)
  print("Stage 3 Test: Schema Evolution")
  print("=" * 60)
  
  # Test store dollar totals (should include tax from transactions4.json)
  print("\n--- Store Dollar Totals (amount + tax) ---")
  actual_store_dollars = get_store_dollar_totals()
  expected_store_dollars = transactions_4_expected["store_dollars"]

  if actual_store_dollars is None:
    print("❌ FAIL: get_store_dollar_totals() returned None")
    passed = False
  else:
    for store_id, expected_amount in expected_store_dollars.items():
      if store_id not in actual_store_dollars:
        print(f"❌ FAIL: Missing store {store_id}")
        passed = False
      elif abs(actual_store_dollars[store_id] - expected_amount) > 0.01:
        print(f"❌ FAIL: Store {store_id} dollars")
        print(f"   Expected: ${expected_amount:.2f}")
        print(f"   Actual:   ${actual_store_dollars[store_id]:.2f}")
        passed = False
      else:
        print(f"✓ PASS: Store {store_id} = ${actual_store_dollars[store_id]:.2f}")

  # Test store item totals (should handle both items_count and items array)
  print("\n--- Store Item Totals (items_count OR len(items)) ---")
  actual_store_items = get_store_item_totals()
  expected_store_items = transactions_4_expected["store_items"]

  if actual_store_items is None:
    print("❌ FAIL: get_store_item_totals() returned None")
    passed = False
  else:
    for store_id, expected_count in expected_store_items.items():
      if store_id not in actual_store_items:
        print(f"❌ FAIL: Missing store {store_id}")
        passed = False
      elif actual_store_items[store_id] != expected_count:
        print(f"❌ FAIL: Store {store_id} items")
        print(f"   Expected: {expected_count}")
        print(f"   Actual:   {actual_store_items[store_id]}")
        passed = False
      else:
        print(f"✓ PASS: Store {store_id} = {actual_store_items[store_id]} items")

  # Test total items
  print("\n--- Total Items ---")
  actual_total = get_item_total()
  expected_total = transactions_4_expected["total_items"]

  if actual_total is None:
    print("❌ FAIL: get_item_total() returned None")
    passed = False
  elif actual_total != expected_total:
    print(f"❌ FAIL: Total items")
    print(f"   Expected: {expected_total}")
    print(f"   Actual:   {actual_total}")
    passed = False
  else:
    print(f"✓ PASS: Total items = {actual_total}")
  
  print("\n" + "=" * 60)
  if passed:
    print("✓ Stage 3 PASSED! Schema evolution handled correctly!")
    print("=" * 60)
    return True
  else:
    print("❌ Stage 3 FAILED")
    print("  Hints:")
    print("  - transactions3.json uses 'items' array instead of 'items_count'")
    print("  - transactions4.json adds 'tax' field (should be added to dollar totals)")
    print("=" * 60)
    return False


if __name__ == "__main__":
  success = test_stage3()
  sys.exit(0 if success else 1)

