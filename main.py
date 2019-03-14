#:last modified 03/03/2019 19:21PM
#Author:marktrevis
#date:27/02/2019
#email:marktrevis61@gmail.com
#facebook:markenzie trevis

   #email me any bugs in the program

#Server_side :onnet text message  encrypted chat program, each message sent and recieved is encrypted by a specific key..when started ,connection is began and  after connection, akey is created to be used for encryption . a key is created by the server side after creation its sent to the client with an encrypted messge ,on recieve the client uses the key to decrypt the message and the same key is used to encrypt the mssage sent from the client to the server and on recieve of the messge to the server, the server decrypts it, and then creates another key for another conversation . the process goes on and on infinite with difference in messages encrypted. an  encrypted 'hi' for a specified key is different from the other encrypted 'hi' with another key. key changes after a send and recieve process is done at one time . so every message even a '.' is encrypted with a specific key .

#process on server

    #create key
     #send key to client
      #send messege'encrypted with key '
       #recieve message from client
       
        # create new key
        
from socket import *
from random import randint,choice
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64
from time import sleep
from termcolor import colored

print(colored("""
	::###############################::
	¦¦  @server+side                 ¦¦
	¦¦         ::#### erver          ¦¦
	¦¦          #                    ¦¦
	¦¦          ####                 ¦¦
	¦¦              #                ¦¦
	¦¦         ####::ide             ¦¦
	¦¦                               ¦¦
	¦¦  @-send messages anonymously  ¦¦
	¦¦  Author:marktrevis            ¦¦
	¦¦  Email:marktrevis61@gmail.com ¦¦
	¦¦                               ¦¦
	::###############################::
	

""",'blue'))


class serv:
  def __init__(self) :
     
     
     
     self.client = []
     self.client1 = []
     self.server = []
     self.nam = []
     self.clnt=[]
     self.buff = 800
  
  def  loader(self):
    i = 0
    j = ""
    k = '⬇'
    for p in range(10):
      i = i+10
      for v in range(1):
        j = k+j
      import time 
      time.sleep(0.5)
      print(str(i)+'%'+j)  
               
                        
                                          
  def client_run(self):#client side 
   sck = socket(AF_INET,SOCK_STREAM)#opening tcp sockets on ip version4
   inp = input("Enter user id:")
   self.client1.append(inp)
   sleep(5)
   print("client connection started to server\n")
   ip = input("enter IP address:")
   port = input("enter port number:")
   sck.connect((ip,int(port) ))
   num = self.client1[0]#the item in list self.server in position 0
   sck.send(num.encode())#sending client name to server 
   op = sck.recv(self.buff).decode()#recieve server user name to client
   self.clnt.append(op)
   print("Authenticating....  to ",ip,"name:",self.clnt[0])
   sleep(1)
   
   print("starting getting keycodes.. \n")
   sleep(3)
   print("Authenticated, connection successful...")
   sleep(2)
   print(colored("waiting for message","blue"))
   while True:
    kv = []
    fd = []
    renc = sck.recv(self.buff)
    kv.append(renc) 
    ky = colored("...keys:",'red') 
    pauth = kv[0]
    salt = b'salt_' 
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend())
    key = base64.urlsafe_b64encode(kdf.derive(pauth) )
    fd.append(key)
    recvm = sck.recv(self.buff)#recieve sent message 
    k = Fernet(fd[0])
    fdck = k.decrypt(recvm)# decrypt received  messgae
    cld = colored('recieved:','red')#colored message
    print(cld,fdck.decode(),'\n')#print ouy the recieved message decodeded 
    inpi = input("Enter message:")
    text = inpi.encode()#encode input  because the encryption function encrypts bytes data
    enc = k.encrypt(text)#encrypt the text , the input
    sck.send(enc)#send encrypted message
    print(colored("message sent",'yellow'))
    

  def server_run(self):#server_side function
   inp = input("Enter Name:")
   self.server.append(inp)#saving the input to list self.server
   sleep(3)
   print("starting server.........")
   sck = socket(AF_INET,SOCK_STREAM)
   sck.bind(("",1026)) #binding ip address to port number 1025 ,the port number can be changed 
   sck.listen(5)
   c,a = sck.accept()#accepting incoming connections
   nu = c.recv(self.buff).decode()#reciving the name of the client 
   self.client.append(nu)#appending/saving the name to list self.client
   c.send(self.server[0].encode())#sending the server name to client in list server in position 0
   print(colored("recieved client authentication",'green'))#print out on recieve of client id/name
   sleep(3)#pausing for 3secs
   
   print("client {} connected...".format(a[0]))#print thaf client of an ip that is represented as list a[0] is connected 
   print("Authenticated to {}".format(a[0]),'name:',self.client[0])
   print("creating key pairs")
   self.loader()
   while True:
    vn = []
    jh = []
    p = []
    l = "abcdefghijklmnopqrstuvwxyz1234567890"
    for i in range(randint(4,16)):
     kl = choice(l)#creating a random key from a list of letters 'l'
     p.append(kl)
    en ="".join(p)
    j = str("".join(p))
    kd = "['']"
    for o in kd:
     kt = j.replace(o,"")
    jh.append(kt)#save key to list kt
    c.send(jh[0].encode())#send key to client
    ky = colored("keys:",'red')
    print(ky,jh[0])
    inh = input("Enter message:")#message entry
    text = inh.encode()#encode message to bytes
    pauth = jh[0].encode() 
    salt = b'salt_' 
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend())
    key = base64.urlsafe_b64encode(kdf.derive(pauth) )#key creation,hashed key
    vn.append(key)
    k = Fernet(vn[0])
    enc = k.encrypt(text)#encrypt message
    c.send(enc)#send message
    print(colored("message sent",'yellow'))#notify message sent
    recvm = c.recv(self.buff)#receive message from connected client
    fdbck = k.decrypt(recvm)#decryt the sent message
    cld = colored('received:','red')#colored text before message
    print(cld,fdbck.decode(),'\n')#print sent message decoded to utf-8 
    
  
  def enc_run(self):
   inp = input("Enter 1-server /2-client::")
   if inp == '1':
    sleep(1)
    print("Running as server..\n")
    sleep(2)
    self.server_run()
   elif inp =='2':
    print("Started as client\n")
    sleep(2)
    self.client_run()
   else:
    print("time out.... wrong input")
    import sys
    sys.exit()
     
if __name__=="__main__":
  serv().enc_run()  
