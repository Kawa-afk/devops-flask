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

        stage('Versioning') {
            steps {
                script {
                    def version = "v${BUILD_NUMBER}"
                    writeFile file: 'version.txt', text: version
                    sh 'git config user.name "jenkins"'
                    sh 'git config user.email "jenkins@localhost"'
                    sh 'git add version.txt'
                    sh 'git commit -m "Add version ${version}" || echo "No changes to commit"'
                    withCredentials([usernamePassword(credentialsId: 'github-token', usernameVariable: 'GIT_USERNAME', passwordVariable: 'GIT_PASSWORD')]) {
                        sh 'git push https://${GIT_USERNAME}:${GIT_PASSWORD}@github.com/Kawa-afk/devops-flask.git HEAD:main || echo "Push skipped"'
                    }
                }
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

        stage('Health Check & Rollback') {
            steps {
                script {
                    def success = false
                    for (int i = 0; i < 15; i++) {
                        def response = sh(script: "curl -sf http://localhost:5000/health || true", returnStatus: true)
                        if (response == 0) {
                            echo "✅ App is healthy and responding."
                            success = true
                            break
                        }
                        echo "⏳ App not healthy yet... (${i + 1}/15)"
                        sleep 2
                    }
                    if (!success) {
                        echo "❌ App failed to respond. Rolling back..."
                        sh 'docker-compose down'
                        error("Deployment failed. Rollback executed.")
                    }
                }
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
