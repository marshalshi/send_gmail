'''
How to use:
  1. User your own gmail address and password in below `SendGmail` class.
  2. Use:
    >>> from send_gmail import SendGmail
    >>> sg = SendGmail()
    >>> sg.login()
    >>> sg.send(['<targetemail@example.com>',], 'title', 'message')
    >>> sg.logout()
  3. If you wanna send fancy email content, please check relevant document.
     https://docs.python.org/3/library/email-examples.html
'''
#!/usr/env/bin python
# -*- coding: utf-8 -*-

import smtplib

class SendGmail:

    from_email = ''
    password = ''

    host = 'smtp.gmail.com'
    port = 587

    msg_head = 'From: {from_email}\r\nTo: {to_emails}\r\nSubject:{subject}\r\n{message}'
    
    def __init__(self):
        self.server = smtplib.SMTP(self.host, self.port)
        self.server.ehlo()
        self.server.starttls()

    def login(self):
        self.server.login(self.from_email, self.password)

    def send(self, to_emails, subject, msg):
        '''
        Args:
           to_emails: list of email address.
           subject: just the email subject
           msg: just message
        '''
        msg = self.msg_head.format(
            from_email = self.from_email, to_emails = ','.join(to_emails),
            subject = subject, message = msg
        )

        self.server.sendmail(self.from_email, to_emails, msg)

    def logout(self):
        self.server.quit()
        
