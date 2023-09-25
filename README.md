# Lambda set up

Create lambda function with `Python 3.11` environment for each module you want to use.

In this repo's case we're creating 3 Lambda functions and name them;
> fakeTweetTracker

> respondGenerator

> smsNotification

For each function, write (copy & paste) the code manually in function's codepad and deploy it.

## Required packages

Use `requirements.txt` file to install necessary packages into a folder named `Python`.
(You should name as `Python` for Lambda to recognize the folder)

You can create `requirements.txt` file using this command:
```
pip freeze > requirements.txt
```
And install all dependencies to `Python` folder with this command:
```
pip install -r requirements.txt --target /path/to/Python-folder
```

### Then zip the `Python` folder using:

macOS Terminal: 
```
zip -r package.zip Python
```

Windows Command Prompt:
```
zip -r package.zip Python
```

Now, `package.zip` archive is ready to upload in lambda layer.
Create a lambda layer with `Python 3.11` runtime and upload the zip file.

Add layer to each functions and test them by creating a test event.


