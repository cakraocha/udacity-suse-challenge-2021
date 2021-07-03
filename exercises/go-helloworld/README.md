# Go Hello World

This is a simple Go web application that prints a "Hello World" message.

## Run the application

This application listens on port `6111`

To run the application, use the following command:
```
go run main.go 
```

Access the application on: http://127.0.0.1:6111/

## Using vagrant with Kubernetes k3s

- Enter command `vagrant up` to build a vagrant box as specified in Vagrantfile
- Enter vagrant box using `vagrant ssh`
- Install k3s using `curl -sfL https://get.k3s.io | sh -`
- Check if it's up and running using `kubectl get no`, use super user such as `sudo su`
- Some useful commands:
    ```
    kubectl get deploy
    kubectl get no
    kubectl get rs
    kubectl describe no <node-name>
    kubectl describe pod <pod-name>
    ```
- Deploy the go-helloworld application using `kubectl create deploy go-helloworld --image=cakraocha/go-helloworld:v1.0.0`
- If the pod is not running, install depedencies by running `zypper install apparmor-parser`
- Forward the port by running `kubectl port-forward --address 0.0.0.0 po/<pod-name> 6111:6111`
- See the app by using the vagrant ip address with the specified port above

## Edit Kubernetes deployment
- Enter command `kubectl edit deploy go-helloworld -o yaml`
- This will let you into the vi mode. Edit where the container name into other version
- :wq, after that see if the app is up and running by forwarding the port

## Delete Kubernetes deployment
`kubectl delete deploy <deployment-name>`

## Some commands for Kubernetes context
```
# create the namespace
# note: label option is not available with `kubectl create`
kubectl create ns demo

# label the namespace
kubectl label ns demo tier=test

# create the nginx-alpine deployment 
kubectl create deploy nginx-alpine --image=nginx:alpine  --replicas=3 --namespace demo

# label the deployment
kubectl label deploy nginx-alpine app=nginx tag=alpine --namespace demo

# expose the nginx-alpine deployment, which will create a service
kubectl expose deployment nginx-alpine --port=8111 --namespace demo

# create a config map
kubectl create configmap nginx-version --from-literal=version=alpine --namespace demo
```