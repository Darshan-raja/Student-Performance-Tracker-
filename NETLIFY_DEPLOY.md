# 🚀 Netlify Deployment Guide

## ⚠️ Important Notes

**Netlify is NOT ideal for Flask applications** because:
- Netlify is designed for static sites and JAMstack apps
- Flask backend requires serverless functions (more complex)
- Database persistence is limited on Netlify's free tier
- Better options: Railway, Render, or Vercel

However, if you still want to try Netlify:

## Prerequisites

1. GitHub account
2. Netlify account (free tier)
3. Your code pushed to GitHub

## Deployment Steps

### 1. Push to GitHub
```bash
git add .
git commit -m "Add edit functionality and Netlify config"
git push origin main
```

### 2. Deploy on Netlify

#### Option A: Via Netlify Dashboard
1. Go to https://app.netlify.com
2. Click "Add new site" → "Import an existing project"
3. Connect your GitHub account
4. Select your repository
5. Build settings (should auto-detect from `netlify.toml`):
   - Build command: (auto-filled)
   - Publish directory: `.`
6. Click "Deploy site"

#### Option B: Via Netlify CLI
```bash
# Install Netlify CLI
npm install -g netlify-cli

# Login
netlify login

# Deploy
netlify deploy --prod
```

### 3. Configure Environment Variables
- Go to Site settings → Environment variables
- Add if needed:
  - `SECRET_KEY` (for Flask sessions)

### 4. Database Considerations

**Important**: Netlify's serverless functions have limitations:
- No persistent file storage (SQLite won't work reliably)
- Need to use external database (PostgreSQL, MongoDB)

For production, you should:
1. Use a managed PostgreSQL database (ElephantSQL, Supabase)
2. Update `database.py` to use `DATABASE_URL`
3. Add PostgreSQL URL as environment variable in Netlify

## Troubleshooting

### Build Fails
- Check Netlify build logs
- Ensure all dependencies are in `requirements.txt`
- Python version should be 3.11

### App Not Working
- Check function logs in Netlify dashboard
- Verify routes are working
- Check database connection

### Database Issues
- SQLite won't persist on Netlify
- Switch to PostgreSQL for production

## Recommended Alternative Platforms

Instead of Netlify, consider:

1. **Railway** (✅ Already deployed)
   - URL: https://web-production-da2c.up.railway.app
   - Best for Python/Flask
   - Free tier available

2. **Render**
   - Easy deployment
   - PostgreSQL support
   - Free tier available

3. **Vercel**
   - Great for frontend + serverless
   - Already configured with `vercel.json`

## Support

For issues:
- Check Netlify docs: https://docs.netlify.com/
- View deployment logs in Netlify dashboard
- Check serverless function logs
