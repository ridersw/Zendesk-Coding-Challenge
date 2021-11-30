# Zendesk-Coding-Challenge

**Language Used: Python<br>**
**Requirements: requirements.txt<br>**
**UI: CLI Based**

**Steps to Run the program**

1. Please Install the packages in requirements.txt and Python version.
2. Create credentials.py in root folder and insert email and token for an account to login and run the program to fetch and display the tickets successfully OR inser the credentials on the terminal on runtime.
3. Run the main.py by command "python3 main.py"

# On Branch main- CLI Based UI

### 1) Connect to Zendesk API

#### CLI Snapshot of Zendesk API Connection Status-

![CLI Snapshot of Zendesk API Connection Status](<images/(1)ZendeskAPIConnected.jpg>)

#### Snapshot of Zendesk API Connection POSTMAN-

![Snapshot of Zendesk API Connection POSTMAN](<images/(1)ZendeskAPIPostman.jpg>)

### 2) Request all the tickets for your account

![Request all the tickets for your account](<images/(2)ZendeskDisplayAllTickets.jpg>)

### 3) Display them in a list

![Display them in a List](<images/(3)DisplayTicketsinaList.jpg>)

### 4) Display individual ticket details

![Display individual ticket details](<images/(4)Displayindividualticketdetails.jpg>)

### 5) Page through tickets when more than 25 are returned

![Page through tickets when more than 25 are returned](<images/(5)Pagination.jpg>)
![Page through tickets when more than 25 are returned](<images/(5)Pagination(1).jpg>)

## Error Handling Scenarios

1. Required Packages not available
2. Credentials (email and token) is not available.
3. API requests fails
4. API response error
5. Specific ticket fetch fails
