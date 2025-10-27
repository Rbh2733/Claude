# 4-Tier Quantitative Stock Scoring System

A comprehensive, data-driven framework for scoring and sizing stock positions across 4 market cap tiers with progressive risk management.

---

## 🚀 Overview

The **4-Tier Quantitative Stock Scoring System** is an advanced investment framework that automatically scores stocks on a 0-100 scale and calculates optimal position sizes based on:

- **Market capitalization** (4 tiers: >$200B, $50-200B, $10-50B, <$10B)
- **Company quality metrics** (profitability, margins, moats, management)
- **Growth characteristics** (revenue growth, TAM penetration, acceleration)
- **Valuation multiples** (P/E, P/S, PEG, FCF yield)
- **Momentum indicators** (price action, relative strength, technical setup)
- **Risk-adjusted sizing** (beta adjustments by tier)

### **Key Features**

✅ **4 Market Cap Tiers** with different scoring weights and risk profiles
✅ **Progressive minimum scores** (60 → 65 → 67 → 70) enforcing discipline
✅ **Beta-adjusted position sizing** automatically scales for volatility
✅ **2-quarter exit rule** prevents holding deteriorating positions
✅ **Mandatory -40% stop loss** on Tier 4 (small-cap moonshots)
✅ **Comprehensive scoring engine** with 40+ sub-components
✅ **Bonus structures** prevent gaming and encourage well-rounded companies

---

## 📊 The 4 Tiers

### **Tier 1: Mega-Cap Core (>$200B)**
- **Focus:** Quality & Stability
- **Position Size:** 8-12%
- **Min Score:** 60
- **Portfolio Allocation:** 40-50%
- **Composite Weights:** Valuation 20%, **Quality 35%**, Growth 25%, Momentum 10%, Financial Health 10%
- **Benchmark:** SPY (S&P 500)
- **Examples:** GOOGL, MSFT, NVDA, AAPL, META

**Why Quality-Focused?**
Mega-caps are portfolio anchors. We prioritize ROIC, margins, moats, and cash generation over explosive growth.

---

### **Tier 2: Large-Cap Growth ($50-200B)**
- **Focus:** High Growth with Emerging Moats
- **Position Size:** 5-8%
- **Min Score:** 65
- **Portfolio Allocation:** 25-35%
- **Composite Weights:** Valuation 18%, Quality 28%, **Growth 32%**, Momentum 12%, Scale/Moat 10%
- **Benchmark:** QQQ (NASDAQ-100)
- **Examples:** PLTR, SNOW, DDOG, CRWD, NET

**Why Growth-Focused?**
These companies are scaling rapidly and building competitive advantages. We emphasize revenue growth and market share gains.

---

### **Tier 3: Mid-Cap Emerging ($10-50B)**
- **Focus:** Explosive Growth & Scale Inflection
- **Position Size:** 3-5%
- **Min Score:** 67
- **Portfolio Allocation:** 12-20%
- **Composite Weights:** Valuation 15%, Quality 22%, **Growth 38%**, Momentum 15%, Scale Inflection 10%
- **Benchmark:** IWM (Russell 2000)
- **Examples:** IONQ, RKLB, emerging SaaS/AI companies

**Why Hypergrowth-Focused?**
Mid-caps are at the inflection point where growth accelerates and operating leverage kicks in. Growth is paramount.

---

### **Tier 4: Small-Cap Moonshots (<$10B)**
- **Focus:** Disruption Potential & TAM
- **Position Size:** 1-3%
- **Min Score:** 70
- **Portfolio Allocation:** 5-10%
- **Composite Weights:** Valuation 10%, Quality 15%, **Growth 40%**, Momentum 15%, Disruption 20%
- **Benchmark:** IWO (Russell 2000 Growth)
- **Examples:** Early-stage space, quantum computing, frontier tech
- **⚠️ MANDATORY -40% STOP LOSS**

**Why Disruption-Focused?**
These are high-risk/high-reward plays on massive TAMs and paradigm shifts. We accept higher risk for asymmetric upside.

---

## 📈 Scoring Methodology

### **Composite Score Formula (Varies by Tier)**

Each stock gets a **0-100 composite score** based on 5 weighted components:

```
TIER 1: COMPOSITE = (V×0.20) + (Q×0.35) + (G×0.25) + (M×0.10) + (FH×0.10)
TIER 2: COMPOSITE = (V×0.18) + (Q×0.28) + (G×0.32) + (M×0.12) + (SM×0.10)
TIER 3: COMPOSITE = (V×0.15) + (Q×0.22) + (G×0.38) + (M×0.15) + (SI×0.10)
TIER 4: COMPOSITE = (V×0.10) + (Q×0.15) + (G×0.40) + (M×0.15) + (D×0.20)
```

Where:
- **V** = Valuation (P/E, FCF yield, PEG ratio)
- **Q** = Quality (ROIC, margins, moats, management)
- **G** = Growth (revenue/EPS CAGRs, TAM, consistency)
- **M** = Momentum (price returns, relative strength, technicals)
- **FH/SM/SI/D** = Financial Health / Scale & Moat / Scale Inflection / Disruption

### **Rating Thresholds (All Tiers)**

```
80-100 = Strong Buy ⭐⭐⭐⭐⭐
70-79  = Buy ⭐⭐⭐⭐
60-69  = Hold ⭐⭐⭐
<60    = Sell
```

### **Minimum Scores to Hold (Progressive by Risk)**

```
Tier 1 (Mega-Cap):   60 minimum
Tier 2 (Large-Cap):  65 minimum
Tier 3 (Mid-Cap):    67 minimum
Tier 4 (Small-Cap):  70 minimum
```

**Why Progressive?**
Higher-risk tiers require higher minimum scores. We won't hold speculative small-caps unless they score exceptionally well.

---

## 💰 Position Sizing

### **Beta-Adjusted Dynamic Sizing**

```python
Position = (Base_Allocation × Score/100) / Volatility_Adjustment

Where:
Base_Allocation = {10% (Tier 1), 7% (Tier 2), 5% (Tier 3), 3% (Tier 4)}
Volatility_Adjustment = 1 + (Beta - 1) × Vol_Multiplier

Vol_Multipliers by Tier:
Tier 1: 0.75
Tier 2: 1.00
Tier 3: 1.30
Tier 4: 1.50
```

### **Example: Tier 2 Stock with Score 88, Beta 1.5**

```
Position = (7% × 0.88) / [1 + (1.5 - 1) × 1.0]
         = 6.16% / 1.5
         = 4.1% → Round to 4%
```

**Key Insight:** Higher beta = smaller position for the same score. This automatically manages portfolio volatility.

---

## 🛡️ Risk Management

### **2-Quarter Exit Rule**

```
IF score drops below tier minimum for 2 CONSECUTIVE quarters → EXIT

Examples:
- Tier 1: Exit if <60 for Q1 AND Q2
- Tier 2: Exit if <65 for Q1 AND Q2
- Tier 3: Exit if <67 for Q1 AND Q2
- Tier 4: Exit if <70 for Q1 AND Q2 OR -40% stop loss hit
```

**Rationale:**
- Allows temporary weakness (earnings miss, macro headwinds)
- Enforces discipline on sustained deterioration
- Prevents "hold and hope" on broken theses

### **Tier 4: Mandatory -40% Stop Loss**

```
Entry Price: $8.20
Stop Loss: $8.20 × 0.60 = $4.92

IF price drops to $4.92 → AUTO EXIT (overrides 2-quarter rule)
```

**Why?**
Small-cap moonshots are the riskiest tier. A -40% loss locks in capital preservation while allowing normal volatility.

---

## 🔧 Implementation

### **Quick Start**

1. **Install Dependencies**
   ```bash
   pip install pandas numpy yfinance openpyxl
   ```

2. **Run Example Scoring**
   ```bash
   python3 example_4tier_scoring.py
   ```

3. **Score Your Own Stocks**
   ```python
   from scoring_engine_4tier import ScoringEngine

   engine = ScoringEngine()

   my_stock_data = {
       'market_cap_billions': 150,  # Determines tier automatically
       'beta': 1.3,
       'pe_ratio': 28,
       'revenue_growth_ttm_pct': 32,
       # ... (add all required metrics)
   }

   result = engine.calculate_score("TICKER", my_stock_data)
   print(f"Score: {result['composite_score']}")
   print(f"Position Size: {result['position_size_pct']}%")
   ```

### **Files Included**

```
scoring_engine_4tier.py          - Core scoring engine (all 4 tiers)
example_4tier_scoring.py         - Demonstration with sample stocks
4TIER_SCORING_SPECIFICATION.md   - Complete methodology documentation
README_4TIER.md                  - This file
```

---

## 📚 Detailed Component Scoring

### **Tier 1 (Mega-Cap) Example: Quality Score**

Quality is **35% of composite** (highest weight). Components:

1. **ROIC (30%):** >25% = 100 pts, 20-25% = 90 pts, 15-20% = 75 pts, etc.
2. **Operating Margin (20%):** >30% = 100 pts, 20-30% = 85 pts, etc.
3. **Op Margin Trend (12%):** >200 bps/yr expansion = 100 pts
4. **Competitive Moat (18%):** Base 50 + bonuses (network effects +25, economies of scale +20, etc.)
5. **Management Execution (10%):** Earnings beat rate >80% = 100 pts
6. **Cash Conversion (10%):** FCF/Net Income >1.2 = 100 pts

**All components cap at 100 BEFORE applying weights.**

Bonus Structure Example:
```
Moat Base: 50
+ Network Effects: +25
+ Economies of Scale: +20
Subtotal: 95 → Apply 18% weight → Contributes 17.1 to Quality Score
```

---

## 🎯 Portfolio Construction Example

### **$100,000 Portfolio**

```
TIER 1 (MEGA-CAP CORE): $45,000 (45%)
  GOOGL  8.5%  $8,500  (Score: 89.9, Rating: Strong Buy)
  MSFT   8.0%  $8,000  (Score: 85.3, Rating: Strong Buy)
  NVDA   9.0%  $9,000  (Score: 88.7, Rating: Strong Buy)
  AAPL   7.5%  $7,500  (Score: 82.1, Rating: Strong Buy)
  META   8.0%  $8,000  (Score: 84.5, Rating: Strong Buy)
  SUB: 41% (within 40-50% target)

TIER 2 (LARGE-CAP GROWTH): $28,000 (28%)
  PLTR   4.0%  $4,000  (Score: 89.0, Rating: Strong Buy)
  SNOW   5.5%  $5,500  (Score: 76.2, Rating: Buy)
  CRWD   6.0%  $6,000  (Score: 87.3, Rating: Strong Buy)
  DDOG   5.0%  $5,000  (Score: 78.9, Rating: Buy)
  NET    5.5%  $5,500  (Score: 81.2, Rating: Strong Buy)
  SUB: 26% (within 25-35% target)

TIER 3 (MID-CAP EMERGING): $15,000 (15%)
  IONQ   3.0%  $3,000  (Score: 72.5, Rating: Buy)
  RKLB   4.0%  $4,000  (Score: 84.8, Rating: Strong Buy)
  HOOD   3.5%  $3,500  (Score: 69.3, Rating: Hold)
  SOFI   3.0%  $3,000  (Score: 71.2, Rating: Buy)
  SUB: 13.5% (within 12-20% target)

TIER 4 (SMALL-CAP MOONSHOTS): $7,000 (7%)
  Ticker A   1.5%  $1,500  (Score: 75.2, Rating: Buy) [-40% stop: $X]
  Ticker B   2.0%  $2,000  (Score: 82.1, Rating: Strong Buy) [-40% stop: $Y]
  Ticker C   1.0%  $1,000  (Score: 71.3, Rating: Buy) [-40% stop: $Z]
  Ticker D   1.5%  $1,500  (Score: 78.5, Rating: Buy) [-40% stop: $W]
  SUB: 6% (within 5-10% target)

CASH RESERVE: $5,000 (5%)
  For rebalancing, opportunities, protection

TOTAL: $100,000
```

---

## 🔬 What Makes This System Unique?

### **1. Market Cap-Based Tier Assignment**

Most scoring systems treat all stocks the same. We recognize that:
- A $1.5T mega-cap should be judged on **quality and profitability**
- A $100B large-cap should be judged on **growth and scaling**
- A $30B mid-cap should be judged on **growth acceleration**
- A $5B small-cap should be judged on **TAM and disruption potential**

### **2. Progressive Minimum Scores**

We won't hold:
- A mega-cap scoring <60 (too low quality for a core holding)
- A large-cap scoring <65 (not growing fast enough)
- A mid-cap scoring <67 (missing inflection point)
- A small-cap scoring <70 (too risky for speculative bet)

### **3. Beta-Adjusted Position Sizing**

A stock with:
- **Beta 0.8 gets a LARGER position** (lower volatility = safer)
- **Beta 2.0 gets a SMALLER position** (higher volatility = riskier)

This automatically balances portfolio volatility without manual intervention.

### **4. Bonus Structures Prevent Gaming**

Instead of:
```
Moat Score = 100 if any moat exists
```

We use:
```
Moat Base = 50
+ Network Effects = +25
+ Switching Costs = +20
+ Scale Advantages = +20
→ Subtotal capped at 100
```

This encourages **multiple sources of competitive advantage** rather than one-trick ponies.

### **5. Non-SaaS Alternatives**

Many scoring systems only work for SaaS companies (NRR, CAC payback, etc.). We provide:
- **Customer retention alternatives** for hardware, semiconductors, fintech
- **Industry-adjusted margin brackets**
- **Sector-specific benchmarks**

---

## 📖 Documentation

- **[4TIER_SCORING_SPECIFICATION.md](4TIER_SCORING_SPECIFICATION.md)** - Complete methodology with all formulas
- **[example_4tier_scoring.py](example_4tier_scoring.py)** - Working examples across all 4 tiers
- **[scoring_engine_4tier.py](scoring_engine_4tier.py)** - Source code with detailed comments

---

## ⚠️ Important Disclaimers

### **This System is NOT:**

❌ **Financial Advice** - Always consult licensed professionals
❌ **A Black Box** - Read the specification to understand the methodology
❌ **Fully Automated** - Requires manual input of financial data and qualitative assessments
❌ **Infallible** - Markets are unpredictable; no system guarantees profits

### **This System IS:**

✅ **A Framework** for systematic, disciplined stock analysis
✅ **Transparent** with all formulas and logic documented
✅ **Flexible** - adjust weights and thresholds to your risk tolerance
✅ **Educational** - learn what metrics drive quality, growth, and value

### **Data Limitations:**

- Some metrics (NRR, TAM, moat assessment) require manual research
- Fundamentals update quarterly (after earnings)
- Price data has 15-minute delay (not real-time tick data)
- Analyst estimates vary by source

---

## 🚀 Getting Started Checklist

### **Week 1: Learn the System**
- [ ] Read `4TIER_SCORING_SPECIFICATION.md`
- [ ] Run `example_4tier_scoring.py`
- [ ] Compare scores to your own analysis

### **Week 2: Score Your Portfolio**
- [ ] Gather financial data for your holdings
- [ ] Calculate component scores manually
- [ ] Check if your positions meet tier minimums

### **Week 3: Implement Risk Management**
- [ ] Set position sizes based on scores and beta
- [ ] Implement 2-quarter exit rule tracking
- [ ] Set -40% stop losses on Tier 4 holdings

### **Week 4: Optimize**
- [ ] Track score changes over time
- [ ] Correlate scores with actual returns
- [ ] Adjust weights to match your risk tolerance

---

## 🤝 Contributing

This is an open framework. Suggested improvements:

- **Automation:** Fetch data from APIs (yfinance, Alpha Vantage, etc.)
- **Backtesting:** Historical score analysis vs. returns
- **Dashboards:** Web UI for portfolio monitoring
- **Alerts:** Email/Slack notifications when scores drop below minimums

---

## 📧 Support

For questions, suggestions, or bug reports:
- Create an issue in the GitHub repository
- Read the full specification document
- Check example code for usage patterns

---

## 🎉 Version History

### **Version 2.0 (Current - 4-Tier System)**
- ✅ Split into 4 market cap tiers (was 3)
- ✅ Progressive minimum scores (60/65/67/70)
- ✅ Beta-adjusted position sizing
- ✅ 2-quarter exit rule formalized
- ✅ Tier 4 mandatory -40% stop loss
- ✅ Comprehensive scoring engine with 40+ sub-components
- ✅ Non-SaaS customer retention alternatives

### **Version 1.0 (Legacy - 3-Tier System)**
- 3 tiers (Core, Emerging, Moonshots)
- Fixed position sizes
- Single minimum threshold (65)

---

**Happy Investing! 📈🚀**

*Remember: Discipline beats emotion. Systematic analysis beats gut feeling. Risk management beats hope.*

---

**Created:** October 2025
**Version:** 2.0 (4-Tier System)
**License:** MIT (Use at your own risk)
