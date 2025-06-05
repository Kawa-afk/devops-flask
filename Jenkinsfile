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

        stage('Code Quality Check') {
            steps {
                echo "Running static code analysis with flake8"
                sh '''
                    docker run --rm \
                        -v $PWD:/app \
                        -w /app \
                        python:3.10-slim \
                        bash -c "pip install flake8 && flake8 app.py"
                '''
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
