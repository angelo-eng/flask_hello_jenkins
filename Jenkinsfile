pipeline {
  agent {
    kubernetes {
      label 'jenkins-agent'
      yaml """
apiVersion: v1
kind: Pod
metadata:
  labels:
    some-label: jenkins-agent
spec:
  containers:
  - name: python
    image: python:3.7
    command:
    - cat
    tty: true
  - name: docker
    image: docker:20.10.16-dind
    securityContext:
      privileged: true
    volumeMounts:
    - name: docker-sock
      mountPath: /var/run/docker.sock
  - name: kubectl
    image: lachlanevenson/k8s-kubectl:v1.27.1
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

  stages {
    stage('Setup SSH known_hosts') {
      steps {
        container('python') {
          sh '''
            mkdir -p ~/.ssh
            ssh-keyscan github.com >> ~/.ssh/known_hosts
          '''
        }
      }
    }

    stage('Checkout') {
      steps {
        container('python') {
          sshagent(['github-ssh-key-id']) {
            sh '''
              git clone -b feature1 git@github.com:angelo-eng/flask_hello_jenkins.git
            '''
          }
        }
      }
    }

    stage('Install dependencies') {
      steps {
        container('python') {
          sh 'pip install -r flask_hello_jenkins/requirements.txt'
        }
      }
    }

    stage('Build Docker image') {
      steps {
        container('docker') {
          sh 'docker build -t flask-jenkins-app flask_hello_jenkins/'
        }
      }
    }

    stage('Push Docker image') {
      steps {
        container('docker') {
          withCredentials([usernamePassword(credentialsId: 'dockerhub', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
            sh '''
              echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
              docker tag flask-jenkins-app $DOCKER_USER/flask-jenkins-app:latest
              docker push $DOCKER_USER/flask-jenkins-app:latest
            '''
          }
        }
      }
    }

    stage('Deploy to Kubernetes') {
      steps {
        container('kubectl') {
          sh 'kubectl apply -f flask_hello_jenkins/kubernetes/deployment.yaml'
          sh 'kubectl apply -f flask_hello_jenkins/kubernetes/service.yaml'
        }
      }
    }
  }
}
