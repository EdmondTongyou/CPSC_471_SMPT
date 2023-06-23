from socket import *
import ssl
import base64

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"
# Choose a mail server (e.g. Google mail server) and call it mailserver

# Using smpt.gmail.com server, configurations include port 25, 465, and 587
mailserver = "smtp.gmail.com"
port = 587
email = 'sample@gmail.com'
password = 'password'
# Create socket called clientSocket and establish a TCP connection with mailserver

#Fill in start
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver, port))
#Fill in end

recv = clientSocket.recv(1024).decode()

print(recv)

if recv[:3] != '220':

    print('220 reply not received from server.')

# Send HELO command and print server response.

heloCommand = 'HELO Alice\r\n'

clientSocket.send(heloCommand.encode())

recv1 = clientSocket.recv(1024).decode()

print(recv1)

if recv1[:3] != '250':

    print('250 reply not received from server.')

# Adding TLS layer
tls_command = 'STARTTLS\r\n'
clientSocket.send(tls_command.encode())
recv2 = clientSocket.recv(1024).decode()
print(recv2)

context = ssl.create_default_context()
clientSocket = context.wrap_socket(clientSocket, server_hostname=mailserver)

# Email and password that will be used for authentication and that is needed to send the email using SMTP
# The server expects a base64-encoded username and password
email = base64.b64encode(
    email.encode()) + '\r\n'.encode()
password = base64.b64encode(password.encode()) + '\r\n'.encode()

# Authentication of account
auth_command = 'AUTH LOGIN \r\n'
clientSocket.send(auth_command.encode())
recv3 = clientSocket.recv(1024).decode()
print(recv3)

clientSocket.send(email)
recv4 = clientSocket.recv(1024).decode()
print(recv4)

clientSocket.send(password)
recv5 = clientSocket.recv(1024).decode()
print(recv5)

# Send MAIL FROM command and print server response.

# Fill in start
mailFrom = 'MAIL FROM: <sample@gmail.com>\r\n'
clientSocket.send(mailFrom.encode())
recv6 = clientSocket.recv(1024).decode()
print(recv6)
# Fill in end
# Send RCPT TO command and print server response.

# Fill in start
rcptTo = 'RCPT TO: <sample@gmail.com>\r\n'
clientSocket.send(rcptTo.encode())
recv7 = clientSocket.recv(1024).decode()
print(recv7)
# Fill in end
# Send DATA command and print server response.

# Fill in start
data_command = 'DATA\r\n'
clientSocket.send(data_command.encode())
recv8 = clientSocket.recv(1024).decode()
print(recv8)
# Fill in end
# Send message data.

# Fill in start
clientSocket.send(msg.encode())
# Fill in end
# Message ends with a single period.

# Fill in start
clientSocket.send(endmsg.encode())
recv10 = clientSocket.recv(1024).decode()
print(recv10)
# Fill in end
# Send QUIT command and get server response.

# Fill in start
quit_command = 'QUIT\r\n'
clientSocket.send(quit_command.encode())
recv11 = clientSocket.recv(1024).decode()
print(recv11)

clientSocket.close()
# Fill in end
