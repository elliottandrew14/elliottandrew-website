# MongoDB Atlas Setup Guide

**Time Required:** ~10 minutes
**Cost:** Free (M0 tier: 512MB storage)

---

## Step 1: Create MongoDB Atlas Account

1. Go to: https://www.mongodb.com/cloud/atlas/register
2. Sign up with email or Google account
3. Choose **Free** tier (M0 Sandbox)
4. Verify email if needed

---

## Step 2: Create a Cluster

1. After login, click "Build a Database"
2. Choose **M0 FREE** tier
3. Select cloud provider and region:
   - Provider: AWS (recommended)
   - Region: Choose closest to you (e.g., us-east-1 or us-west-2)
4. Cluster Name: Keep default or name it "elliottandrew"
5. Click **Create**

Wait 3-5 minutes for cluster to deploy.

---

## Step 3: Create Database User

1. Click "Database Access" in left sidebar
2. Click "Add New Database User"
3. Authentication Method: **Password**
4. Username: `elliott` (or your choice)
5. Password: Click "Autogenerate Secure Password" (copy it!)
6. Database User Privileges: **Read and write to any database**
7. Click "Add User"

**SAVE THIS PASSWORD!** You'll need it for the connection string.

---

## Step 4: Allow Network Access

1. Click "Network Access" in left sidebar
2. Click "Add IP Address"
3. For development: Click "Allow Access from Anywhere" (0.0.0.0/0)
   - This is fine for testing
   - For production, whitelist specific IPs
4. Click "Confirm"

---

## Step 5: Get Connection String

1. Click "Database" in left sidebar
2. Click "Connect" button on your cluster
3. Choose "Connect your application"
4. Driver: **Node.js**
5. Version: **5.5 or later**
6. Copy the connection string

It looks like:
```
mongodb+srv://elliott:<password>@cluster0.xxxxx.mongodb.net/?retryWrites=true&w=majority
```

---

## Step 6: Save to .env File

Replace `<password>` with the password you copied in Step 3:

```
MONGODB_URI=mongodb+srv://elliott:YOUR_ACTUAL_PASSWORD@cluster0.xxxxx.mongodb.net/portfolio?retryWrites=true&w=majority
```

Note: I added `/portfolio` after `.net` to specify the database name.

Save this to: `/Volumes/2025/SynologyDrive/Operating/elliottandrew-website/backend/.env`

---

## Step 7: Create Database and Collection (Optional - Auto-created)

MongoDB will automatically create the database and collection when you first insert data.

But if you want to create manually:
1. Click "Browse Collections"
2. Click "Add My Own Data"
3. Database name: `portfolio`
4. Collection name: `creations`
5. Click "Create"

---

## Troubleshooting

**Can't connect:**
- Check password is correct (no < > symbols)
- Check IP address is whitelisted (0.0.0.0/0 for all)
- Check connection string has `/portfolio` after `.net`

**Cluster paused:**
- Free tier pauses after 60 days of inactivity
- Just click "Resume" to reactivate

**Storage limit:**
- Free tier: 512MB
- Current data: ~5-10MB for 73 creations
- Plenty of space!

---

## Next Steps

Once you have your `.env` file with the connection string:
1. The backend API will connect automatically
2. Run `website-sync` to upload your catalog data
3. Check MongoDB Atlas dashboard to see data appear

---

## Security Notes

**For Production:**
- Whitelist only necessary IP addresses
- Use strong password
- Rotate credentials periodically
- Enable 2FA on MongoDB Atlas account

**For Development:**
- Current setup (allow all IPs) is fine
- .env file is gitignored (won't be committed)

---

**Setup complete! Ready to build the backend.**
