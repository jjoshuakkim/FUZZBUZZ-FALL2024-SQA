Activities and Lessons learned:

Joshua Kim
I was responsible for creating a Git Hook that will run and report all security weaknesses in the project and integrating continuous integration with Github Actions. A key component of security weakness identification workflow involves the integration of a static analysis tool, bandit, into a pre-commit Git hook. This hook automatically scans code for security weaknesses before each commit, ensuring that only secure code is merged into the main branch. We've incorporated continuous integration (CI) with GitHub Actions to automate the security analysis process. Whenever code is pushed to the main branch, the CI pipeline triggers, executing the static analysis tool and failing the build if critical vulnerabilities are detected. This automated approach helps maintain code quality and security throughout the development lifecycle. The CI pipeline serves as an additional layer of security. By automatically scanning the codebase, we can identify and address vulnerabilities early in the development process. This proactive approach helps prevent security breaches and minimizes the impact of potential attacks.