# test_traffic_sim.py
import pytest
from traffic_control import add_traffic, clear_traffic
from unittest.mock import patch

# ------------------------
# Tests for add_traffic
# ------------------------

def test_add_traffic_non_negative():
    traffic = {'north': 5, 'east': 3, 'south': 0, 'west': 2}
    updated, new_added = add_traffic(traffic.copy())
    for count in updated.values():
        assert count >= 0
    for count in new_added.values():
        assert count >= 0

def test_add_traffic_keys_unchanged():
    traffic = {'north': 1, 'east': 2, 'south': 3, 'west': 4}
    updated, new_added = add_traffic(traffic.copy())
    assert set(updated.keys()) == set(traffic.keys())
    assert set(new_added.keys()) == set(traffic.keys())

def test_add_traffic_increases_or_same():
    traffic = {'north': 0, 'east': 0, 'south': 0, 'west': 0}
    updated, new_added = add_traffic(traffic.copy())
    for direction in traffic:
        assert updated[direction] >= traffic[direction]

def test_add_traffic_random_output_range():
    traffic = {'north': 0, 'east': 0, 'south': 0, 'west': 0}
    updated, new_added = add_traffic(traffic.copy())
    for val in new_added.values():
        assert 0 <= val <= 10  # Reasonable range for testing

# ------------------------
# Tests for clear_traffic
# ------------------------

def test_clear_traffic_does_not_go_negative():
    traffic = {'north': 3, 'east': 1, 'south': 0, 'west': 5}
    with patch('traffic_control.add_traffic', side_effect=lambda t: (t, {k:0 for k in t})):
        clear_traffic(traffic, cycles=1)
    for count in traffic.values():
        assert count >= 0

def test_clear_traffic_reduces_if_nonzero():
    traffic = {'north': 8, 'east': 4, 'south': 2, 'west': 6}
    before = traffic.copy()
    with patch('traffic_control.add_traffic', side_effect=lambda t: (t, {k:0 for k in t})):
        clear_traffic(traffic, cycles=1)
    for direction in traffic:
        if before[direction] > 0:
            assert traffic[direction] <= before[direction]

def test_clear_traffic_zero_stays_zero():
    traffic = {'north': 0, 'east': 0, 'south': 0, 'west': 0}
    with patch('traffic_control.add_traffic', side_effect=lambda t: (t, {k:0 for k in t})):
        clear_traffic(traffic, cycles=1)
    for count in traffic.values():
        assert count == 0

def test_clear_traffic_multiple_cycles():
    traffic = {'north': 10, 'east': 5, 'south': 3, 'west': 8}
    with patch('traffic_control.add_traffic', side_effect=lambda t: (t, {k:0 for k in t})):
        clear_traffic(traffic, cycles=3)
    for count in traffic.values():
        assert count >= 0
