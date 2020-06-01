# devops-challange

step 1 : Install the jenkins using install_jenkins.sh file
         
         install_jenkins.sh file : 
          
                sudo apt update
                sudo apt install openjdk-8-jdk
                wget -q -O - https://pkg.jenkins.io/debian/jenkins-ci.org.key | sudo apt-key add -
                sudo sh -c 'echo deb http://pkg.jenkins.io/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list'
                sudo apt-get update
                sudo apt-get install jenkins

step 2 : Install the docker, ansible , python and pip on jenkins server using the following commands
         
         sudo apt-get install -y docker.io

         sudo apt-get install -y ansible

         sudo apt-get install -y python

         sudo apt-get install python3-pip

        ansible conf :

            cd /etc/ansible

            mkdir keys

            cd keys

            place the remote server ec2 private key here 

            vi chandu.pem

            save it  and give read permissions to the pem file using chmod 400 chandu.pem

            cd ..

            vi ansible.cfg

            do the following changes 

            remote_user = ubuntu

            private_key_file = /etc/ansible/keys/chandu.pem

            save it 

            vi hosts 

            place the remote server private ip here 

            save it 

            Now check the connection is established to ec2 using 

            ansible -m ping all 




step 3 : go to jenkins and select pipeline project and configure with the repo and call the Jenkinsfile

    
step 4 : Executing the terraform script and Installing the nginx in EC2 and confiuring reverse proxy

        Terraform commands : 

            terraform init

            terraform validate 

            terraform plan -var-file=terraform.tfvars  -out=outputs.json

            terraform apply "outputs.json"
        
        nginx conf :

            1. sudo apt-install -y nginx

            2. cd /etc/nginx/sites-available

            3. vi devops.challange

            server {
                listen 80;
                server_name <ip_addr_server>
            location / {
                proxy_pass http://127.0.0.1:8000;
            }
            }
            
            4. save it 

            5. ln -s /etc/nginx/sites-available/devops.challange /etc/nginx/sites-enables/devops.challange

            6. systemctl restart nginx

step 5 : Build a job 

         steps completed after a successful build 

         1 . Build suceess with BUILD_NUMBER

         2.  Created a docker image with the BUILD_NUMBER

         3.  Pushed the docker image to docker hub with the BUILD_NUMBER

         4.  Deployed the docker image with BUILD_NUMBER in ec2  and created the container from the pulled image 


         Commands used for docker : 

                1. docker build -t  rchandu3447/chandu-python:BUILD_NUMBER .

                2. docker login --username="username of docker hub" --password="dockerhub password" (need to configure credentials in jenkins)

                3. docker push rchandu3447/chandu-python:$BUILD_NUMBER

            Note 1 : I used a below command to up the container because if application is configured to listen to requests coming from its localhost the check depends on the server type
                   
                   docker run --name chandu-c1 --network host rchandu3447/chandu-python


step 6 : Accesss the endpoint
         
         ipddr/hello/name
    
      

