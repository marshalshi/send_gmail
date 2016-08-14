##### How to use:

1. User your own gmail address and password in below `SendGmail` class.
2. Use:
```
  >>> from send_gmail import SendGmail
  >>> sg = SendGmail()
  >>> sg.login()
  >>> sg.send(['<targetemail@example.com>',], 'title', 'message')
  >>> sg.logout()
```
3. If you wanna send fancy email content, please check relevant document.  
https://docs.python.org/3/library/email-examples.html
