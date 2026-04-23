class BowlingGame:
    def __init__(self):
        self.throw_list = []

    def is_valid_roll(self, pins):
        throws = self.throw_list

        if len(throws) == 0:
            return True

        i = 0
        frame = 0

        while frame < 9 and i < len(throws):
            if throws[i] == 10:
                i += 1
            else:
                i += 2
            frame += 1

        if i < len(throws):
            first = throws[i]
            if first != 10 and first + pins > 10:
                return False

        return True

    def calculate_live_scores(self):
        scores = []
        total = 0
        i = 0

        for _ in range(10):
            if i >= len(self.throw_list):
                break

            if self.throw_list[i] == 10:
                if i + 2 >= len(self.throw_list):
                    break
                total += 10 + self.throw_list[i+1] + self.throw_list[i+2]
                scores.append(total)
                i += 1
            else:
                if i + 1 >= len(self.throw_list):
                    break

                if self.throw_list[i] + self.throw_list[i+1] == 10:
                    if i + 2 >= len(self.throw_list):
                        break
                    total += 10 + self.throw_list[i+2]
                else:
                    total += self.throw_list[i] + self.throw_list[i+1]

                scores.append(total)
                i += 2

        return scores

    def get_display_data(self):
        display_frames = []
        i = 0

        for frame in range(10):
            if i >= len(self.throw_list):
                display_frames.append([])
                continue

            if frame == 9:
                shots = []
                while i < len(self.throw_list):
                    val = self.throw_list[i]

                    if val == 10:
                        shots.append("X")
                    elif len(shots) > 0 and shots[-1].isdigit() and int(shots[-1]) + val == 10:
                        shots.append("/")
                    else:
                        shots.append("-" if val == 0 else str(val))

                    i += 1

                display_frames.append(shots)

            else:
                if self.throw_list[i] == 10:
                    display_frames.append([" ", "X"])
                    i += 1

                elif i + 1 < len(self.throw_list):
                    f, s = self.throw_list[i], self.throw_list[i+1]

                    s1 = "-" if f == 0 else str(f)
                    s2 = "/" if f + s == 10 else ("-" if s == 0 else str(s))

                    display_frames.append([s1, s2])
                    i += 2

                else:
                    display_frames.append(
                        ["-" if self.throw_list[i] == 0 else str(self.throw_list[i])]
                    )
                    i += 1

        return display_frames

    def is_game_over(self):
        return len(self.calculate_live_scores()) == 10

