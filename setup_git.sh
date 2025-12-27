git init

cat > .gitignore <<EOL
__pycache__/
*.pyc
*.pyo
*.pyd
venv/
outputs/
*.csv
*.pkl
mlruns/
.vscode/
*.DS_Store
EOL

git add .
git commit -m "Initial commit: project structure, src, tests, workflow"

git branch -M main
git remote add origin https://github.com/<AkashGururaj>/heart-disease-mlops.git
git push -u origin main
