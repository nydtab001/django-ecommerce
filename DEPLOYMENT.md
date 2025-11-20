# Deploy Django E-commerce to Back4App

## Files Created for Deployment

1. **Dockerfile** - Container configuration
2. **.dockerignore** - Files to exclude from Docker build
3. **docker-compose.yml** - For local testing (optional)
4. **.env.example** - Example environment variables

## Prerequisites

- Back4App account
- Git repository (GitHub, GitLab, etc.)

## Deployment Steps

### 1. Update Environment Variables on Back4App

In your Back4App dashboard, go to App Settings > Environment Variables and add:

```
DJANGO_SECRET_KEY=<generate-a-secure-random-key>
DEBUG=False
ALLOWED_HOSTS=<your-app-name>.back4app.io
STRIPE_TEST_SECRET_KEY=<your-stripe-secret-key>
STRIPE_TEST_PUBLISHABLE_KEY=<your-stripe-publishable-key>
```

### 2. Push Your Code to Git

```bash
git add .
git commit -m "Add Docker configuration for Back4App deployment"
git push origin master
```

### 3. Connect to Back4App

1. Log in to Back4App
2. Create a new app or select existing app
3. Go to "App Settings" > "Server Settings"
4. Connect your Git repository
5. Select the branch (master/main)
6. Back4App will automatically detect the Dockerfile

### 4. Database Configuration (Optional)

If using PostgreSQL on Back4App:
- Add database connection string to environment variables
- Update settings.py to use DATABASE_URL

### 5. Test Locally with Docker (Optional)

```bash
# Build the Docker image
docker build -t django-ecommerce .

# Run with docker-compose
docker-compose up

# Or run directly
docker run -p 8000:8000 --env-file .env django-ecommerce
```

## Important Notes

- Static files are served using WhiteNoise (no need for separate CDN initially)
- Media files should be stored on cloud storage (AWS S3, Cloudinary) for production
- Make sure to set DEBUG=False in production
- Generate a strong SECRET_KEY for production
- Update ALLOWED_HOSTS with your Back4App domain

## Generate Secret Key

Run this in Python to generate a secure secret key:

```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

## Post-Deployment

After deployment, you may need to:
1. Run migrations (usually automatic)
2. Create a superuser for admin access
3. Configure custom domain (optional)
4. Set up SSL certificate (usually automatic on Back4App)
