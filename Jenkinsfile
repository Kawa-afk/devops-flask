pipeline {
    agent any

    environment {
        IMAGE_TAG = "${BUILD_NUMBER}"
        DISCORD_WEBHOOK = 'https://discord.com/api/webhooks/1381349097583280148/La4R4y_MRvm7Lp3QK2M1O7fgzrlF2C6fjQjI5kM9tOrlJpmj7yMzt_rcUJoizhJeKcmo'
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
                        -v "$WORKSPACE:/app" \
                        -w /app \
                        python:3.10-slim \
                        bash -c "pip install flake8 && flake8 ."
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
                sh 'docker-compose up -d web redis'
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
        success {
    sh """
        curl -H "Content-Type: application/json" \
             -X POST \
             -d '{"username": "Jenkins", "content": "✅ Pipeline zakończony **sukcesem** (Build #${BUILD_NUMBER})"}' \
             $DISCORD_WEBHOOK
    """
}
failure {
    sh """
        curl -H "Content-Type: application/json" \
             -X POST \
             -d '{"username": "Jenkins", "content": "❌ Pipeline **nie powiódł się** (Build #${BUILD_NUMBER})"}' \
             $DISCORD_WEBHOOK
    """
}

        always {
            echo 'Pipeline finished.'
        }
    }
}
