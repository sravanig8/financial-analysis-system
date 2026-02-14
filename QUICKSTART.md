## 🚀 Quick Start - Run Web Interface

### Step 1: Verify Dependencies
```powershell
pip list | findstr streamlit
```
Should show: `streamlit`

### Step 2: Set API Keys (PowerShell)
```powershell
$env:GEMINI_API_KEY="AIzaSyAR9Gb-a1P4CdYuTIf_PXCBu6W8NJudLaM"
$env:GNEWS_API_KEY="your-gnews-key"  # Optional
```

### Step 3: Start Streamlit App
```powershell
streamlit run app.py
```

### Step 4: Analyze Stocks
- Browser opens automatically
- Enter stock symbol (e.g., AAPL, TSLA)
- Click "🔍 Analyze Stock"
- View results in tabs

### Access URL
If browser doesn't auto-open: `http://localhost:8501`

### Stop Server
Press `Ctrl+C` in PowerShell

## 📚 Documentation Files

- `README.md` - Full system documentation
- `STREAMLIT_GUIDE.md` - Web interface guide  
- `GNEWS_SETUP.md` - GNEWS API key setup
- `IMPLEMENTATION_SUMMARY.md` - What was added

## 🎯 Key Differences: CLI vs Web

**CLI (python main.py)** - For power users
- Terminal-based
- Text output
- Keyboard input

**Web (streamlit run app.py)** - For everyone
- Browser-based
- Visual results
- Simple interface

Both analyze the same way! Choose your preference.

---

Questions? Check the relevant documentation file above.
