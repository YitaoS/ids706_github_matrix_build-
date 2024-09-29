# IDS706 Mini Project
![CI Status](https://github.com/YitaoS/ids706_github_matrix_build-/actions/workflows/ci.yml/badge.svg)

## Getting Started
Purpose of this project:

- Set up a Gitlab Actions workflow
- Test across at least 3 different Python versions

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/YitaoS/ids706_github_matrix_build.git
   cd ids706_github_matrix_build
   ```

2. **Install dependencies**:
   ```bash
   make install
   ```

   This will upgrade `pip` and install the necessary dependencies for development.

3. **Optional: Build the development environment using DevContainer**:
   - Open the project in Visual Studio Code.
   - Run **Reopen in Container** from the Command Palette (`Ctrl + Shift + P` or `Cmd + Shift + P`).

### Usage

- **Run the main script**:
  ```bash
  make run
  ```

- **Run tests**:
  ```bash
  make test
  ```

- **Format the code** using `black`:
  ```bash
  make format
  ```

- **Lint the code** using `flake8`:
  ```bash
  make lint
  ```

### Additional Commands

- **Clean up `.pyc` files and `__pycache__` directories**:
  ```bash
  make clean
  ```

- **Run the full CI process (linting, testing, and formatting check)**:
  ```bash
  make ci
  ```

### CI/CD Status
Continuous Integration (CI) checks are automatically run using GitHub Actions. You can view the current status by looking at the badge at the top of this file.

### Contributing

Feel free to fork the repository and submit pull requests for improvements or bug fixes. Ensure your changes pass the linting and test suites before submission.
