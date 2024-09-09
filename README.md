# my-ci-cd-pipeline
First CI/CD Pipeline Project

My CI/CD Pipeline Project: A Journey from Scratch

Overview

In this project, I set out to create a CI/CD pipeline for a simple Flask application. The goal was to learn about version control, code quality, testing, and deployment.

Key Steps Taken

Repository Creation:

I started by creating a GitHub repository called "my-ci-cd-pipeline" to manage my project and track changes.

Local Setup:

I cloned the repository to my local machine, which created a folder for my project files.

Code Quality Integration:

I integrated SonarQube to help maintain code quality from the beginning by creating a configuration file.

Flask Application Development:

I built a simple Flask application with basic routes, including a "Hello, World!" route and an "About" page. This served as the foundation for my project.

Testing Setup:

I wrote tests to ensure my application behaves as expected. These tests check if the app returns the correct messages and status codes for different routes.

GitHub Actions Integration:

I set up a GitHub Actions workflow to automatically run tests whenever changes are pushed to the repository.

Challenges Faced and Overcome

Permission Issues:

I encountered errors when trying to access my project directory. I resolved this by enabling Full Disk Access for my terminal application.

Setting Up the Testing Environment:

I installed the necessary tools (Flask and pytest) and set up a virtual environment to manage my project dependencies.

Import Errors:

I faced issues with Python not finding my application files. I fixed these by organising my project structure and ensuring all necessary files were in place.

CI Workflow Configuration:

Initially, the GitHub Actions workflow failed due to incorrect configuration. I resolved this by updating the workflow file to properly set up the Python environment and run tests.

Dependency Management:

I learned to create and maintain a requirements.txt file to ensure consistent dependencies across different environments.

Key Achievements

Successful Local Test Execution:

After resolving import issues, I successfully ran my tests locally, confirming that my Flask app works correctly.

Functional CI Pipeline:

I achieved a green tick on my GitHub Actions workflow, indicating that my tests are running successfully in the CI environment.

Reflections and Lessons Learned

This project has taught me valuable lessons about:

- Setting up a project with GitHub and version control.

- Ensuring code quality with tools like SonarQube.

- Writing and running tests for a Flask application.

- Managing dependencies with virtual environments.

- Configuring and troubleshooting CI pipelines using GitHub Actions.

- The importance of proper project structure and import management in Python.

Next Steps

- Expand the Flask application with more features and corresponding tests.

- Enhance the CI pipeline with additional checks like code linting and coverage reporting.

- Explore deployment options and potentially add deployment steps to the CI/CD pipeline.

- Improve project documentation, including updating the README with CI process information.

- Implement branch protection rules in GitHub to enforce code quality checks.
