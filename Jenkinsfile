pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                echo 'Cloning repository...'
            }
        }

        stage('Build Docker image') {
            steps {
                sh 'docker build -t devops-app .'
            }
        }

        stage('Run container') {
            steps {
                sh 'docker run -d -p 5000:5000 --name devops-app-container devops-app'
            }
        }
    }
}