from PythonSendEmail import SendEmail

email = SendEmail("sender@email.com", "receiver1@email.com, receiver2@email.com")
email.setCCRecipient("cc1@email.com, cc2@email.com")
email.Login("Your password")
email.SetEmailSubject("Your Subject")
email.SetEmailMessage("Your Message")
email.toDraft()
email.Send()
