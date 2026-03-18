# qs7---exctract domain from email = "user1234@gmail.com",,,print gmail.com
# email = "user1234@gmail.com"
# indx = email.find("@")
# domain = email[indx+1:]
# print(domain)

# qs8----extract domain from sentence -- line = "from yash.raj@company.com Mon Jan 10",print- company.com
# line = "from yash.raj@company.com Mon Jan 10"
# indx1 = line.find("@")
# indx2 = line.find(" ",indx1)
# domain = line[indx1+1:indx2]
# print(domain)

#  

text = "X-DSPAM-Confidence:    0.8475"
indx = text.find("0")
number = text[indx:]
print(float(number))