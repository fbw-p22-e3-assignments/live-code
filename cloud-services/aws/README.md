# Installing AWS CLI

**LINUX**

1. Download the installation file:

    ```
    curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
    ```

2. Unzip the installation folder:

    ```
    unzip awscliv2.zip
    ```

3. Install the CLI:

    ```
    sudo ./aws/install
    ```

4. Confirm installation:

    ```
    aws --version
    ```

**Windows**

1. Download and run the AWS CLI installer

    https://awscli.amazonaws.com/AWSCLIV2.msi

2. Confirm installation:

    ```
    aws --version
    ```

## Login to EC2 using the AWS CLI

1. Using instance ID and the private key file:

    ```
    aws ec2-instance-connect ssh --instance-id i-0639a984d5df0fbc1 --private-key-file pb-test-1.pem
    ```

## Login to EC2 using the SSH Client

1. Using the key pair

    ```
    ssh -i pb-test-1.pem root@ec2-52-59-195-202.eu-central-1.compute.amazonaws.com
    ```