# Helm Chart

Helm is a package manager that manages Kubernetes manifests through charts.

## python-helloworld

- Make sure to setup ArgoCD as written in exercises/README.md
- Enter Vagrant Box using `vagrant ssh`
- Create `argocd-helm-python.yaml` as the Helm-Kubernetes declarative file
- Configure `Chart.yaml` file
- Create `templates` with declarative files / manifests that want to be deployed, in this case `namespace.yaml` and `deployment.yaml`
- Create `values.yaml` or `values-prod.yaml` as a parameter file for templates
- Make sure all has been pushed to repo
- Apply declarative file using `kubectl apply -f argocd-helm-python.yaml`
- Check to ArgoCD IP and sync if it is out of sync
- Check inside the vagrant box using `kubectl get po -n test`
- Similar steps above if want to use `values-prod.yaml` as the parameter, just use `kubectl apply -f argocd-helm-python-prod.yaml` as the Helm Kubernetes file
- Sync in ArgoCD IP, and check inside the vagrant box using `kubectl get po -n prod`
