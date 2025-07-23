pipeline {
  agent {
    kubernetes {
      label 'jenkins-agent-full'
      yaml """
apiVersion: v1
kind: Pod
metadata:
  labels:
    component: ci
spec:
  containers:
  - name: python
    image: python:3.11
    command:
    - cat
    tty: true
  - name: docker
    image: docker:20.10.16
    command:
    - cat
    tty: true
    volumeMounts:
    - mountPath: /var/run/docker.sock
      name: docker-sock
  - name: kubectl
    image: lachlanevenson/k8s-kubectl:v1.27.3
    command:
    - cat
    tty: true
  volumes:
  - name: docker-sock
    hostPath:
      path: /var/run/docker.sock
"""
    }
  }

  triggers {
    pollSCM('* * * * *') // déclenche toutes les minutes si nouveau commit
  }

  stages {
    stage('Test Python') {
      steps {
        container('python') {
          sh 'pip install -r requirements.txt'
          sh 'python test.py'
        }
      }
    }

    stage('Build Docker Image') {
      steps {
        container('docker') {
          sh 'docker build -t localhost:4000/pythontest:latest .'
          sh 'docker push localhost:4000/pythontest:latest'
        }
      }
    }
    stage('Setup SSH known_hosts') {
  steps {
    container('python') { // ou autre container dans ton pod agent qui a bash/ssh
      sh 'mkdir -p ~/.ssh && ssh-keyscan github.com >> ~/.ssh/known_hosts'
    }
  }
}


    stage('Deploy to Kubernetes') {
      steps {
        container('kubectl') {
          sh 'kubectl apply -f ./kubernetes/deployment.yaml'
          sh 'kubectl apply -f ./kubernetes/service.yaml'
        }
      }
    }
  }
}
