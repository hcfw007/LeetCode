class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs = []
        digit_logs = []
        for log in logs:
            parts = log.split(" ", 1)
            if parts[1][0].isdigit():
                digit_logs.append(log)
            else:
                letter_logs.append(log)
        letter_logs.sort(key=lambda log: (log.split(" ", 1)[1], log.split(" ", 1)[0]))
        return letter_logs + digit_logs
