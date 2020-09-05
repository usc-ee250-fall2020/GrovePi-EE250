from pprint import pprint

import json
import requests

class mailboxClient():
    def __init__(self, username, serv_addr, serv_password):
        """
        Summary: Class that manages the HTTP interactions with a mailboxServer

        Args:
            username (string): Username that will identify the client for current session
            serv_addr (string): Target mailbox server to connect to in format ip_addr:port
            serv_password (string): Target mailbox server's password
        """
        self.serv_addr = serv_addr
        self.serv_pw = serv_password
        self.username = username

    def send_mail(self, address, subject, body):
        """
        Summary: Sends a POST message to the server to add mail

        Args:
            address (string): Target mailbox server to send mail to in format ip_addr:port
            subject (string): Message subject
            body (string): Message body
        """

        # This header sets the HTTP request's mimetype to `application/json`.
        # This means the payload of the HTTP message will be formatted as a
        # JSON object
        headers = {
            'Content-Type': 'application/json',
            'Authorization': None   # not using HTTP secure
        }

        # The payload of our message starts as a simple dictionary. Before sending
        # the HTTP message, we will format this into a JSON object
        payload = {
            'subject': subject,
            'body': body,
            'sender': self.username
        }

        # Send an HTTP POST message and block until a response is given.
        # Note: requests is NOT the same thing as the request from the Flask
        # library.
        response = requests.post("http://{}/send-mail".format(address),
                                 headers=headers,
                                 data=json.dumps(payload))

        # Print the JSON object from the HTTP response in a pretty format
        pprint(response.json())

    def get_mail(self):
        """
        Summary: Sends a GET request to server for all mail
        """

        params = {
            'password': self.serv_pw,
        }

        # Since we are not using JSON format for our payload, we do not have to use the headers and
        # data fields of requests.get()
        response = requests.get("http://{}/mailbox".format(self.serv_addr),
                                params=params)
        pprint(response.json())

    def search_mail(self, field, text):
        """
        Summary: Sends a GET request to server for mail matching search parameters

        Args:
            field (string): One of the fields of the email (body, subject, sender, etc)
            text (string): Description
        """
        if field != None:
            params = {
                'password': self.serv_pw,
                'field': field,
                'text': text,
            }
            response = requests.get("http://{}/mailbox/search"
                                    .format(self.serv_addr), params=params)

        else:
            params = {
                'password': self.serv_pw,
                'text': text,
            }
            response = requests.get("http://{}/mailbox/search"
                                    .format(self.serv_addr), params=params)

        if response.status_code == 200:
            pprint(response.json())

        else:
            print('\n' + response.text)

    def delete_mail(self, mail_ids):
        """
        Summary: Sends a DELETE message to the server to remove mail with certain ids

        Args:
            mail_ids (list): list of integers corresponding to the ids of the mail to delete
        """
        headers = {
            'Content-Type': 'application/json',
            'Authorization': None #not using HTTP secure
        }
        payload = {
            'password': self.serv_pw,
            'mail_ids': mail_ids
        }
        response = requests.delete("http://{}/mailbox/delete".format(self.serv_addr),
                        headers=headers, data=json.dumps(payload))

        pprint(response.json())

