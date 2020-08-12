import argparse

import mailboxTools

valid_commands = ['quit', 'q', 'send_mail', 'get_mail', 'search_mail', 'delete_mail']

def command_is_valid(command):
    if command in valid_commands:
        return True

    else:
        print('Valid commands are {}'.format(valid_commands))
        return False

def main():
    mailbox_client = mailboxTools.mailboxClient(args.u, args.a, args.p)

    usr_input = ''
    command = ''

    while command != 'quit' and command != 'q':
        while not command_is_valid(usr_input):
            usr_input = input('Command: ')
            command = usr_input

        if command == 'send_mail':
            address = input('Destination address: ')
            address = address if address != '' else None

            subject = input('Message subject: ')
            subject = subject if subject != '' else None

            body = input('Message body: ')
            body = body if body != '' else None

            try:
                mailbox_client.send_mail(address, subject, body)

            except Exception as e:
                print(e)

        if command == 'get_mail':
            mailbox_client.get_mail()

        if command == 'search_mail':
            field = input('Search field (optional): ')
            field = field if field != '' else None

            text = input('Search text: ')
            text = text if text != '' else None

            mailbox_client.search_mail(field, text)

        if command == 'delete_mail':
            print('Please enter the ids you wish to delete')
            print("Enter 'done' when complete")
            ids = []
            delete_input = ''

            while delete_input != 'done':
                try:
                    delete_input = input('ID: ')

                    if delete_input == 'done':
                        break

                    ids.append(int(delete_input))

                except ValueError:
                    print("Please enter an integer or 'done' if complete")

            mailbox_client.delete_mail(ids)

        print('')
        usr_input = ''

    return 0

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='mailClient',
            description='Script to send and read emails')

    parser.add_argument('-a', metavar='ip_addr:port_num', required=True,
            help="Address of the server in the format ip_addr:port_num")

    parser.add_argument('-p', metavar='password', required=True,
            help="Password to access server")

    parser.add_argument('-u', metavar='username', required=True,
            help="Username to go by when sending emails")

    args = parser.parse_args()

    main()

