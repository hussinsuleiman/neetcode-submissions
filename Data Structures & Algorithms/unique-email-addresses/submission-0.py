class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        mails = set()

        for mail in emails:
            new = []
            i = 0

            while mail[i] != '@':
                if mail[i] == '.':
                    i += 1
                    continue
                
                if mail[i] == '+':
                    while mail[i] != '@':
                        i += 1
                    i += 1
                    break
                
                new.append(mail[i])
                i += 1
            
            while i < len(mail):
                new.append(mail[i])
                i += 1

            mails.add(''.join(new))
        
        return len(mails)