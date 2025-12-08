# GitHub Pages Deployment Troubleshooting

## Issue
The book content is not showing on the GitHub Pages live site.

## Possible Causes and Solutions

### 1. Check GitHub Pages Settings

Go to your repository settings:
1. Navigate to: `https://github.com/Mehnazar/Physical-AI-Humanoid-Robotics/settings/pages`
2. Ensure **Source** is set to: **GitHub Actions** (NOT "Deploy from a branch")
3. If it says "Deploy from a branch", change it to "GitHub Actions"

### 2. Check GitHub Actions Workflow Status

1. Visit: `https://github.com/Mehnazar/Physical-AI-Humanoid-Robotics/actions`
2. Look for the "Deploy to GitHub Pages" workflow
3. Check if it's:
   - ✅ **Passing** (green checkmark) - Good!
   - ❌ **Failing** (red X) - Click on it to see error details
   - 🟡 **Running** (yellow dot) - Wait for it to complete

### 3. Verify Permissions

The workflow needs specific permissions. Check if these are set in your repository:

1. Go to: `https://github.com/Mehnazar/Physical-AI-Humanoid-Robotics/settings/actions`
2. Under "Workflow permissions", ensure:
   - ✅ **Read and write permissions** is selected
   - OR ensure the workflow has specific permissions (already set in `.github/workflows/deploy.yml`)

### 4. Manual Trigger

If automatic deployment isn't working:

1. Go to: `https://github.com/Mehnazar/Physical-AI-Humanoid-Robotics/actions/workflows/deploy.yml`
2. Click "Run workflow"
3. Select branch: `001-physical-ai-book`
4. Click "Run workflow" button

### 5. Check Build Logs

If the workflow is failing:

1. Click on the failed workflow run
2. Click on the "build" job
3. Look for error messages
4. Common issues:
   - Missing dependencies
   - Build errors
   - Broken links (we set this to 'warn' already)

### 6. Verify the Built Files

The build should create these files in `book/build/`:
- ✅ `index.html` - Main page
- ✅ `.nojekyll` - Tells GitHub Pages not to use Jekyll
- ✅ `assets/` - CSS and JS files
- ✅ `docs/` - Documentation pages

You can verify locally by running:
```bash
cd book
npm run build
ls build/
```

### 7. Test Locally

Before deploying, always test the production build locally:

```bash
cd book
npm run build
npm run serve
```

Then visit: `http://localhost:3000/Physical-AI-Humanoid-Robotics/`

The URL path must match the `baseUrl` in `docusaurus.config.ts`.

### 8. Check Base URL Configuration

In `book/docusaurus.config.ts`, verify:

```typescript
url: 'https://mehnazar.github.io',
baseUrl: '/Physical-AI-Humanoid-Robotics/',
```

These must match your GitHub Pages URL exactly.

### 9. Cache Issues

If you see old content:
1. Clear your browser cache (Ctrl+Shift+Delete)
2. Try incognito/private browsing mode
3. Wait 5-10 minutes for GitHub's CDN to update

### 10. Force Rebuild and Deploy

If all else fails, make a small change and push:

```bash
# Make a trivial change to trigger rebuild
echo "# Updated $(date)" >> book/README.md
git add book/README.md
git commit -m "Trigger deployment"
git push origin 001-physical-ai-book
```

## Expected GitHub Pages URL

Your live site should be at:
**https://mehnazar.github.io/Physical-AI-Humanoid-Robotics/**

## How to Check if Deployment is Working

1. **Visit the URL**: https://mehnazar.github.io/Physical-AI-Humanoid-Robotics/
2. **Check the environment**: https://github.com/Mehnazar/Physical-AI-Humanoid-Robotics/deployments
3. **View workflow runs**: https://github.com/Mehnazar/Physical-AI-Humanoid-Robotics/actions

## Common Error Messages and Fixes

### Error: "404 - Page Not Found"
- **Cause**: GitHub Pages not enabled or wrong source
- **Fix**: Go to Settings > Pages > Set source to "GitHub Actions"

### Error: "This site can't be reached"
- **Cause**: Deployment hasn't run yet or failed
- **Fix**: Check Actions tab for workflow status

### Error: "Blank page" or "Loading forever"
- **Cause**: Wrong baseUrl configuration
- **Fix**: Verify `baseUrl` in `docusaurus.config.ts` matches `/Physical-AI-Humanoid-Robotics/`

### Error: "CSS/JS not loading"
- **Cause**: Incorrect asset paths
- **Fix**: Ensure baseUrl is correct and files are in build output

## Quick Checklist

- [ ] GitHub Pages source is set to "GitHub Actions"
- [ ] Latest workflow run is successful (green checkmark)
- [ ] Repository has proper permissions for workflows
- [ ] Build locally succeeds: `npm run build`
- [ ] `baseUrl` matches repository name: `/Physical-AI-Humanoid-Robotics/`
- [ ] `.github/workflows/deploy.yml` exists and is correct
- [ ] Pushed latest changes to `001-physical-ai-book` branch
- [ ] Waited 2-5 minutes for deployment to complete
- [ ] Cleared browser cache

## Still Not Working?

1. Check repository visibility:
   - Public repositories: GitHub Pages is free
   - Private repositories: Requires GitHub Pro

2. Check if there's a CNAME file conflict (shouldn't be one for this setup)

3. Try deploying to `main` branch instead:
   - Update workflow to trigger on `main`
   - Merge `001-physical-ai-book` into `main`

## Contact Points

If you need more help:
- Check GitHub Pages status: https://www.githubstatus.com/
- Docusaurus deployment docs: https://docusaurus.io/docs/deployment
- GitHub Pages docs: https://docs.github.com/en/pages

---

**Last Updated**: December 8, 2025
