# PyVmomi Test Automation Framework

This is a test automation framework for VMware vSphere using PyVmomi and Pytest.

## Getting Started

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure vCenter credentials:**
   - Open `tests/test_connection.py` and replace the placeholder values for `VCENTER_HOST`, `VCENTER_USER`, and `VCENTER_PASSWORD` with your vCenter server details.

3. **Run the tests:**
   ```bash
   pytest
   ```

## Project Structure

- `src/`: Contains the core framework code, such as the vCenter connection manager.
- `tests/`: Contains the test files.
- `requirements.txt`: Lists the Python dependencies for the project.
