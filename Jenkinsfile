pipeline {
    agent any
        stages {
            stage('checkout') {
                steps {
                    git 'https://github.com/jachetblix/devops-experts-first.git'
            }
        }
            stage('Install requirements.txt') {
                steps {
                    sh 'pip3 install --user -r requirements.txt'
                }
            }
             stage('Run rest_app') {
                steps {
                    script {
                        sh 'nohup python3 rest_app.py &'
                    }
                }
            }

            stage('Run web_app') {
                steps {
                    script {

                        sh 'nohup python3 web_app.py &'
                }
            }
        }
            stage('Run backend_testing') {
                steps {
                    script {
                        sh 'python3 tests/backend_testing.py'
                }
            }
        }
            stage('Run frontend_testing') {
                steps {
                    script {
                        sh 'python3 tests/frontend_testing.py'
                }
            }
        }
            stage('Run combined_testing') {
                steps {
                    script {
                        sh 'python3 tests/combined_testing.py'
                }
            }
        }
            stage('Run clean_environment') {
                steps {
                    script {
                        sh 'python3 clean_environment.py'
                }
            }
        }
    }
}

