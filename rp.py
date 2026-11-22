from dataclasses import dataclass 
from heapq import heappush, heappop 
from typing import List, Tuple 
  
  
def activity_selection(activities: List[Tuple[int, int, str]]): 
    """Greedy by earliest finishing time. Each activity is (start, finish, name).""" 
    chosen = [] 
    last_finish = float("-inf") 
    for start, finish, name in sorted(activities, key=lambda x: x[1]): 
        if start >= last_finish: 
            chosen.append((start, finish, name)) 
            last_finish = finish 
    return chosen 
  
  
def fractional_knapsack(items: List[Tuple[str, float, float]], capacity: float): 
    """Each item is (name, value, weight); items may be taken fractionally.""" 
    ranked = sorted(items, key=lambda x: x[1] / x[2], reverse=True) 
    chosen, total_value, remaining = [], 0.0, capacity 
    for name, value, weight in ranked: 
        if remaining <= 0: 
            break 
        fraction = min(1.0, remaining / weight) 
        chosen.append((name, fraction, value * fraction, weight * fraction)) 
        total_value += value * fraction 
        remaining -= weight * fraction 
    return chosen, total_value 
  
  
def job_sequencing(jobs: List[Tuple[str, int, int]]): 
    """Each job is (job_id, deadline, profit); each job takes one time slot.""" 
    jobs = sorted(jobs, key=lambda j: j[2], reverse=True) 
    max_deadline = max((deadline for _, deadline, _ in jobs), default=0) 
    slots = [None] * max_deadline 
    total_profit = 0 
    for job_id, deadline, profit in jobs: 
        for slot in range(min(deadline, max_deadline) - 1, -1, -1): 
            if slots[slot] is None: 
                slots[slot] = (job_id, profit) 
                total_profit += profit 
                break 
    return slots, total_profit 
  
  
def huffman_codes(frequencies): 
    """Return a mapping from symbol to prefix-free Huffman bit string.""" 
    if not frequencies: 
        return {} 
    heap, counter = [], 0 
    for symbol, freq in frequencies.items(): 
        heappush(heap, (freq, counter, {symbol: ""})) 
        counter += 1 
    if len(heap) == 1: 
        symbol = next(iter(frequencies)) 
        return {symbol: "0"} 
    while len(heap) > 1: 
        f1, _, left = heappop(heap) 
        f2, _, right = heappop(heap) 
        merged = {s: "0" + c for s, c in left.items()} 
        merged.update({s: "1" + c for s, c in right.items()}) 
        heappush(heap, (f1 + f2, counter, merged)) 
        counter += 1 
    return heap[0][2] 
  
  
def demo(): 
    activities = [(1, 3, "A"), (2, 5, "B"), (4, 7, "C"), 
                  (1, 8, "D"), (8, 10, "E"), (9, 11, "F")] 
    print("Activity Selection:", activity_selection(activities)) 
  
    items = [("Laptop", 60, 10), ("Router", 100, 20), ("Sensor", 120, 30)] 
    print("Fractional Knapsack:", fractional_knapsack(items, 50)) 
  
    jobs = [("J1", 2, 100), ("J2", 1, 19), ("J3", 2, 27), 
            ("J4", 1, 25), ("J5", 3, 15)] 
    print("Job Sequencing:", job_sequencing(jobs)) 
  
    frequencies = {"A": 5, "B": 9, "C": 12, "D": 13, "E": 16, "F": 45} 
    print("Huffman Codes:", huffman_codes(frequencies)) 
  
  
if __name__ == "__main__": 
    demo() 
