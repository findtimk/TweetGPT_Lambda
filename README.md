# Lambda set up

Create lambda function with `Python 3.11` environment for each module you want to use.

In this repo's case we're creating 2 lambda functions and name them;
> fakeTweetTracker

> respondGenerator

For each function, write (copy & paste) the code manually in function's codepad and deploy it.

## Required packages

Use `requirements.txt` file to install necessary packages into a folder named `Python`.

(You should name as `Python` for Lambda to recognize the folder)

Installation command:
```
pip install -r requirements.txt --target /path/to/target/Python
```

Then zip the root folder named `'Python'` using:

macOS Terminal: 
```
zip -r package.zip Python
```

Windows Command Prompt:
```
zip -r package.zip Python
```

Now, `package.zip` archive is ready to upload in lambda layer.
Create a lambda layer with `Python 11` runtime and upload the zip file.

Add layer to each functions and test them by creating a test event.


