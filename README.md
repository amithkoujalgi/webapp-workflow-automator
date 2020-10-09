## Framework for Webapp Workflow Automation

### Development

##### Prerequisites:

- Python3.7+
- A run environment which can open browser window. Preferably, a non-headless *nix environment..

##### Start the server:

```bash
cd webapp_workflow_automator/rest_api
uvicorn server:app --reload
```
Server starts up at http://127.0.0.1:8000/

For API docs, head to http://127.0.0.1:8000/docs in your browser to checkout the available API endpoints and their specifications.

##### Run build to generate a distributable artifact (.whl):
```bash
./build.sh
```

This generates the whl file under `dist` directory.
