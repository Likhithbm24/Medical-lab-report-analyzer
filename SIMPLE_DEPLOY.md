# 🚀 SIMPLE DEPLOYMENT - This Will Work 100%

## ⚡ **Skip the render.yaml - Use Manual Deployment Instead**

The automated deployment isn't working, so let's do it manually step by step.

---

## 🎯 **STEP 1: Deploy Backend to Render (Manual Method)**

### **1. Go to Render Dashboard**

- **Click**: [https://dashboard.render.com](https://dashboard.render.com)
- **Sign up/Login** with your GitHub account

### **2. Create Backend Service**

1. **Click "New +"** → **"Web Service"**
2. **Connect GitHub** (if not already connected)
3. **Select Repository**: `Likhithbm24/Medical-lab-report-analyzer`
4. **Configure Service EXACTLY like this:**
   - **Name**: `medical-insights-backend`
   - **Environment**: `Python`
   - **Region**: `Oregon` (or closest to you)
   - **Branch**: `main`
   - **Root Directory**: `backend` ⚠️ **MUST SET THIS!**
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`
   - **Plan**: Free

### **3. Deploy Backend**

- **Click "Create Web Service"**
- **Wait 5-10 minutes** for deployment
- **Copy your backend URL** (e.g., `https://medical-insights-backend.onrender.com`)

---

## ⚡ **STEP 2: Deploy Frontend to Vercel**

### **1. Go to Vercel Dashboard**

- **Click**: [https://vercel.com](https://vercel.com)
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

## 🚨 **CRITICAL SETTING FOR RENDER**

**When creating the backend service in Render, you MUST set:**

- **Root Directory**: `backend`

**This tells Render to look in the backend folder for all files!**

**Without this setting, Render will look in the wrong place and fail!**

---

## ⏰ **Time Required: 15-20 minutes total**

- **Backend**: 5-10 minutes
- **Frontend**: 3-5 minutes
- **Testing**: 5 minutes

---

## 🔧 **Why This Manual Method Works**

- **No render.yaml issues**: We're setting everything manually
- **Direct control**: You can see exactly what's being set
- **Immediate feedback**: You'll know if something is wrong right away
- **Proven method**: This is how most people deploy successfully

---

**🚀 START NOW - Follow these steps exactly! 🌍✨**

**The key is setting Root Directory to `backend` in Render!**
