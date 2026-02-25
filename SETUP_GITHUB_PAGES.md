# Setting Up GitHub Pages for AI Behavioral Safety Studies Portfolio

## Enabling GitHub Pages

### Method 1: GitHub Web Interface (Recommended)
1. Go to your repository: https://github.com/febufenn-cyber/ai-behavioral-safety-studies
2. Click **Settings** (top right, gear icon)
3. In left sidebar, click **Pages**
4. Under **Source**, select:
   - **Branch**: `main`
   - **Folder**: `/docs`
5. Click **Save**
6. Wait 1-2 minutes for the site to deploy
7. Your site will be available at: `https://febufenn-cyber.github.io/ai-behavioral-safety-studies/`

### Method 2: GitHub CLI
```bash
# Enable Pages with docs folder as source
gh api --method POST \
  /repos/febufenn-cyber/ai-behavioral-safety-studies/pages \
  -f source='{"branch":"main","path":"/docs"}'

# Check Pages status
gh api /repos/febufenn-cyber/ai-behavioral-safety-studies/pages
```

### Method 3: GitHub API Directly
```bash
curl -X POST \
  -H "Authorization: token YOUR_GITHUB_TOKEN" \
  -H "Accept: application/vnd.github.v3+json" \
  https://api.github.com/repos/febufenn-cyber/ai-behavioral-safety-studies/pages \
  -d '{"source":{"branch":"main","path":"/docs"}}'
```

## Website Features

The `docs/index.html` file includes:
- **Professional portfolio overview**
- **Key findings summary**
- **Case study highlights**
- **Methodology overview**
- **Tools and evidence sections**
- **Responsive design** for all devices
- **GitHub integration** with direct links

## Customizing the Website

### Changing Content
Edit `docs/index.html`:
- Update header text in `<h1>` and `.subtitle` sections
- Modify card content in the `.container` sections
- Update footer information
- Change color scheme in CSS variables (`:root` section)

### Adding Pages
1. Create additional HTML files in `docs/` folder
2. Update navigation links in `index.html`
3. Ensure consistent styling by copying CSS

### Custom Domain (Optional)
1. In GitHub Pages settings, add your custom domain
2. Update CNAME file in `docs/` folder
3. Configure DNS with your domain provider

## Testing Locally
```bash
# Serve website locally
cd docs
python3 -m http.server 8000
# Open http://localhost:8000 in browser
```

## Troubleshooting

### Pages Not Deploying
- Check GitHub Actions tab for deployment logs
- Ensure `docs/index.html` exists and is valid HTML
- Verify repository is public (required for free GitHub Pages)

### 404 Errors
- Wait a few minutes after enabling Pages
- Clear browser cache
- Check URL is correct: `username.github.io/repository-name`

### Styling Issues
- Check browser console for errors (F12 → Console)
- Ensure CSS paths are correct
- Test on different browsers

## Advanced Features

### Google Analytics
Add to `docs/index.html` `<head>`:
```html
<script async src="https://www.googletagmanager.com/gtag/js?id=GA_MEASUREMENT_ID"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'GA_MEASUREMENT_ID');
</script>
```

### SEO Optimization
Add meta tags to `docs/index.html` `<head>`:
```html
<meta name="description" content="AI Behavioral Safety Studies Portfolio - Systematic evaluation of LLM behavioral patterns under social framing conditions">
<meta name="keywords" content="AI safety, red teaming, LLM, evaluation, portfolio, machine learning">
<meta property="og:title" content="AI Behavioral Safety Studies Portfolio">
<meta property="og:description" content="Systematic evaluation of LLM behavioral patterns with concrete evidence">
<meta property="og:image" content="https://febufenn-cyber.github.io/ai-behavioral-safety-studies/og-image.png">
```

## Maintenance

### Updating Content
1. Edit HTML/CSS files in `docs/`
2. Commit and push changes
3. GitHub Pages automatically redeploys

### Monitoring
- Check GitHub Pages build status in Actions tab
- Review website analytics if configured
- Regularly update portfolio with new findings

## Quick Commands
```bash
# Enable Pages
gh repo edit febufenn-cyber/ai-behavioral-safety-studies --enable-pages --pages-branch=main --pages-source=docs

# Disable Pages  
gh api --method DELETE /repos/febufenn-cyber/ai-behavioral-safety-studies/pages

# Get Pages status
gh api /repos/febufenn-cyber/ai-behavioral-safety-studies/pages | jq .status
```

---

*Last Updated: February 25, 2026*  
*GitHub Pages provides free hosting for project documentation and portfolios.*