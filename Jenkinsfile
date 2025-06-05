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

        stage('Remove old container') {
            steps {
                sh 'docker stop flask-app || true'
                sh 'docker rm flask-app || true'
            }
        }

        stage('Run container') {
            steps {
                sh 'docker run -d -p 5001:5000 --name flask-app devops-app'
                sh 'docker ps -a'
                sh 'docker logs flask-app || true'
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished.'
        }
    }
}