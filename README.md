# Dad Jokes Web UI #

![Build Status](https://github.com/jaysgrant/dadjoke-ui/workflows/dadjoke_ui/badge.svg)
![GitHub release (https://github.com/jaysgrant/dadjoke-ui/releases)](https://img.shields.io/github/v/release/jaysgrant/dadjoke-ui?include_prereleases)

A simple Python 3 Flask based web UI for the [Dad Jokes microservice](https://github.com/yesinteractive/dad-jokes_microservice) project. The project is built around the idea of deployment hosted on Docker, and Kubernetes.

## Getting Started ##

See the deployment examples within the [examples](./examples) folder.

### Kubernetes ###

The Kubernetes example deployes two services, and two deployments.

#### DadJokes Microservice ####

* Creation of a service, and deployment of the DadJokes Microservice to generate the jokes.
* Service creation with a type of NodePort.

#### DadJokes Web UI ####

* Creation of a service, and deployment of the DadJokes UI, providing a web view of the output of the DadJokes Microservice.
* Service creation with a type of NodePort.

#### Installation on Kubernetes ####

Installation can be performed by running the following command.
```bash
kubectl apply -f examples/kubernetes/dadjokes.yaml
```

### Docker ###

* Todo: Docker instructions