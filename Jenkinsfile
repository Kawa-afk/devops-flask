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
                script {
                    docker.build('devops-app')
                }
            }
        }

        stage('Run container') {
            steps {
                sh 'docker run -d -p 5000:5000 devops-app'
            }
        }
    }
}