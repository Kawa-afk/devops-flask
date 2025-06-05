pipeline {
    agent any

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
                sh 'docker-compose up -d --build'
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