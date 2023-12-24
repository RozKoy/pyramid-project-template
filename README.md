# Pyramid Project Template

Getting Started
---------------

- Change directory into your newly created project if not already there. Your
  current directory should be the same as this README.txt file and setup.py.

```bash
cd backend_uts_pwl
```

- Create a Python virtual environment, if not already created.

```bash
python3 -m venv env
```

- Upgrade packaging tools, if necessary.

```bash
env/bin/pip install --upgrade pip setuptools
```

- Install the project in editable mode with its testing requirements.

```bash
env/bin/pip install -e ".[testing]"
```

- Initialize and upgrade the database using Alembic.

    - Generate your first revision.

    ```bash
    env/bin/alembic -c development.ini revision --autogenerate -m "init"
    ```

    - Upgrade to that revision.

    ```bash
    env/bin/alembic -c development.ini upgrade head
    ```

- Load default data into the database using a script.

```bash
env/bin/initialize_backend_uts_pwl_db development.ini
```

- Run your project's tests.

```bash
env/bin/pytest
```

- Run your project.

```bash
env/bin/pserve development.ini
```