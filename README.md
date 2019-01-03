# HeavyWater
HeavyWater Machine Learning Problem





An algorithmic approach for Document classification model.






Approached this Problem with Random Forest, SVM, Naive Bayes, LogisticRegression Classifiers and found out RFC to be the best Classifier.






Then used Random Classification Model with Best Paramaters, resulting in 87% effeciency.




# Steps to create EC2 Instance

## Step 1 - Setting up an account on AWS
Sign up on [Amazon Web Services](https://aws.amazon.com/free/)

![
](https://lh3.googleusercontent.com/zu53EKRKnBcgCfu3GHWgjxbEXzJXTaClSWBR8WySrdbzZyp0sr8BS_COaYzU92tHq3o-l5DTXP76 "EC2 CONSOLE")

## Step 2 - Creating an EC2 instance
This step consists of the following steps :-
-   Select the  **EC2 option**  under the  **Compute**  section.
-  Select the  **Launch Instance**  option under the  **Create Instance**  section.
-  Select Ubuntu
-  Select Free Tier t2 micro
-  Configure Instance Details
-  Add Storage if you need it
-  Launch your instance
-  Create a key pair and make sure to save it somewhere safe. You won’t be able to replace it.
-  Now Finally launch the instance!
- 
![enter image description here](https://lh3.googleusercontent.com/5AMjNNFb1sDLJukIUreqUuw1GH48oQDHnriyOa9-SkRLqsiXZd6In_42kZoxsE2xS6qA7CHiAQ3u "Instance Launched")

# Steps to Deploy the flask Application

## Step 1 - Connect to your EC2 instance
- Open a terminal session in the directory where you have saved the key pair. 
- Set permissions on the file.
> **Command:** 
>  $ sudo chown -v user keyValuePair.pem
>  $ chmod 400 keyValuePair.pem
>  $ ssh -i keyValuePair.pem ubuntu@ec2-18-218-201-44.us-east-2.compute.amazonaws.com
![enter image description here](https://lh3.googleusercontent.com/z_AChTYSIcdCaRKAz8dXfHUq0dF_gWjcBSKSHUhsuD2gB6mIjqrhu-5lGXMNnZQPIO4n8R896YQy "Terminal")

## Step 2 - Setup Python3 Environment
- Python3 (3.5 at the time of writing) should be already available on EC2 but pip still needs to be installed.
-  Setup Flask
- Get Environment
> **Command:** 
> $ sudo apt-get install python3-pip
> $ pip3 install virtualenv
> $ pip install Flask

## Step 3 - Uploading Files to EC2 Instance
- I have used FileZilla to upload the relevant files
 1.  Edit (Preferences) > Settings > Connection > SFTP, Click "Add key file”
2.  Browse to the location of your .pem file and select it.
3.  A message box will appear asking your permission to convert the file into ppk format. Click Yes, then give the file a name and store it somewhere.
4.  If the new file is shown in the list of Keyfiles, then continue to the next step. If not, then click "Add keyfile..." and select the converted file.
5.  File > Site Manager Add a new site with the following parameters:
    
    **Host**: Your public dns name of ec2 instance, or the public ip address of the server
    
    **Protocol**: SFTP
    
    **Logon Type**: Normal
    
    **User**: From the  [docs](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AccessingInstancesLinux.html): "For Amazon Linux, the default user name is  **ec2-user**. For RHEL5, the user name is often root but might be ec2-user. For Ubuntu, the user name is  **ubuntu**. For SUSE Linux, the user name is  **root**. For Debian, the user name is  **admin**. Otherwise, check with your AMI provider."
    
    Press Connect Button - If saving of passwords has been disabled, you will be prompted that the logon type will be changed to 'Ask for password'. Say 'OK' and when connecting, at the password prompt push 'OK' without entering a password to proceed past the dialog.
    
    **Note:**  FileZilla automatically figures out which key to use. You do not need to specify the key after importing it as described above.
- Drag and drop all the relevant files(index.html, mainpage.css, features.pkl, rfc1.pkl).
- Installed Numpy, Pandas , NLTK in order to run the model_api.py

## Step 4 - Running the model_api.py
- Commands to run this project
- Go to the project directory in terminal and type the following commands
> $ export FLASK_APP=model_api.py
> $ sudo nohup python3 model_api.py & 

![enter image description here](https://lh3.googleusercontent.com/DFSKWe4fV-UhYdvE_lQnVlIn-7aij7wsB2YKccxB563N3ARjk8z31ILTYjTZZyWFTOY4JInHt0AN "Terminal")

-Now the server is running.
-You can drop any test.csv file to classify the documents.

![enter image description here](https://lh3.googleusercontent.com/mYtLgbtHdIWgcqLXVg5U9OIMaZRdjsByFi3rHy9dljy4mWXs4V5FzfF5OrqufD9qQYVABWSF4FIc "Final Website")
