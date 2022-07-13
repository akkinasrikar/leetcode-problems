class Solution(object):
    def numUniqueEmails(self, emails):
        mails=map(self.Mail_ID,emails)
        return len(set(mails))
    def Mail_ID(self,mail):
        at_rate_index=mail.index("@")
        lc=mail[:at_rate_index]
        dn=mail[at_rate_index+1:]
        if "+" in lc:
            plus_index=lc.index("+")
            name=lc[:plus_index]
        else:
            name=lc
        return name.translate({ord("."):None})+"@"+dn
            
        