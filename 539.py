# 539. Minimum Time Difference
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minutes = []
        for time in timePoints:
            minute_sum = int(time[:2]) * 60 + int(time[3:])
            if minute_sum in minutes:
                return 0
            minutes.append(minute_sum)

        minutes.sort()

        min_delta = (24 * 60) - minutes[-1] + minutes[0]  # wraparound
        for i in range(1, len(minutes)):
            min_delta = min(min_delta, minutes[i] - minutes[i - 1])

        return min_delta
