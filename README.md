# :briefcase: CSCI 656 Final Project - JobJump
JobJump is a Django CRUD application that helps track and document job applications. JobJump utilizes a Postgres database hosted on Heroku for persistent data with a Python Django backend and a simple HTML and SASS frontend with bootstrap. This application is deployed and hosted on AWS Elastic Beanstalk. JQuery AJAX is used to update the HTML DOM seamlessly with database changes or responses received from AWS lambda.

# :clipboard: Project Requirements
## :white_check_mark: A web app with purpose - something I would use
Applying to many jobs can become overwhelming and one can quickly lose track. Having one spot to track them and view the overall data is very benefical. Additionally, being able to identify which job links have been removed helps identify positions that are no longer available and thus no further work should be exerted on the application.
## :white_check_mark: Should be deployed on Elastic Beanstalk
The application was succesfully deployed to AWS Elastic Beanstalk. Permissions for the IAM instance profile were updated to allow for calling the AWS Lambda function from within Elastic Beanstalk through Boto3 without any additional credentials needed.
## :white_check_mark: Connected to a PostgreSQL database
A Heroku Postgres database was deployed and connected to the JobJump application successfully.
## :white_check_mark: Atleast 5 tables should be used within models.py with atleast 2 one-to-many relationships
5 tables were defined within models.py: Company, CompanyReviews, Job, JobApp, and Event. Additionally the built-in auth_user table was used for authentication. Two one-to-many relationships are:

- Job and Company: A Job can only have one Company but a Company can have many Jobs
- Event and JobApp: An Event can only be linked to one JobApp but a JobApp can have many linked Events

## :white_check_mark: Atleast 1 Lambda function should be used that is called using Boto3 within Django
A lambda function is utilized to quickly query a list of URLs and return whether or not the URL is still valid. This is executed using Boto3 to invoke the lambda function which returns a json body that is transferred to the frontend to display the appropriate color (GREEN==Healthy, RED== Not Healthy) next to the URL.

## :white_check_mark: AJAX should be utilized for communication from the front-end to the back-end
AJAX is used to discreetly update HTML DOM elements on the front-end based on database updates, user interactions, or lambda invocations and responses.

## :white_check_mark: Unit tests should be implemented using Pytest
Pytest is used for several unit tests checking the navigation URL responses and the restriction of the myjobs page from users who are not authenticated.
