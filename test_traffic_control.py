from traffic_control import pick_signal
from traffic_control import calculate_waiting_time
import pytest



# function 1

def test_pick_signal_zero():
    traffic = {'north':0, 'east':0, 'west':0, 'south':0}
    assert pick_signal(traffic) == "none"

def test_pick_signal_normal():
    traffic = {'north':1, 'east':2, 'west':3, 'south':4}
    assert pick_signal(traffic) == "south"
    
def test_pick_signal_same():
    traffic = {'north':1, 'east':1, 'west':1, 'south':1}
    assert pick_signal(traffic) == "north"

def test_pick_signal_one_lane():
    traffic = {'north': 0, 'east': 0, 'west': 0, 'south': 7}
    assert pick_signal(traffic) == "south"


#function 2

def test_calculate_waiting_time_reduce():
    traffic = {"north": 9, "east": 9, "west": 8, "south": 8}
    updated, cleared = calculate_waiting_time(traffic.copy(), "north", 5)
    assert updated["north"] == 4
    assert cleared == 5

def test_calculate_waiting_time_clear():
    traffic = {"north": 3, "east": 9, "west": 8, "south": 8}
    updated, cleared = calculate_waiting_time(traffic.copy(), "north", 5)
    assert updated["north"] == 0
    assert cleared == 3

def test_calculate_waiting_time_zero_lane():
    traffic = {"north": 0, "east": 9, "west": 8, "south": 8}
    updated, cleared = calculate_waiting_time(traffic.copy(), "north", 5)
    assert updated["north"] == 0
    assert cleared == 0

def test_calculate_waiting_time_excess_green():
    traffic = {"north": 2, "east": 9, "west": 8, "south": 8}
    updated, cleared = calculate_waiting_time(traffic.copy(), "north", 10)
    assert updated["north"] == 0
    assert cleared == 2
