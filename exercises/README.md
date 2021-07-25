# Exercises for Docker and Kubernetes deployment

This folder servers as an exercise for the SUSE Udacity Cloud Native Fundamentals Scholarship

## Docker

There are two docker deployment.
1. In the folder `python-helloworld` for docker deployment in Python
2. In the folder `go-helloworld` for docker deployment in Golang

Most of the project, including using vagrant, will be done in the `go-helloworld` folder.

## Declarative Kubernetes

All declarative Kubernetes can be found in the `manifests` folder.

## ArgoCD Setup

Is a declarative Continuous Delivery tool for Kubernetes, which follows the GitOps patterns.

- Make sure vagrant has been set up with Kubernetes (see readme.MD in `./exercise/go-helloworld/` folder)
- Enter vagrant box using `vagrant ssh`
- Install [ArgoCD](https://argoproj.github.io/argo-cd/getting_started/#1-install-argo-cd), or copy the code below:

    ```
    kubectl create namespace argocd
    kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
    ```

- Check installation using `kubectl get po -n argocd`. Use `zypper install apparmor-parser` if necessary.
- Look at services using `kubectl get svc -n argocd`
- Some glossary:

    ```
    NAME                    TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)                      AGE
    argocd-dex-server       ClusterIP   10.43.191.172   <none>        5556/TCP,5557/TCP,5558/TCP   10m
    argocd-metrics          ClusterIP   10.43.241.129   <none>        8082/TCP                     10m
    argocd-redis            ClusterIP   10.43.157.70    <none>        6379/TCP                     10m
    argocd-repo-server      ClusterIP   10.43.139.85    <none>        8081/TCP,8084/TCP            10m
    argocd-server           ClusterIP   10.43.11.207    <none>        80/TCP,443/TCP               10m
    argocd-server-metrics   ClusterIP   10.43.167.99    <none>        8083/TCP                     10m
    ```

    We can see that **argocd-server** is exposed using **ClusterIP**, which will be only available within the cluster<br/>
    using the `10.43.11.207` IP on `80/TCP,443/TCP` port

- Use Nodeport to expose service to the host by editing `kubectl get svc -n argocd argocd-server -o yaml > argocd-nodeport.yaml`
- Remove `annotations` content
- Remove `managedFields` (if any)
- Change name to `argocd-server-nodeport`
- Remove `resourceVersion`, `selfLink`, and `uid` since this already appended
- Remove `ClusterIP` since it has been provisioned and added to the manifest
- Change `type` to `NodePort`. We can choose port between 3000-32767 as per [Kubernetes documentation](https://kubernetes.io/docs/concepts/services-networking/service/) and add under `http` and `https` with different ports (e.g. 30007 and 30008)
- Apply changes using `kubectl apply -f argocd-nodeport.yaml`
- Verify using `kubectl get svc -n argocd`
- Proceed to the IP provided by the Vagrant Box with port 30008
- Connect to [ArgoCD by CLI](https://argoproj.github.io/argo-cd/getting_started/#4-login-using-the-cli) using `kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d`
- Login using `admin` and the password which provided by the command above
