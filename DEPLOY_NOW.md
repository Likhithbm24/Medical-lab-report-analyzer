# 🚀 DEPLOY NOW - Follow These Steps Exactly

## ⚡ **IMMEDIATE ACTION REQUIRED - Deploy Both Services**

Your code is ready. Now follow these steps to make your app live:

---

## 🎯 **STEP 1: Deploy Backend to Render (DO THIS FIRST)**

### **1. Open Render Dashboard**
- **Click here**: [https://dashboard.render.com](https://dashboard.render.com)
- **Sign up/Login** with your GitHub account

### **2. Create Backend Service**
1. **Click "New +"** → **"Web Service"**
2. **Connect GitHub** (if not already connected)
3. **Select Repository**: `Likhithbm24/Medical-lab-report-analyzer`
4. **Configure Service:**
   - **Name**: `medical-insights-backend`
   - **Environment**: `Python`
   - **Region**: `Oregon` (or closest to you)
   - **Branch**: `main`
   - **Root Directory**: `backend` ⚠️ **IMPORTANT!**
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`
   - **Plan**: Free

### **3. Deploy Backend**
- **Click "Create Web Service"**
- **Wait 5-10 minutes** for deployment
- **Copy your backend URL** (e.g., `https://medical-insights-backend.onrender.com`)

---

## ⚡ **STEP 2: Deploy Frontend to Vercel (DO THIS SECOND)**

### **1. Open Vercel Dashboard**
- **Click here**: [https://vercel.com](https://vercel.com)
- **Sign up/Login** with your GitHub account

### **2. Import Project**
1. **Click "New Project"**
2. **Import Git Repository**: `Likhithbm24/Medical-lab-report-analyzer`
3. **Configure Project:**
   - **Framework Preset**: `Vite`
   - **Root Directory**: `frontend`
   - **Build Command**: `npm run build`
   - **Output Directory**: `dist`
   - **Install Command**: `npm install`

### **3. Set Environment Variable (CRITICAL!)**
**BEFORE clicking Deploy:**
- **Name**: `VITE_API_URL`
- **Value**: `https://your-backend-name.onrender.com` (paste your actual Render backend URL here)

### **4. Deploy Frontend**
- **Click "Deploy"**
- **Wait 3-5 minutes** for deployment
- **Copy your frontend URL** (e.g., `https://medical-insights-app.vercel.app`)

---

## 🧪 **STEP 3: Test Your Deployment**

### **Test Backend:**
- Visit: `https://your-backend-name.onrender.com/health`
- Should show: `{"status": "healthy", "service": "Medical Insights API"}`

### **Test Frontend:**
- Visit your frontend URL
- Upload a PDF file
- Verify it connects to your backend

---

## 🎉 **SUCCESS INDICATORS**

✅ **Backend**: Health check works  
✅ **Frontend**: Loads without errors  
✅ **File Upload**: Works and connects to backend  
✅ **Analysis**: Returns lab results  

---

## 🚨 **IF SOMETHING GOES WRONG**

1. **Check the logs** in both Render and Vercel dashboards
2. **Verify environment variable** is set correctly in Vercel
3. **Ensure backend is running** before testing frontend
4. **Wait for full deployment** (don't test too early)
5. **Make sure you set Root Directory to `backend`** in Render

---

## 📱 **Your App URLs After Deployment**

- **Backend**: `https://medical-insights-backend.onrender.com`
- **Frontend**: `https://medical-insights-app.vercel.app`
- **Health Check**: `https://medical-insights-backend.onrender.com/health`

---

## ⏰ **Time Required: 15-20 minutes total**

- **Backend**: 5-10 minutes
- **Frontend**: 3-5 minutes
- **Testing**: 5 minutes

---

## ⚠️ **CRITICAL SETTING FOR RENDER**

**When creating the backend service in Render, you MUST set:**
- **Root Directory**: `backend`

**This tells Render to look in the backend folder for all files!**

---

**🚀 START NOW - Your Medical Insights App will be live worldwide! 🌍✨**

**Follow the steps above exactly as written. Don't skip any step!**
