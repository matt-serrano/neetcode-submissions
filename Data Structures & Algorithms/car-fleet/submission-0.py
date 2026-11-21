class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p, s] for p, s in zip(position, speed)]

        stack = []
        for p, s in sorted(pair)[::-1]: # reverse sorted order
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)

'''
LeetCode 853, Car Fleet, gives me a target distance, a list of starting positions, and a list of speeds, and I return the number of car fleets that arrive at the target. It's a single lane and cars can't pass, so a faster car that catches up to a slower one has to slow down and travel with it as one fleet. First I zip positions and speeds into a list of pairs, since the two lists have the same length. Then I sort the pairs by position in descending order so I process the car closest to the target first. For each car I compute its arrival time as (target - position) / speed and push it onto a stack, where each entry represents a fleet's arrival time. If the stack has at least two entries and the new car's time is less than or equal to the time of the car ahead of it, it would catch up before the target, so it merges into that fleet and I pop it off. If its time is greater, it arrives later on its own, so it stays as a new fleet. After going through every car, the stack size is the number of fleets. This runs in O(n log n) time because of the sort, with O(n) space.
'''