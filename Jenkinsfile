pipeline {
    agent any

    environment {
        GIT_REPO = 'git@github.com:N-Otsubo/django-app.git'
        GIT_BRANCH = 'main' // 必要に応じてブランチを変更
    }

    stages {
        stage('Clone Repository') {
            steps {
                script {
                    // リポジトリをクローン
                    rm -rf django-app
                    sh 'git clone -b ${GIT_BRANCH} ${GIT_REPO}'
                }
            }
        }

        stage('Build') {
            steps {
                // ここでビルドプロセスを追加
                echo 'Building...'
            }
        }

        stage('Test') {
            steps {
                // ここでテストプロセスを追加
                echo 'Testing...'
            }
        }

        stage('Deploy') {
            steps {
                // ここでデプロイプロセスを追加
                echo 'Deploying...'
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}

