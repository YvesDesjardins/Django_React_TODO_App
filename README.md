# 1. Django TODO App
Create a Python 3 Django app that provides a REST API for a simple TODO app. It should provide the following API:

Add a TODO. Each TODO is composed of:
- State: todo, in-progress, done
- Due date.
- TODO text.
- Delete one or more TODOs.
- List all TODOs.
- Able to filter TODOs by state and/or due-date.
## 1.1. Base Software
Use:
- Python 3.7.x
- Django 2.x
- SQLite as datastore.
- Any other Python packages to help with the assignment.

Use pipenv to setup the virtual environment. I.e., we should be able to run “pipenv install” from the root of your project folder to create the virtual environment and install all the packages into it. If you haven’t used pipenv yet, read up about it here: https://docs.pipenv.org/
## 1.3. Test Script
Write unit tests for the API. Django has built-in unit testing functionality, we strongly encourage you to use it.
## 1.4. OS
Both the app and test script should run on Ubuntu Server 18.04.
## 1.5. Readme
Add a readme file in Markdown format. Write step-by-step instructions with the terminal commands required to install the Django app, run the Django app.
# 2. React.js Interface
Create a responsive interface for your TODOs app using React + Redux to interface with the API you made. The app should include the following commands:
- Add a new TODO that is comprised of: State (todo, in-progress, done), Due date & TODO text
- List all TODO in a table view 
- Sort due date by descending order
- Keep each TODO on one line. If it doesn’t fit the screen, cut off the text and terminate with a ‘...’
- Highlight past due date TODOs in red, and done TODOs in green
- Make it possible to click on a TODO and view it individually
- Toggle the done state of one or more TODOs in the list (done > todo)
- Delete one or more TODOs in the list
- Make the interface usable on both mobile and desktop

## 1.1. Base Software
Use:
- React.js
- Redux
## 1.4. OS
The app should run on Ubuntu Server 18.04.
## 1.5. Readme
Add a readme file in Markdown format. Write step-by-step instructions with the terminal commands required to install the React.js app, run the React.js app.
# 3. Delivery
Submit the assignment as a public repo in GitHub, BitBucket, or GitLab. Put each part into a separate folder. E.g.,

```
<repo root>
django_app/
react_interface/
```
