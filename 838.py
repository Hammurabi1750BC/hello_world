# 838. Push Dominoes

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        prev_right = dot_span_left = None
        final_dominoes = []

        for i, d in enumerate(dominoes):
            final_dominoes.append(d)
            if d == '.':
                if dot_span_left == None:
                    dot_span_left = i
            elif d == 'L':
                if dot_span_left != None:
                    span = i - dot_span_left
                    if prev_right != None:
                        falls = span // 2
                        if falls > 0:
                            final_dominoes[dot_span_left:dot_span_left + falls] = 'R' * falls
                            final_dominoes[i - falls:i] = 'L' * falls
                    else:
                        final_dominoes[dot_span_left:i] = 'L' * span
                dot_span_left = None
                prev_right = None
            else:  # R
                if dot_span_left != None and prev_right != None:
                    span = i - dot_span_left
                    final_dominoes[dot_span_left:i] = 'R' * span
                dot_span_left = None
                prev_right = i

        # if prev r, then r to end
        if prev_right != None and dot_span_left != None:
            span = i - dot_span_left + 1  # no L at position i so + 1
            final_dominoes[dot_span_left:] = 'R' * span

        return ''.join(final_dominoes)
