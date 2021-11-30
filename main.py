
try:
    from typing import cast
    import requests
    import base64
except: 
    print("Missing Packages.Please installed the packages in requirements.txt and rerun the program")

try: 
    from credentials import email, token
except:
    answer = input("Do you wish to insert required Creds on Terminal? (y/ N)")
    if answer == 'y' or answer == 'Y':
        email = input("Please Enter the Email: ")
        token = input("Please Enter the Secured Token: (Found at URL-https://zccdatamaster.zendesk.com/agent/admin/api/settings)")
    else:
        print("Please create or copy the crendentials.py file. Include Account's email and token to access the tickets.")


class zendeskTicketTab:
    def __init__(self):
        # Set the request parameters
        url = 'https://zccdatamaster.zendesk.com/api/v2/tickets.json'

        # credentialAnswer = input()

        # Create the basic auth header
        auth = email + '/token:' + token
        auth = auth.encode("utf-8")
        auth = base64.b64encode(auth)
        auth = auth.decode("utf-8")
        headers = {'Authorization': 'Basic ' + auth}

        # Do the HTTP get request
        try:
            response = requests.get(url, headers=headers)
            print(f"Zendesk API Connected Successfully. Status: {response.status_code}")
        except:
            print("Unable to fetch the data. Please check the API and Credential details")


        # Check for HTTP codes other than 200
        if response.status_code != 200:
            print('Status:', response.status_code, 'Problem with the request. Exit.')
            exit()

        # Decode the JSON response into a dictionary and use the data
        data = response.json()

        print(f'Total Number of Tickets Assigned to you: {len(data["tickets"])}')

        self.ticketDetails = []
        ticketIDs = []

        for swi in range(len(data["tickets"])):
            temp = []
            temp.append(data["tickets"][swi]["id"])
            temp.append(data["tickets"][swi]["created_at"])
            temp.append(data["tickets"][swi]["type"])
            temp.append(data["tickets"][swi]["subject"])
            temp.append(data["tickets"][swi]["description"])
            temp.append(data["tickets"][swi]["priority"])
            temp.append(data["tickets"][swi]["status"])
            temp.append(data["tickets"][swi]["assignee_id"])
            self.ticketDetails.append(temp)
            ticketIDs.append(data["tickets"][swi]["id"])

    def displayTickets(self, currCount):


        if currCount + 25 < len(self.ticketDetails)-1:
            # print(self.ticketDetails[currCount: currCount+25],sep='\n')
            if len(self.ticketDetails) < 1:
                return
            for tic in self.ticketDetails[currCount: currCount+25]:
                print(tic)
                print('\n')
        elif len(self.ticketDetails[currCount:]) < 1:
            print("No More Tickets to Display")
        else:
            for tic in self.ticketDetails[currCount:]:
                print(tic)
                print('\n')

if __name__ == "__main__":
    
    if not email or not token:
        exit()

    showNextTickets = "y"
    

    while True:
        print("===================================================")
        print("      Welcome to Zendesk Ticket Viewer")
        print("===================================================")
        option = input("Select the Option: \n 1) Display All Tickets assigned to me \n 2) Display Ticket (ID Required) \n 3) Refresh Tickets \n 4) Exit \n Answer: ")

        if option == '1':
            obj = zendeskTicketTab()
            currCount = 0
            if currCount == 0:
                word = "first"
            else:
                word = "next"

            if obj.ticketDetails:
                # print(f"Displaying {word} 25 Tickets..")
                obj.displayTickets(currCount)
                currCount += 25

                while showNextTickets == 'y' or showNextTickets == 'Y' and currCount < len(obj.ticketDetails):
                    #if currCount > len(obj.ticketDetails):
                    showNextTickets = input(f"Display Next 25 Tickets: (y/N): ")
                    
                    if showNextTickets == 'y' or showNextTickets == 'Y' and currCount < len(obj.ticketDetails)-1:
                        obj.displayTickets(currCount)
                        currCount += 25
                    else:
                        break
            else:
                print("No Tickets Found. Please check the Account Name")

        elif option == '2':
            ticketID = input("Enter the Ticket ID: ")
            url = f'https://zccdatamaster.zendesk.com/api/v2/tickets/{ticketID}.json'

            # credentialAnswer = input()

            # Create the basic auth header
            auth = email + '/token:' + token
            auth = auth.encode("utf-8")
            auth = base64.b64encode(auth)
            auth = auth.decode("utf-8")
            headers = {'Authorization': 'Basic ' + auth}

            # Do the HTTP get request
            try:
                response = requests.get(url, headers=headers)
                data = (response.json())
                print("====================================")
                print("      Requested Ticket Details")
                print("====================================")
                print(f"Ticket ID: {data['ticket']['id']} \n\nCreated at: {data['ticket']['created_at']} \n\nSubject: {data['ticket']['subject']} \n\nDescription: {data['ticket']['description']} \n\nPriority: {data['ticket']['priority']}\n\nStatus: {data['ticket']['status']} \n\nAssignee ID: {data['ticket']['assignee_id']}\n\n")

            except:
                print("Unable to fetch the data. Please check the Ticket ID")

        elif option == '3':
            try:
                obj = zendeskTicketTab()
                print("Ticket List Refreshed Successfully")
            except:
                print("Ticket Fetch Operation Failed")

        elif option == '4':
            exit()

        else:
            print("Please Enter the Correct Choice")




        

