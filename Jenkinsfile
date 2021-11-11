pipeline{
    agent any
    environment{
        imageName = 'vishnus5/demo'
        registryCredentialSet = 'dockerhub'
    }

    stages{

        stage('Clone Repo'){
            steps{
                echo 'Cloning repo'
                git([url: 'https://github.com/vishnu721/demo.git', branch: 'main'])
            }            
        }

        stage('Build Docker Image'){
            steps{
                echo 'Building the docker image'
                script{
                    dockerImage = docker.build(imageName)
                }
            }
        }

        stage('Push Docker Image'){
            steps{
                echo 'Pushing docker image to docker hub'
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