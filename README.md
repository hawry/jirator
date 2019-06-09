## Configuration

jirator will look in `~/.jirator/config` for a configuration file, which will specify server to use, credentials for the server and what issue statuses jirator should consider as "open" issues (i.e. the ones that will be shown for you).

### Example config
```json
{
  "server": "http://localhost:2990/jira",
  "username": "fredsusername",
  "password": "fredspassword",
  "status": ["TO DO","IN PROGRESS","ON HOLD", "IN REVIEW", "OPEN"]
}
```

## Contributing

Contributions are welcome. Note that all contributions are subject to the license of this project.

### Setup up dev environment

1. Install the atlassian-plugin-sdk to get a local instance of the Jira REST API to test against. Follow the instructions at
  1. https://developer.atlassian.com/server/framework/atlassian-sdk/downloads/
  1. https://developer.atlassian.com/server/framework/atlassian-sdk/create-a-helloworld-plugin-project/
  1. Run Jira by being in the plugin directory and running `atlas-run`
1. When you've created your plugin and the server is running, login and create a project and a few issues to  test on

### Create a release

Run the following command in the root path:

`python setup.py sdist`

install locally:

`pip install (--user) /path/to/tarfile`
