pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                echo "Repo already checked out"
            }
        }

        stage('Build Docker image') {
            steps {
                sh 'docker build -t devops-app .'
            }
        }

        stage('Run container') {
            steps {
                sh 'docker stop flask-app || true'
                sh 'docker rm flask-app || true'
                sh 'docker run -d -p 5000:5000 --name flask-app devops-app'
            }
        }
    }
}
