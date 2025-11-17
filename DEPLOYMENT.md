# Deployment Guide

This document explains how to deploy the Elliott Andrew Archive website to production.

## Architecture

**Frontend (Next.js):** Vercel
**Backend (Node.js/Express):** Railway
**Database:** MongoDB Atlas (already configured)

---

## Quick Deploy (When Updates Are Ready)

**Since auto-deployment is configured, pushing to GitHub automatically deploys both services!**

### Option 1: Auto-Deploy (Recommended)
Changes are already pushed to GitHub, so deployment will happen automatically:

✓ **Frontend:** Vercel detects changes and auto-deploys (takes ~2-3 minutes)
✓ **Backend:** Railway detects changes and auto-deploys (takes ~1-2 minutes)

Check deployment status:
- **Vercel:** https://vercel.com/dashboard
- **Railway:** https://railway.app/dashboard

### Option 2: Manual Trigger (if needed)

**Frontend (Vercel Dashboard):**
1. Go to https://vercel.com
2. Select project: `elliottandrew-archive-frontend` (or your project name)
3. Click "Deployments" tab
4. Click "Redeploy" on latest deployment

**Backend (Railway Dashboard):**
1. Go to https://railway.app
2. Select project: `elliottandrew-archive-backend` (or your project name)
3. Click "Deployments" tab
4. Click "Deploy" or "Redeploy"

### Option 3: CLI Deploy (advanced)

**Frontend:**
```bash
cd frontend
npx vercel --prod
```

**Backend:**
```bash
cd backend
npx railway up
```
(Requires CLI tools installed: `npm install -g vercel @railway/cli`)

---

## Initial Setup (First Time Only)

### Frontend - Vercel Setup

1. **Install Vercel CLI** (if not already installed):
   ```bash
   npm install -g vercel
   ```

2. **Login to Vercel**:
   ```bash
   vercel login
   ```

3. **Deploy from frontend directory**:
   ```bash
   cd /Users/elliottandrew/Desktop/Operating/Systems/Creative Practice System/Website/elliottandrew-website/frontend
   vercel --prod
   ```

4. **Configure Project**:
   - Project name: `elliottandrew-archive-frontend`
   - Framework: Next.js (auto-detected)
   - Build command: `npm run build`
   - Output directory: `.next`
   - Install command: `npm install`

5. **Set Environment Variables** (if needed):
   ```bash
   vercel env add NEXT_PUBLIC_API_URL production
   # Enter: https://your-backend-url.railway.app
   ```

6. **Connect to GitHub** (for auto-deploy):
   - Vercel Dashboard → Project Settings → Git
   - Connect to `elliottandrew14/elliottandrew-archive-frontend`
   - Auto-deploys on push to main

### Backend - Railway Setup

1. **Install Railway CLI** (if not already installed):
   ```bash
   npm install -g @railway/cli
   ```

2. **Login to Railway**:
   ```bash
   railway login
   ```

3. **Initialize Railway project**:
   ```bash
   cd /Users/elliottandrew/Desktop/Operating/Systems/Creative Practice System/Website/elliottandrew-website/backend
   railway init
   ```

4. **Set Environment Variables**:
   ```bash
   railway variables set MONGODB_URI="mongodb+srv://..."
   railway variables set PORT=3001
   railway variables set NODE_ENV=production
   ```

5. **Deploy**:
   ```bash
   railway up
   ```

6. **Get Railway URL**:
   ```bash
   railway domain
   ```
   This will be something like: `https://elliottandrew-backend-production.up.railway.app`

7. **Update Frontend API URL**:
   - Go to Vercel dashboard
   - Add environment variable: `NEXT_PUBLIC_API_URL` = Railway backend URL
   - Redeploy frontend

---

## Environment Variables

### Frontend (Vercel)
```bash
NEXT_PUBLIC_API_URL=https://your-backend.railway.app
```

### Backend (Railway)
```bash
MONGODB_URI=mongodb+srv://username:password@cluster.mongodb.net/portfolio?retryWrites=true&w=majority
PORT=3001
NODE_ENV=production
```

---

## Deployment Checklist

Before deploying:
- [ ] All changes committed to git
- [ ] All changes pushed to GitHub
- [ ] Database updates applied (if any)
- [ ] Environment variables configured
- [ ] Local testing complete

Deploy:
- [ ] Backend deployed to Railway
- [ ] Frontend deployed to Vercel
- [ ] Test production URLs
- [ ] Check that API calls work
- [ ] Verify images load correctly
- [ ] Test cart functionality
- [ ] Check print purchases work

---

## URLs

**Production Frontend:** https://elliottandrew-archive-frontend.vercel.app (or custom domain)
**Production Backend:** https://elliottandrew-backend-production.up.railway.app
**MongoDB:** Already connected via MONGODB_URI

**Development:**
- Frontend: http://localhost:3000
- Backend: http://localhost:3001

---

## Troubleshooting

### Frontend Issues
- Check Vercel deployment logs: `vercel logs`
- Verify API URL environment variable is set
- Check build logs in Vercel dashboard

### Backend Issues
- Check Railway logs: `railway logs`
- Verify MongoDB connection string
- Check that PORT is set correctly
- Ensure all dependencies are in package.json (not devDependencies)

### CORS Issues
If frontend can't reach backend:
- Add frontend URL to CORS whitelist in `backend/server.js`
- Redeploy backend

---

## Custom Domain (Future)

### Frontend (elliottandrew.com)
1. Vercel Dashboard → Project → Settings → Domains
2. Add `elliottandrew.com` and `www.elliottandrew.com`
3. Update DNS records with your domain registrar:
   - Type: `CNAME`
   - Name: `@` or `www`
   - Value: `cname.vercel-dns.com`

### Backend (api.elliottandrew.com)
1. Railway Dashboard → Project → Settings → Domains
2. Add custom domain: `api.elliottandrew.com`
3. Update DNS records:
   - Type: `CNAME`
   - Name: `api`
   - Value: provided by Railway

---

## Auto-Deployment

Once connected to GitHub:

**Vercel** (Frontend):
- Automatically deploys on push to `main` branch
- Preview deployments on pull requests

**Railway** (Backend):
- Automatically deploys on push to `main` branch
- Can configure deploy triggers in dashboard

---

## Rollback

### Frontend (Vercel)
```bash
# List deployments
vercel ls

# Promote previous deployment
vercel promote [deployment-url]
```

Or use Vercel Dashboard → Deployments → Promote to Production

### Backend (Railway)
```bash
# View deployments
railway logs --deployment

# Rollback via dashboard
# Railway Dashboard → Deployments → Select previous → Redeploy
```

---

## Monitoring

### Vercel Analytics
- Automatically included
- View in Vercel Dashboard → Analytics

### Railway Metrics
- Railway Dashboard → Metrics
- Shows CPU, memory, requests

### Database
- MongoDB Atlas Dashboard → Metrics
- Shows connections, operations, storage

---

## Cost

**Vercel:** Free tier (plenty for this site)
**Railway:** ~$5-10/month (usage-based)
**MongoDB Atlas:** Free tier (512MB, sufficient for catalog)

**Total:** ~$5-10/month

---

## Notes

- Always push to GitHub before deploying
- Frontend deployment takes ~2 minutes
- Backend deployment takes ~1 minute
- Database changes are instant (no deployment needed)
- Session logs and scripts are NOT deployed (only code)

---

**Last Updated:** 2025-11-17
**Status:** Production deployment active
