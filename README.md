
# **Django Newspaper Web App**

This project is a newspaper web application developed with Django. It allows registered users to create, read, update, and delete articles, as well as leave comments on articles by other users.

## Features
- **User Registration:** Users can sign up to create an account.
- **Login and Authentication:** Users can log in to their existing accounts.
- **Article Creation:** Users can create new articles once logged in.
- **Article Reading:** Users can view existing articles on the homepage and individual detail pages.
- **Article Updating:** Users can edit articles they have created.
- **Article Deletion:** Users can delete articles they have created.
- **Comments:** Users can leave comments on articles by other users.

## Installation and Setup
1. Clone this repository to your local machine.
2. Create a virtual environment for the project and activate it.
3. Install project dependencies using the requirements.txt file.
4. Configure the database in the settings.py file.
5. Perform necessary migrations using the `python manage.py migrate` command.
6. Start the development server with the `python manage.py runserver` command.

## Usage Examples
1. Register a new user account.
2. Log in with your credentials.
3. Create a new article from the homepage.
4. Read existing articles on the homepage by clicking on their titles.
5. Edit or delete an article you have created from the article detail page.
6. Leave a comment on an article created by another user.

## Testing
This project includes automated tests to ensure its correct functionality. You can run the tests using the `python manage.py test` command.

## Contributing
If you would like to contribute to this project, follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bug fix (`git checkout -b feature/feature-name`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push your changes to your remote repository (`git push origin feature/feature-name`).
5. Open a Pull Request on GitHub.

## FAQ
- **How can I reset my password if I forget it?**
  - You can reset your password using the "Forgot your password?" feature on the login page.

- **Can I delete a comment I have left on an article?**
  - No, currently comments cannot be deleted by the users who left them.
