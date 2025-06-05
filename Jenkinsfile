pipeline {
    agent any

    environment {
        IMAGE_TAG = "${BUILD_NUMBER}"
    }

    stages {
        stage('Clone') {
            steps {
                echo "Repo already checked out"
            }
        }

        stage('Docker Compose - Down') {
            steps {
                sh 'docker-compose down || true'
            }
        }

        stage('Docker Compose - Build and Up') {
            steps {
                sh 'docker-compose build --build-arg IMAGE_TAG=${IMAGE_TAG}'
                sh 'docker-compose up -d'
            }
        }

        stage('Check Running Containers') {
            steps {
                sh 'docker ps -a'
            }
        }

        stage('Logs') {
            steps {
                sh 'docker logs $(docker ps -qf "name=web") || true'
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished.'
        }
    }
}