pipeline {
  agent any
  stages {
    stage('installing requirements') {
      steps {
        sh 'pip3 install -r requirements.txt'
      }
    }
     stage('run') {
      steps {
        sh 'python3 server.py &'
      }   
    }
     stage('test') {
      steps {
        sh 'python3 -m unittest tests'
      }   
    }
    stage('building docker image from docker file by tagging') {
      steps {
        sh 'docker build -t rchandu3447/chandu-python:$BUILD_NUMBER .'
      }   
    }
    stage('logging into docker hub') {
      steps {
        sh 'docker login --username="rchandu3447" --password="Chandu@123"'
      }   
    }
    stage('pushing docker image to the docker hub with build number') {
      steps {
        sh 'docker push rchandu3447/chandu-python'
      }   
    }
    stage('deploying the docker image into EC2 instance and run the container') {
      steps {
        sh 'ansible-playbook deploy.yml --extra-vars="buildNumber=$BUILD_NUMBER"'
      }   
    }
  }
}


