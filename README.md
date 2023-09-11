# Lambda set up

Create lambda function with `Python 11` environment for each module you want to use.

In this repo's case we're creating 2 lambda functions and name them;
> fakeTweetTracker

> respondGenerator

## Required packages

Create a lambda layer with `Python 11` runtime for functions.
Use `requirements.txt` file to install necessary packages into the folder named `Python`.

(You should name as 'Python' for AWS to recognize the folder)

Installation command:
```
pip install -r requirements.txt --target /path/to/target/Python
```

Then zip the root folder `'Python'` using:

macOS Terminal: ```zip -r package.zip Python```

Windows Command Prompt: ```zip -r package.zip Python```




