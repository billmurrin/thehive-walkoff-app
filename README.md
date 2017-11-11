# TheHive WALKOFF App
## DISCLAIMER: ALPHA Status

TheHive WALKOFF App aims to (eventually) provide WALKOFF orchestration for receiving TheHive webhooks as well as creating cases in TheHive. 

[TheHive](https://github.com/CERT-BDF/TheHive) is a modern incident case management system geared for Security Operation Centers and Computer Emergency Response Teams.

[WALKOFF](https://github.com/iadgov/WALKOFF) is an OSS project made by the NSA that provides an automation framework for automating repetitive tasks.

## Installation
1. Clone the repo
```
git clone https://github.com/billmurrin/thehive-walkoff-app.git
```
2. Copy the TheHive directory to WALKOFF/apps directory
3. From the WALKOFF directory, install the package dependencies in requirements.txt
```
# python installDependencies -a TheHive
```
4. Start, or restart, the WALKOFF web server
```
# python startServer.py
```

## Usage
* The 'Web Hooks' action is an event that will listen for web hooks from TheHive.
* You can configure TheHive to send Case creation and update events to the App by adding the following to your application.conf (restart thehive after):
```
webhooks {
  myLocalWebHook {
    url = "http://10.0.0.30:5000/apps/TheHive/thehive_webhook"
  }
}
```
* As of this writing. It will receive the data but not do much with it.
* You must add the 'Web Hooks' event to a workflow and start it in order for it to be available to TheHive

## Way Ahead
1. Provide sample workflows.
2. Additional actions for interacting with return objects
3. @actions for creating cases in TheHive
4. Implement tests using pytest.