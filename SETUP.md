# DynamoDB Sample Project Setup Guide

This guide will walk you through setting up your development environment for the DynamoDB sample project.

## Prerequisites

Before starting, ensure you have the following installed:
- Python 3.10 or higher
- Git

## Step 1: Clone the Repository

Open your terminal and navigate to your desired project directory:

```bash
# Navigate to your projects directory
cd ~/projects  # or wherever you keep your code

# Clone the repository
git clone <repository-url> dynamodb_sample

# Navigate into the project directory
cd dynamodb_sample
```

## Step 2: Create and Activate Virtual Environment

Virtual environments isolate your project dependencies from your system Python installation.

### On Linux/macOS:

```bash
# Create virtual environment
python3 -m venv .env

# Activate the virtual environment
source .env/bin/activate

# Verify activation (you should see (.env) in your prompt)
which python
```

### On Windows:

```bash
# Create virtual environment
python -m venv .env

# Activate the virtual environment
.env\Scripts\activate

# Verify activation (you should see (.env) in your prompt)
where python
```

## Step 3: Install Dependencies

With your virtual environment activated, install the required packages:

```bash
# Install all dependencies from requirements.txt
pip install -r requirements.txt

# If you experience connection issues (especially on campus networks), 
# use the Tencent mirror for faster and more reliable downloads:
pip install -r requirements.txt -i https://mirrors.cloud.tencent.com/pypi/simple

# Alternatively, install boto3 specifically with the mirror:
pip install boto3 -i https://mirrors.cloud.tencent.com/pypi/simple

# Verify installation
pip list
```

You should see the following packages installed:
- boto3 (AWS SDK for Python)
- botocore (Low-level AWS service access)
- Additional supporting libraries

## Step 4: Configure AWS Credentials

The project requires AWS credentials to interact with DynamoDB. Create the AWS credentials file:

### Create AWS Credentials Directory and File

```bash
# Create .aws directory in your home folder
mkdir ~/.aws

# Create credentials file
touch ~/.aws/credentials
```

### Configure Credentials File

Edit the `~/.aws/credentials` file and add your AWS credentials:

**For Windows users:** There is a batch file uploaded on Canvas that will open the credentials file for you.

```ini
[default]
aws_access_key_id = YOUR_ACCESS_KEY_HERE
aws_secret_access_key = YOUR_SECRET_ACCESS_KEY_HERE

[profile_name]
aws_access_key_id = ANOTHER_ACCESS_KEY_HERE
aws_secret_access_key = ANOTHER_SECRET_ACCESS_KEY_HERE
```

### Create Config File (Optional)

Create `~/.aws/config` to set default region and output format:

```ini
[default]
region = us-east-1
output = json

[profile profile_name]
region = ap-southeast-1
output = json
```

### File Permissions (Linux/macOS)

Secure your credentials file:

```bash
chmod 600 ~/.aws/credentials
chmod 600 ~/.aws/config
```

## Step 5: Verify Setup

Test your setup by running the sample scripts:

```bash
# 1. Create the DynamoDB table
python music.py

# 2. Insert sample data
python insert_music.py

# 3. Query the data
python read_music.py
```

## Step 6: Deactivate Virtual Environment

When you're done working on the project:

```bash
# Deactivate the virtual environment
deactivate
```

## Troubleshooting

### Common Issues:

1. **"boto3 not found" error:**
   - Ensure your virtual environment is activated
   - Reinstall dependencies: `pip install -r requirements.txt`
   - Try with mirror: `pip install boto3 -i https://mirrors.cloud.tencent.com/pypi/simple`

2. **AWS credentials error:**
   - Verify credentials file exists: `ls ~/.aws/credentials`
   - Check file permissions and content format
   - Ensure IAM permissions for DynamoDB access

3. **Region mismatch errors:**
   - Ensure consistent regions across all Python files
   - Check your `~/.aws/config` file for default region

4. **Table already exists error:**
   - Delete existing table first or use a different table name
   - Check AWS Console to verify table status

5. **Credentials file not found:**
   - Verify the file path: `~/.aws/credentials`
   - On Windows, this translates to: `C:\Users\YourUsername\.aws\credentials`

6. **Pip connection timeout:**
   - Use the Tencent mirror: `pip install <package> -i https://mirrors.cloud.tencent.com/pypi/simple`
   - This is especially helpful on campus networks with restricted internet access

## Next Steps

Once your environment is set up:
1. Review the code comments in each Python file
2. Experiment with different query patterns
3. Try modifying the table schema
4. Explore additional DynamoDB features like Global Secondary Indexes
5. Practice with your own data sets

Remember to always work within your activated virtual environment to ensure consistent dependency management!
