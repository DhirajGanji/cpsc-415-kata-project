@ECHO off

kubectl apply -f ./k8s-prereqs/namespace-decl.yaml
kubectl apply -f ./k8s-prereqs/env-configmap.yaml
kubectl apply -f ./k8s-files

ECHO Up and running! Please go to localhost:30000 to use application.

PAUSE
