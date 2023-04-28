from locust import HttpUser, TaskSet, task, between


class MyLocust(HttpUser):
    # Define the wait time between requests to be between 10 and 5000 milliseconds
    wait_time = between(10, 5000)

    # Call the login function at the start of the test
    def on_Start(self):
        self.login()

    # Define the login task
    @task
    def login(self):
        # Send a GET request to the root URL to retrieve the CSRF token cookie
        response = self.client.get('/')
        # Extract the CSRF token from the cookie
        csrftoken = response.cookies['csrftoken']
        # Send a POST request with the login credentials and CSRF token
        response = self.client.post("/", {"username": "admin@gmail.com", "password": "admin"}, headers={"X-CSRFToken": csrftoken})
        # Return the response object
        return response

    # Define the logout task
    @task
    def logout(self):
        # Send a GET request to the logout URL
        response = self.client.get('/logout')
        # Return the response object
        return response

    # Define the admin page task
    @task
    def adminpage(self):
        # Call the login function to authenticate
        self.login()
        # Send a GET request to the admin page URL
        response = self.client.get('/admin_page')
        # Return the response object
        return response

    # Define the leave status rejected task
    @task
    def leave_status_rejected(self):
        # Call the login function to authenticate
        self.login()
        # Send a GET request to the leave status rejected URL
        response=self.client.get('/leave_status_rejected')
        # Return the response object
        return response

    # Define the leave status approved task
    @task
    def leave_status_approved(self):
        # Call the login function to authenticate
        self.login()
        # Send a GET request to the leave status approved URL
        response=self.client.get('/leave_status_approved')
        # Return the response object
        return response
    
    # Define the leave status pending task
    @task
    def leave_status_pending(self):
        # Call the login function to authenticate
        self.login()
        # Send a GET request to the leave status pending URL
        response=self.client.get('/leave_status_pending')
        # Return the response object
        return response

