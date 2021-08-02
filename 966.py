# 966	Vowel Spellchecker

class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        answers = []
        
        words_exact = set(wordlist)
        dw = dict()
        dv = dict()
        for i in range(len(wordlist) -1, -1, -1):
            wlow = wordlist[i].lower()
            dw[wlow] = i
            wlow = re.sub('[aeiou]', '_', wlow)
            dv[wlow] = i
        
        for qw in queries:
            if qw in words_exact:
                answers.append(qw)
            else:
                qw = qw.lower()                
                if qw in dw:
                    dex = dw[qw]
                    answers.append(wordlist[dex])
                else:
                    qw = re.sub('[aeiou]', '_', qw)
                    if qw in dv:
                        dex = dv[qw]
                        answers.append(wordlist[dex])
                    else:
                        answers.append("")

        return answers
