# ArgoCD Deployment

## python-helloworld

- Make sure to setup ArgoCD as written in exercises/README.md
- Enter Vagrant Box using `vagrant ssh`
- Create `argocd-python.yaml` as the Kubernetes declarative file
- Create `deployment.yaml` inside the `python-manifests` folder as the deployment file
- Make sure all files has been pushed to repo
- Apply declarative file using `kubectl apply -f argocd-python.yaml`
- Check using `kubectl get application -n argocd`
- Check to ArgoCD IP and sync if it is out of sync
- Check the pods using `kubectl get po -A`
- We can experiment by changing the version of container in the `deployment.yaml` file, sync, and let ArgoCD do the automatic deployment from previous version to new version