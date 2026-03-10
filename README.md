# 🚀 QA Automation Challenge - Multi-App QA Automation Framework

Professional automated testing suite designed to validate critical modules of "The Internet" platform. This project follows **Senior QA standards**, utilizing a **BDD (Behavior Driven Development)** approach for readability and the **Page Object Model (POM)** pattern for high maintainability.
Professional automated testing suite designed to validate critical business flows for **The Internet (Herokuapp)** and **SauceDemo E-commerce**. This project follows **Senior QA standards**, utilizing **Playwright, Python**, and **Pytest-BDD**.

## 🛠️ Tech Stack
*   **Language:** Python 3.10+
*   **Automation Framework:** [Playwright](https://playwright.dev) (Web-First Assertions & Auto-waiting)
*   **Test Runner & BDD:** Pytest + Pytest-BDD
*   **Reporting:** Allure Reports (Interactive Dashboards with Screenshots)
*   **Logging:** Python Logging Module (Full Traceability)
*   **Environment Management:** Python-dotenv

## 📁 Project Deliverables


| Deliverable | Link |
| :--- | :--- |
| **Bug Tracking Board** | [Trello Board] https://trello.com/invite/b/69af7bb1cc2415df2a179685/ATTI9ff18aa35c3414dd4fbf039c97d9485e8D7AAF26/mi-tablero-de-trello |
| **Strategic Planning & Test Cases** | [PDF Document](./docs/QA%20Stategy%202026.pdf) |
| **Automation Report** | [Allure Results](./reports/allure-results) |

## 🏗️ Project Architecture
```text

.
├── features/
│   ├── herokuapp/          # Exercise 1: Auth, Upload, Dynamic, Dropdown
│   └── saucedemo/           # Exercise 2: E2E Purchase & Responsive flows
├── pages/
│   ├── common/             # Shared Core (BasePage)
│   ├── herokuapp/          # Page Objects for Exercise 1
│   └── saucedemo/           # Page Objects for Exercise 2
├── step_definitions/
│   ├── test_herokuapp.py   # Glue code for Exercise 1
│   └── test_saucedemo.py   # Glue code for Exercise 2
├── docs/                   # Strategic Planning PDFs (Exercise 1 & 2)
├── conftest.py             # Global Fixtures & Mobile Viewport Logic (@mobile)
├── pytest.ini              # Markers & Logging configuration
└── .env                    # Environment variables (Sensitive data)
```

## 📋 Test Modules Overview

This test suite covers the following critical modules:

- **Login Module** - User authentication and session management
- **Dropdown Selection** - Dynamic element selection and validation
- **Dynamic Loading** - Asynchronous content loading and visibility handling
- **File Upload** - File upload functionality and validation

## 🚀 Setup & Installation

### 1. Prerequisites
- Python 3.10 or higher installed
- Node.js (Required for Allure Reporting CLI)
- Git for version control

### 2. Environment Setup

```bash
# Create and activate virtual environment
python -m venv venv
.\venv\Scripts\activate  # Windows
# or for Linux/Mac:
# source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Install Playwright Browsers
playwright install chromium
```

### 3. Global Allure Installation

```bash
# Required to generate visual reports
npm install -g allure-commandline --save-dev
```

### 4. Configuration

Create a `.env` file in the root directory:

```ini
BASE_URL=https://the-internet.herokuapp.com
USER_NAME=tomsmith
USER_PASSWORD=SuperSecretPassword!
```

## 🧪 Execution & Reporting

### Run All Tests

```bash
pytest
```

### Run by Category (Tags)

```bash
# Only Smoke tests
pytest -m smoke

# Only Regression suite
pytest -m regression

# Run Exercise 1 (Herokuapp)
pytest -m herokuapp

# Run Exercise 2 (SauceDemo)
pytest -m saucedemo

# Run specific test file
pytest step_definitions/test_login_steps.py

# Run Mobile Responsive tests only
pytest -m mobile

# Run with verbose output
pytest -v

# Run and generate Allure results
pytest --alluredir=reports/allure-results

allure generate reports/allure-results -o reports/allure-report --clean

```

### Generate & View Allure Report

```bash
allure serve reports/allure-results
```

This command will open an interactive dashboard in your default browser, showing:
- Execution trends and statistics
- Test step details with timings
- Full logs and assertions
- Screenshots of failed tests
- Environment information

## 🏗️ Detailed Project Structure

| Directory | Purpose |
|-----------|---------|
| `features/` | BDD scenarios in Gherkin format (.feature files) |
| `pages/` | Page Object Model classes with locators and methods |
| `step_definitions/` | Glue code connecting Gherkin steps to Python methods |
| `reports/allure-results/` | Test execution results and Allure artifacts |
| `conftest.py` | Pytest configuration, global fixtures, hooks, and screenshot capture |
| `pytest.ini` | Pytest execution settings and custom markers |
| `.env` | Environment variables (not committed to version control) |

## 📖 Page Object Model Pattern

Each page module follows the POM design pattern:

- **Locators**: All element selectors defined at the class level
- **Actions**: Methods encapsulating user interactions
- **Assertions**: Helper methods for validation
- **Navigation**: Methods for page transitions

Example:
```python
class LoginPage(BasePage):
    LOCATOR_USERNAME = "id=username"
    LOCATOR_PASSWORD = "id=password"
    LOCATOR_LOGIN_BTN = "button:has-text('Login')"
    
    def login(self, username: str, password: str):
        self.fill(self.LOCATOR_USERNAME, username)
        self.fill(self.LOCATOR_PASSWORD, password)
        self.click(self.LOCATOR_LOGIN_BTN)
```

## 🐞 Bug Tracking & QA Planning

As part of the assignment requirements, manual exploratory testing was performed. All identified defects and the strategic planning sheet are located here:

- **Trello Board (Bug Tracking)**: [INSERT_YOUR_TRELLO_LINK_HERE]
- **QA Planning Sheet**: Located in the docs/ folder (or root) of this repository

## 🔧 Troubleshooting

### Common Issues & Solutions

#### 1. Playwright Browser Installation Failed
```bash
# Reinstall browsers with cache clearing
playwright install --with-deps chromium
```

#### 2. Allure Report Not Generating
```bash
# Check if allure is installed globally
allure --version

# Reinstall if needed
npm install -g allure-commandline --save-dev
```

#### 3. Tests Timing Out
- **Issue**: Tests fail due to slow network or long loading animations (e.g., Dynamic Loading).
- **Solution**: We use Playwright's **web-first assertions** with custom timeouts where needed.
- **Example**:
  ```python
  # Specifically for slow dynamic content:
  expect(page.locator("#finish")).to_be_visible(timeout=10000)
    ```

#### 4. Element Not Found / StaleElementReference
- **Issue**: Dynamic elements not loading before interaction
- **Solution**: Playwright auto-waits for elements. Verify selectors in page objects
- **Debugging**: Run tests with `--headed` flag to see browser:
```bash
pytest --headed
```

#### 5. Screenshot Path Issues on Windows
- **Issue**: Screenshots not saved with backslash paths
- **Solution**: Paths are normalized in `conftest.py`. Ensure reports folder exists:
```bash
mkdir reports/allure-results
```

#### 6. .env File Not Loading
- **Issue**: Environment variables undefined
- **Solution**: Ensure `.env` is in root directory and `python-dotenv` is installed
```bash
pip install python-dotenv
```

## 📝 Contributing Guidelines

### Code Standards

1. **Follow PEP 8** Python style guide
2. **Use meaningful names** for variables, functions, and test cases
3. **Add docstrings** to all custom functions and classes
4. **Include comments** for complex logic
5. **Keep methods small** - Single Responsibility Principle

### Test Development Workflow

1. **Create a feature file** in `features/` folder with Gherkin scenarios
2. **Implement page objects** in `pages/` with locators and methods
3. **Write step definitions** in `step_definitions/` connecting Gherkin to code
4. **Run tests locally** before committing:
   ```bash
   pytest -v
   ```
5. **Generate Allure report** to verify test execution:
   ```bash
   allure serve reports/allure-results
   ```

### Git Workflow

1. Create a feature branch:
   ```bash
   git checkout -b feature/module-name
   ```
2. Make changes and commit with descriptive messages:
   ```bash
   git commit -m "feat: add login page tests"
   git commit -m "fix: update dropdown selector"
   git commit -m "doc: enhance README with troubleshooting"
   ```
3. Push and create a Pull Request:
   ```bash
   git push origin feature/module-name
   ```

### Pull Request Checklist

- [ ] Tests pass locally (`pytest -v`)
- [ ] Allure report generated successfully
- [ ] No unused imports
- [ ] Code follows PEP 8 standards
- [ ] Docstrings added to new functions
- [ ] Feature files are clear and descriptive
- [ ] No credentials or sensitive data in code

## 🚀 CI/CD Integration

### Running Tests in CI/CD Pipeline

For integration with GitHub Actions, GitLab CI, or Jenkins:

```yaml
# Example GitHub Actions workflow
- name: Install dependencies
  run: |
    pip install -r requirements.txt
    playwright install chromium

- name: Run tests
  run: pytest --alluredir=reports/allure-results

- name: Publish Allure Report
  if: always()
  uses: simple-elf/allure-report-action@master
  with:
    allure_results: reports/allure-results
    allure_history: reports/history
```

## 📊 Test Coverage & Metrics

After running tests, check coverage:

```bash
# Run with coverage
pytest --cov=pages --cov=step_definitions --cov-report=html

# View coverage report
start htmlcov/index.html  # Windows
```

## 💡 Best Practices

1. **Use Explicit Waits** - Playwright handles this automatically, but verify timing
2. **Isolate Tests** - Each test should be independent
3. **Mock External APIs** - When testing, avoid real API calls
4. **Keep Fixtures Lean** - Use `conftest.py` for setup/teardown
5. **Log Strategically** - Capture relevant info without noise
6. **Version Control** - Exclude `venv/`, `__pycache__/`, `.env`, and reports

## 📚 Additional Resources

- [Playwright Documentation](https://playwright.dev/python/)
- [Pytest Documentation](https://docs.pytest.org/)
- [Pytest-BDD Guide](https://pytest-bdd.readthedocs.io/)
- [Allure Report Docs](https://docs.qameta.io/allure/)
- [The Internet Herokuapp](https://the-internet.herokuapp.com/)

## 👤 Contact & Support

For questions, issues, or contributions:

- **Report Issues**: Create an issue in this repository
- **Suggest Features**: Use GitHub Discussions
- **Pull Requests**: Follow the Contributing Guidelines above

---

**Last Updated**: March 2026  
**Version**: 1.0  
**Status**: Active & Maintained
