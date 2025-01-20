Responsive Webpage, Chat Application, and AWS Lambda Functions
This project includes three key components:

Frontend Development: A responsive webpage with collapsible menus and adaptive scaling.
Django Chat Application: A real-time chat app with WebSocket integration.
AWS Lambda Functions: Serverless functions for mathematical operations and file storage.
Frontend
Features
Fixed Navbar: A static top navigation bar.
Responsive Layout: Includes a collapsible left menu, main content area, and right-side panel.
Adaptive Scaling: Page width adjusts based on screen size:
992px to 1600px: Shrinks to 90%.
700px to 767px: Shrinks to 80%.
600px to 700px: Shrinks to 75%.
≤600px: Shrinks to 50%.
Running the Frontend
Open the frontend/index.html file in your browser.
Ensure the styles.css and script.js are in the same directory as the HTML file.
Django Chat Application
Features
User Authentication: Sign-up and login functionality.
Collapsible User Menu: Displays all registered users for easy chat initiation.
Real-time Messaging: WebSocket-based messaging with saved chat history.
Database Integration: Stores user data and messages in a database.
Old Messages: Automatically loads previous messages when a chat is initiated.
Running the Application
Navigate to the django folder.
Install dependencies:
bash
Copy
Edit
pip install -r requirements.txt
Apply migrations:
bash
Copy
Edit
python manage.py migrate
Start the server:
bash
Copy
Edit
python manage.py runserver
Access the app at http://127.0.0.1:8000.
AWS Lambda Functions
Features
Addition Function: Accepts two numbers as input and returns the sum.
File Upload: Uploads documents or PDFs to an S3 bucket.
Deploying Lambda Functions
Install the AWS CLI and configure it with your credentials:
bash
Copy
Edit
aws configure
Zip the Lambda function and deploy it:
bash
Copy
Edit
zip function.zip lambda_function.py
aws lambda create-function --function-name FunctionName \
    --runtime python3.x \
    --role arn:aws:iam::account-id:role/role-name \
    --handler lambda_function.lambda_handler \
    --zip-file fileb://function.zip
Update or test the functions using AWS CLI or the AWS Console.
Folder Structure
bash
Copy
Edit
north90/
├── django/                 # Backend Django application
│   ├── manage.py
│   ├── db.sqlite3          # SQLite Database
│   ├── myapp/              # Django app for chat
│   └── ...
├── frontend/               # Frontend files
│   ├── index.html
│   ├── styles.css
│   ├── script.js
├── was_lambda/             # AWS Lambda functions
│   ├── addition_function.py
│   ├── upload_to_s3.py
└── README.md
Project Deployment
The Django app is hosted at: 
AWS Lambda functions are deployed and can be invoked via the AWS Console or CLI.
Contributors
Krushna Dandge
