## Configuration

jirator will look in `~/.jirator/config` for a configuration file, which will specify server to use, credentials for the server and what issue statuses jirator should consider as "open" issues (i.e. the ones that will be shown for you).

Parts of the configuration file is meant to be used by you as a user, and parts of it should only be modified by the application itself. The example config shows the fields that you can change without affecting the inner workings of the application.

### Example config
```json
{
  "server": "http://localhost:2990/jira",
  "username": "fredsusername",
  "password": "fredspassword",
  "status": ["TO DO","IN PROGRESS","ON HOLD", "IN REVIEW", "OPEN"]
}
```

## Usage
All commands require that you are standing in your project root and have intialized a git repository, otherwise no git actions will be performed.
```
Usage: jirator [OPTIONS] COMMAND [ARGS]...

Options:
  -v, --verbose  enable debug logging
  --version      Show the version and exit.
  --help         Show this message and exit.

Commands:
  assign
  work
```

### See a list of your assigned tasks
`jirator work`, and then select the issue you wish to work on. `jirator` will call `git checkout -b [issue]` for you automatically.

### Assign me to a specific task and move it to "in progress"
`jirator assign [issue]`

If you haven't configured which transition group / workflow id to use as an "in progress" status, `jirator` will fetch a list of available transitions to use, and you can select a default id to use in the future. `jirator` will then checkout a new branch for you automatically.

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
