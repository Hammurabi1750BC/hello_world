# 1169	Invalid Transactions
class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        poss_invalid = set()

        d_trans = defaultdict(list)

        for i in range(len(transactions)):
            name, time, amount, city = transactions[i].split(',')
            d_trans[name].append([int(time), city, i])
            if int(amount) > 1000:
                poss_invalid.add(i)

        for name in d_trans.keys():
            trans_list = sorted(d_trans[name])
            for left in range(len(trans_list)-1):
                right = left + 1
                left_time = trans_list[left][0]
                found_inval = False
                while right < len(trans_list) and trans_list[right][0] <= left_time + 60:
                    if trans_list[right][1] != trans_list[left][1]:
                        found_inval = True
                        poss_invalid.add(trans_list[right][2])
                    right += 1
                if found_inval:
                    poss_invalid.add(trans_list[left][2])

        invalid_list = [transactions[i] for i in poss_invalid]

        return invalid_list
