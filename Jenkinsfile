pipeline{
    agent any
    environment{
        imageName = 'vishnus5/demo'
        registryCredentialSet = 'dockerhub'
    }

    stages{

        stage('Clone Repo'){
            git([url: 'https://github.com/vishnu721/demo.git', branch: 'main'])
        }

        stage('Build Docker Image'){
            steps{
                script{
                    dockerImage = docker.build(imageName)
                }
            }
        }

        stage('Push Docker Image'){
            steps{
                script{
                    docker.withRegistry('', registryCredentialSet){
                        dockerImage.push("$BUILD_NUMBER")
                        dockerImage.push('latest')
                    }
                }
            }
        }
    }
}