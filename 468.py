# 468	Validate IP Address
class Solution:
    def validIPAddress(self, IP: str) -> str:
        def ipv4(IP):
            IP = IP.split('.')
            for i in range(4):
                if not 1 <= len(IP[i]) <= 3:
                    return False
                for digit in IP[i]:
                    if not digit.isdigit():
                        return False

                if len(IP[i]) > 1 and (IP[i][0] == '0' or int(IP[i]) > 255):
                    return False

            return True

        def ipv6(IP):
            IP = IP.split(':')
            for i in range(8):
                if not 1 <= len(IP[i]) <= 4:
                    return False
                for char in IP[i]:
                    if not char.isdigit() and char.lower() not in 'abcdef':
                        return False

            return True

        if IP.count('.') == 3 and ipv4(IP):
            return 'IPv4'

        elif IP.count(':') == 7 and ipv6(IP):
            return 'IPv6'

        return 'Neither'
