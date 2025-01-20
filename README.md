Project: Responsive Webpage, Real-time Chat Application, and AWS Lambda Functions
This project showcases a combination of frontend development, a Django-based real-time chat application, and AWS Lambda functions. It is designed to demonstrate skills in responsive web design, backend development, WebSocket integration, and serverless computing.

1)Frontend Development
Responsive Webpage Features:

Fixed Navbar: Static top navigation bar remains visible during scrolling.

Layout: Includes a collapsible left menu, a main content area, and a right-side panel.

Footer: Fixed footer at the bottom of the page.

Adaptive Scaling: Dynamic page resizing based on screen width:
  992px to 1600px: Shrinks to 90%.
  
  700px to 767px: Shrinks to 80%.
  
  600px to 700px: Shrinks to 75%.
  
  ≤600px: Shrinks to 50%.

Running the Frontend:
  
  Open frontend/index.html in your browser.
  
  Ensure styles.css and script.js are in the same directory as index.html.

2)Django Chat Application
Features:

User Authentication: Sign-up and login functionality.

Collapsible User Menu: Displays all registered users for initiating chats.

Real-time Messaging: Powered by WebSockets with a saved chat history.

Database Integration: Stores user data and messages in a relational database.

Old Messages Retrieval: Automatically loads previous messages when initiating a chat.

Running the Application:

Navigate to the django folder.

Install dependencies:
pip install -r requirements.txt

Apply migrations:
python manage.py migrate

Start the server:
python manage.py runserver

Access the app at: http://127.0.0.1:8000.


3)AWS Lambda Functions
Features:

Addition Function:

Accepts two numbers as input.

Returns their sum.

File Upload Function:

Uploads documents or PDF files to an S3 bucket.

Deploying Lambda Functions:


Install and configure AWS CLI:
aws configure

Zip the Lambda function:
zip function.zip lambda_function.py


Deploy the Lambda function:

aws lambda create-function --function-name FunctionName \
    --runtime python3.x \
    --role arn:aws:iam::account-id:role/role-name \
    --handler lambda_function.lambda_handler \
    --zip-file fileb://function.zip

Frontend  Hosted on PythonAnywhere or AWS.
Accessible URL:https://krushna123a.pythonanywhere.com/static/

AWS Lambda Functions:
Deployed and accessible via AWS Console or CLI.
