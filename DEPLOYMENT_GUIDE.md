# 🚀 Deployment Guide for Medical Insights App

This guide will help you deploy your full-stack medical insights application to Render (backend) and Vercel (frontend).

## 📋 Prerequisites

- GitHub account with your code repository
- Render account (free tier available)
- Vercel account (free tier available)

## 🔧 Backend Deployment (Render)

### Step 1: Deploy Backend to Render

1. **Go to [Render.com](https://render.com)** and sign up/login
2. **Click "New +"** → **"Web Service"**
3. **Connect your GitHub repository**
4. **Configure the service:**

   - **Name**: `medical-insights-backend`
   - **Environment**: `Python 3`
   - **Build Command**: `cd backend && pip install -r requirements.txt`
   - **Start Command**: `cd backend && uvicorn main:app --host 0.0.0.0 --port $PORT`
   - **Plan**: Free

5. **Add Environment Variables:**

   - `PYTHON_VERSION`: `3.11.0`
   - `PORT`: `8000`
   - `CORS_ORIGIN`: `*`

6. **Click "Create Web Service"**

### Step 2: Get Backend URL

After deployment, note your backend URL:

- **Format**: `https://your-service-name.onrender.com`
- **Example**: `https://medical-insights-backend.onrender.com`

## 🌐 Frontend Deployment (Vercel)

### Step 1: Deploy Frontend to Vercel

1. **Go to [Vercel.com](https://vercel.com)** and sign up/login
2. **Click "New Project"**
3. **Import your GitHub repository**
4. **Configure the project:**

   - **Framework Preset**: Vite
   - **Root Directory**: `frontend`
   - **Build Command**: `npm run build`
   - **Output Directory**: `dist`
   - **Install Command**: `npm install`

5. **Add Environment Variable:**

   - **Name**: `VITE_API_URL`
   - **Value**: Your backend URL from Render (e.g., `https://medical-insights-backend.onrender.com`)

6. **Click "Deploy"**

### Step 2: Get Frontend URL

After deployment, note your frontend URL:

- **Format**: `https://your-project-name.vercel.app`

## 🔗 Update CORS Configuration

### Option 1: Update Backend CORS (Recommended)

1. Go to your Render dashboard
2. Navigate to your backend service
3. Go to "Environment" tab
4. Update `CORS_ORIGIN` to your Vercel frontend URL:
   ```
   https://your-project-name.vercel.app
   ```
5. Redeploy the service

### Option 2: Update Code and Redeploy

If you prefer to update the code:

1. Update `backend/main.py` line 25:

   ```python
   "https://your-project-name.vercel.app",  # Your Vercel frontend
   ```

2. Commit and push to GitHub
3. Render will automatically redeploy

## ✅ Testing Your Deployment

1. **Test Backend Health**: Visit `https://your-backend.onrender.com/health`
2. **Test Frontend**: Visit your Vercel URL
3. **Test File Upload**: Try uploading a PDF lab report

## 🚨 Troubleshooting

### Backend Issues

- Check Render logs for build errors
- Ensure all dependencies are in `requirements.txt`
- Verify Python version compatibility

### Frontend Issues

- Check Vercel build logs
- Ensure `VITE_API_URL` environment variable is set correctly
- Verify the backend URL is accessible

### CORS Issues

- Check browser console for CORS errors
- Verify CORS_ORIGIN is set correctly in Render
- Ensure backend is accessible from frontend

## 🔄 Updating Your App

- **Backend**: Push to GitHub → Render auto-deploys
- **Frontend**: Push to GitHub → Vercel auto-deploys

## 📱 Your App URLs

After deployment, you'll have:

- **Backend API**: `https://your-backend-name.onrender.com`
- **Frontend App**: `https://your-project-name.vercel.app`
- **API Docs**: `https://your-backend-name.onrender.com/docs`

## 🎉 Success!

Your medical insights app is now live and accessible worldwide! Users can upload lab reports and get AI-powered analysis through your deployed application.
