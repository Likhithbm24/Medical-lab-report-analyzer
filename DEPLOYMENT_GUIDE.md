# 🚀 Complete Deployment Guide - Render + Vercel

## 📋 Prerequisites
- GitHub repository: `Likhithbm24/Medical-lab-report-analyzer`
- All code pushed to GitHub ✅
- Render account (free)
- Vercel account (free)

---

## 🎯 **STEP 1: Deploy Backend to Render**

### **1.1 Go to Render Dashboard**
- Visit: [https://dashboard.render.com](https://dashboard.render.com)
- Sign up/Login with your GitHub account

### **1.2 Create Backend Service**
1. **Click "New +"** → **"Web Service"**
2. **Connect GitHub** (if not already connected)
3. **Select Repository**: `Likhithbm24/Medical-lab-report-analyzer`
4. **Configure Service:**
   - **Name**: `medical-insights-backend`
   - **Environment**: `Python`
   - **Region**: `Oregon` (or closest to you)
   - **Branch**: `main`
   - **Build Command**: `pip install -r backend/requirements.txt`
   - **Start Command**: `cd backend && uvicorn main:app --host 0.0.0.0 --port $PORT`
   - **Plan**: Free

### **1.3 Deploy Backend**
- Click **"Create Web Service"**
- Wait for build and deployment (5-10 minutes)
- **Save your backend URL** (e.g., `https://medical-insights-backend.onrender.com`)

### **1.4 Test Backend**
- Visit: `https://your-backend-name.onrender.com/health`
- Should return: `{"status": "healthy", "service": "Medical Insights API"}`

---

## ⚡ **STEP 2: Deploy Frontend to Vercel**

### **2.1 Go to Vercel Dashboard**
- Visit: [https://vercel.com](https://vercel.com)
- Sign up/Login with your GitHub account

### **2.2 Import Project**
1. **Click "New Project"**
2. **Import Git Repository**: `Likhithbm24/Medical-lab-report-analyzer`
3. **Configure Project:**
   - **Framework Preset**: `Vite`
   - **Root Directory**: `frontend`
   - **Build Command**: `npm run build`
   - **Output Directory**: `dist`
   - **Install Command**: `npm install`

### **2.3 Set Environment Variables**
**BEFORE clicking Deploy, add this environment variable:**
- **Name**: `VITE_API_URL`
- **Value**: `https://your-backend-name.onrender.com` (replace with your actual Render backend URL)

### **2.4 Deploy Frontend**
- Click **"Deploy"**
- Wait for build and deployment (3-5 minutes)
- **Save your frontend URL** (e.g., `https://medical-insights-app.vercel.app`)

---

## 🔧 **STEP 3: Post-Deployment Configuration**

### **3.1 Test Complete Flow**
1. **Visit your frontend URL**
2. **Upload a PDF file**
3. **Verify it connects to your backend**
4. **Check if analysis works**

### **3.2 Update CORS if Needed**
If you get CORS errors, the backend is already configured for both platforms.

---

## 🚨 **TROUBLESHOOTING**

### **Backend Issues:**
- **Build fails**: Check if `requirements.txt` has all dependencies
- **Service won't start**: Verify start command is correct
- **Health check fails**: Check if `/health` endpoint exists

### **Frontend Issues:**
- **Build fails**: Ensure `vercel.json` is in `frontend` folder
- **API connection fails**: Verify `VITE_API_URL` environment variable
- **CORS errors**: Backend CORS is already configured

---

## 📱 **Expected URLs After Deployment**

- **Backend API**: `https://medical-insights-backend.onrender.com`
- **Frontend App**: `https://medical-insights-app.vercel.app`
- **API Health**: `https://medical-insights-backend.onrender.com/health`
- **API Docs**: `https://medical-insights-backend.onrender.com/docs`

---

## 🎉 **Success Indicators**

✅ **Backend**: Health check returns `{"status": "healthy"}`  
✅ **Frontend**: Loads without errors  
✅ **File Upload**: Works and connects to backend  
✅ **Analysis**: Returns lab results and interpretations  

---

## 🔄 **Automatic Deployments**

Both platforms will automatically redeploy when you push to GitHub:
- **Render**: Auto-deploys on `main` branch pushes
- **Vercel**: Auto-deploys on `main` branch pushes

---

## 📞 **Need Help?**

1. **Check logs** in both Render and Vercel dashboards
2. **Verify environment variables** are set correctly
3. **Ensure all files** are pushed to GitHub
4. **Test endpoints** individually

---

## 🎯 **Quick Commands for Testing**

```bash
# Test backend health
curl https://your-backend-name.onrender.com/health

# Test backend root
curl https://your-backend-name.onrender.com/

# Test frontend
curl https://your-frontend-name.vercel.app
```

---

**Your Medical Insights App will be live worldwide once both deployments are complete! 🌍✨**
