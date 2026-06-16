from collections import Counter

from .parser import parse_line


class LogAnalyzer:

    def __init__(self):

        self.total_lines = 0
        self.levels = Counter()
        self.ips = Counter()
        self.errors = Counter()


    def process_line(self, line):

        self.total_lines += 1

        data = parse_line(line)


        if data["level"]:
            self.levels[data["level"]] += 1


        if data["ip"]:
            self.ips[data["ip"]] += 1


        if data["level"] in [
            "ERROR",
            "CRITICAL"
        ]:
            self.errors[
                data["message"]
            ] += 1



    def analyze(self, filepath):

        with open(
            filepath,
            "r",
            encoding="utf-8",
            errors="ignore"
        ) as file:

            for line in file:
                self.process_line(line)



    def get_summary(self):

        return {

            "total_lines":
                self.total_lines,

            "levels":
                dict(self.levels),

            "top_ips":
                self.ips.most_common(10),

            "top_errors":
                self.errors.most_common(10)
        }