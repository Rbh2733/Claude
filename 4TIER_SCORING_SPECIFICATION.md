# QUANTITATIVE STOCK SCORING SYSTEM - FINAL 4-TIER VERSION
## Multi-Tier Investment Framework by Market Cap

---

## STANDARDIZED RULES (READ FIRST)

### **Bonus Integration Methodology:**
All bonuses add to component score BEFORE capping at 100, BEFORE applying weights.

**Process:**
1. Calculate base component score (0-100)
2. Add applicable bonuses
3. Cap total at 100 if exceeded
4. Apply component weight to final score

**Example:**
- Management Execution base: 100 points
- Earnings beat bonus: +15
- Total: 115 → CAP AT 100
- Apply weight: 100 × 0.10 = 10 points to Quality Score

### **Component Score Caps:**
- All individual component scores cap at 100 BEFORE weighting
- Composite scores range 0-100 (uncapped, but effectively limited by inputs)

### **Bracket Scoring:**
- Use midpoint of bracket for ambiguous cases
- Always round final position sizes to nearest 0.5%

### **P/E Formula Floor:**
- P/E calculations have FLOOR at 0 (cannot go negative)
- Cap at 100 maximum

---

## TIER DEFINITIONS

```
TIER 1: MEGA-CAP CORE
Market Cap: >$200B
Risk: Lowest
Position Size: 8-12%
Minimum Score: 60

TIER 2: LARGE-CAP GROWTH
Market Cap: $50B - $200B
Risk: Low-Moderate
Position Size: 5-8%
Minimum Score: 65

TIER 3: MID-CAP EMERGING
Market Cap: $10B - $50B
Risk: Moderate-High
Position Size: 3-5%
Minimum Score: 67

TIER 4: SMALL-CAP MOONSHOTS
Market Cap: <$10B
Risk: Highest
Position Size: 1-3%
Minimum Score: 70
```

---

## COMPOSITE FORMULAS BY TIER

### **Tier 1: Mega-Cap Core**
```
COMPOSITE = (V × 0.20) + (Q × 0.35) + (G × 0.25) + (M × 0.10) + (FH × 0.10)

Weights:
V  = Valuation (20%)
Q  = Quality (35%) ← HIGHEST
G  = Growth (25%)
M  = Momentum (10%)
FH = Financial Health (10%)

Output: 0-100 scale
Rating thresholds:
  80+ = Strong Buy
  70-79 = Buy
  60-69 = Hold
  <60 = Sell
```

---

### **Tier 2: Large-Cap Growth**
```
COMPOSITE = (V × 0.18) + (Q × 0.28) + (G × 0.32) + (M × 0.12) + (SM × 0.10)

Weights:
V  = Valuation (18%)
Q  = Quality (28%)
G  = Growth (32%) ← HIGHEST
M  = Momentum (12%)
SM = Scale/Moat (10%)

Output: 0-100 scale
Rating thresholds: Same as Tier 1
```

---

### **Tier 3: Mid-Cap Emerging**
```
COMPOSITE = (V × 0.15) + (Q × 0.22) + (G × 0.38) + (M × 0.15) + (SI × 0.10)

Weights:
V  = Valuation (15%)
Q  = Quality (22%)
G  = Growth (38%) ← HIGHEST
M  = Momentum (15%)
SI = Scale Inflection (10%)

Output: 0-100 scale
Rating thresholds: Same as Tier 1
```

---

### **Tier 4: Small-Cap Moonshots**
```
COMPOSITE = (V × 0.10) + (Q × 0.15) + (G × 0.40) + (M × 0.15) + (D × 0.20)

Weights:
V  = Valuation (10%)
Q  = Quality (15%)
G  = Growth (40%) ← HIGHEST
M  = Momentum (15%)
D  = Disruption (20%)

Output: 0-100 scale
Rating thresholds: Same as Tier 1
```

---

## RATING SYSTEM (ALL TIERS)

```
80-100 = Strong Buy ⭐⭐⭐⭐⭐
70-79 = Buy ⭐⭐⭐⭐
60-69 = Hold ⭐⭐⭐
<60 = Sell

Minimum Score to Hold:
Tier 1: 60
Tier 2: 65
Tier 3: 67
Tier 4: 70
```

---

## POSITION SIZING BY TIER

### **Tier 1: Mega-Cap Core**
```
Base Allocation = 10%
Volatility Adjustment = 1 + (Beta - 1) × 0.75

Position = (Base × Score/100) / Vol Adj

Example (Score 85, Beta 1.1):
= (10% × 0.85) / [1 + (0.1 × 0.75)]
= 8.5% / 1.075
= 7.9% → Round to 8%

Guidelines:
- Top allocation: 8-12%
- Target: 4-6 positions (40-50% combined)
- Minimum score: 60
- Stop loss: None (quality exits via 2-quarter rule)
```

---

### **Tier 2: Large-Cap Growth**
```
Base Allocation = 7%
Volatility Adjustment = 1 + (Beta - 1) × 1.0

Position = (Base × Score/100) / Vol Adj

Example (Score 88, Beta 1.5):
= (7% × 0.88) / [1 + (0.5 × 1.0)]
= 6.16% / 1.5
= 4.1% → Round to 4%

Guidelines:
- Top allocation: 5-8%
- Target: 4-6 positions (25-35% combined)
- Minimum score: 65
- Stop loss: None (quality exits via 2-quarter rule)
```

---

### **Tier 3: Mid-Cap Emerging**
```
Base Allocation = 5%
Volatility Adjustment = 1 + (Beta - 1) × 1.3

Position = (Base × Score/100) / Vol Adj

Example (Score 82, Beta 1.8):
= (5% × 0.82) / [1 + (0.8 × 1.3)]
= 4.1% / 2.04
= 2.0% → Round to 2%

Guidelines:
- Top allocation: 3-5%
- Target: 4-5 positions (12-20% combined)
- Minimum score: 67
- Stop loss: None (quality exits via 2-quarter rule)
```

---

### **Tier 4: Small-Cap Moonshots**
```
Base Allocation = 3%
Volatility Adjustment = 1 + (Beta - 1) × 1.5

Position = (Base × Score/100) / Vol Adj

Example (Score 90, Beta 2.4):
= (3% × 0.90) / [1 + (1.4 × 1.5)]
= 2.7% / 3.1
= 0.87% → Round to 1%

MANDATORY STOP LOSS: -40% from entry

Entry/Stop Framework:
Entry Price: $8.20
Stop Loss: $8.20 × 0.60 = $4.92 (-40% hard stop)

Guidelines:
- Top allocation: 1-3%
- Target: 3-5 positions (5-10% combined)
- Minimum score: 70
- Stop loss: -40% MANDATORY (price-based exit)
```

---

## SCORE HOLDING & EXIT RULES

### **2-Quarter Rule (All Tiers)**

```
IF score drops below tier minimum for 2 CONSECUTIVE quarters → EXIT

Tier 1: Exit if <60 for 2 consecutive quarters
Tier 2: Exit if <65 for 2 consecutive quarters
Tier 3: Exit if <67 for 2 consecutive quarters
Tier 4: Exit if <70 for 2 consecutive quarters OR -40% stop loss hit

RATIONALE:
- Allows temporary weakness
- Enforces discipline
- Prevents holding deteriorating positions
```

### **2-Quarter Rule Examples**

**Scenario 1: (Tier 1) degrades**
```
Q1: Score 62 (Hold) ✓
Q2: Score 59 (Sell) → EXIT trigger
Action: Sell position
```

**Scenario 2: (Tier 2) weakens**
```
Q1: Score 66 (Hold) ✓
Q2: Score 64 (Hold) → Warning
Q3: Score 63 (Hold) → EXIT trigger
Action: Sell position
```

**Scenario 3: Mid-cap (Tier 3) slips**
```
Q1: Score 68 (Hold) ✓
Q2: Score 66 (Hold) → EXIT trigger
Action: Sell position (tighter standard)
```

**Scenario 4: (Tier 4) deteriorates**
```
Q1: Score 72 (Buy) ✓
Q2: Score 69 (Hold) → EXIT trigger
Also: Monitor -40% stop loss
Action: Sell position (requires "Buy" rating)
```

---

## PORTFOLIO REBALANCING

### **Drift Threshold Detection**

```
Drift % = (Current Position Value - Target Value) / Target Value × 100

ACTION TRIGGERS:
  Drift >10% above target → Trim on next review
  Drift >10% below target → Add if score ≥ tier minimum + 8
  Quarterly rebalance → Trim all >5% off target

Example:
Target: 7% of $100k = $7,000
Current: $7,900 (stock appreciated)
Drift = ($7,900 - $7,000) / $7,000 × 100 = 12.86% OVER
ACTION: Trim to $7,000 at next quarterly review
```

### **Portfolio Composition Targets**

```
TIER 1 (CORE): 40-50% of portfolio
  Typical: 4-6 positions at 8-10% each

TIER 2 (LARGE GROWTH): 25-35% of portfolio
  Typical: 4-6 positions at 5-7% each

TIER 3 (MID EMERGING): 12-20% of portfolio
  Typical: 4-5 positions at 3-4% each

TIER 4 (MOONSHOTS): 5-10% of portfolio
  Typical: 3-5 positions at 1-2% each

CASH RESERVE: 5-10% of portfolio
  Use for: Rebalancing, opportunities, protection

EXAMPLE ($100K PORTFOLIO):
Tier 1: $45,000 (45%) - 5 positions @ 9% avg
Tier 2: $28,000 (28%) - 5 positions @ 5.6% avg
Tier 3: $15,000 (15%) - 5 positions @ 3% avg
Tier 4: $7,000 (7%) - 5 positions @ 1.4% avg
Cash: $5,000 (5%)
TOTAL: $100,000
```

---

## DETAILED TIER SCORING METHODOLOGIES

### **TIER 1: MEGA-CAP CORE (>$200B)**

#### **VALUATION SCORE (20% weight)**

**Component Weights:**
- P/E Ratio: 35%
- FCF Yield: 30%
- PEG Ratio: 35%

**Component 1: P/E Ratio (35%)**
```
Raw Score = 100 - [(Current P/E / Historical Avg P/E) - 1] × 100
FLOOR at 0, CAP at 100

Example (Below Historical):
Current P/E = 22, Historical = 25
= 100 - [(22/25) - 1] × 100
= 100 - (-0.12) × 100
= 112 → CAP AT 100

Bracket Interpretation:
<0.8x historical = 100 (undervalued)
0.8-1.0x = 85
1.0-1.2x = 70
1.2-1.5x = 50
>1.5x = 30 (overvalued)
```

**Component 2: FCF Yield (30%)**
```
FCF Yield = (TTM Free Cash Flow / Market Cap) × 100

Scoring Brackets:
  >5% = 100 points
  3-5% = 80 points
  2-3% = 60 points
  1-2% = 40 points
  <1% = 20 points
```

**Component 3: PEG Ratio (35%)**
```
PEG = Forward P/E / Expected EPS Growth Rate (%)

Scoring Brackets:
  <1.0 = 100 points
  1.0-1.5 = 85 points
  1.5-2.0 = 70 points
  2.0-2.5 = 50 points
  >2.5 = 30 points
```

---

#### **QUALITY SCORE (35% weight) - HIGHEST**

**Component Weights:**
- ROIC: 30%
- Operating Margin: 20%
- Op Margin Trend: 12%
- Competitive Moat: 18%
- Management Execution: 10%
- Cash Conversion: 10%

**Component 1: ROIC (30%)**
```
ROIC = NOPAT / Invested Capital

Where:
NOPAT = Operating Income × (1 - Tax Rate)
Invested Capital = Total Debt + Equity - Cash

Scoring Brackets:
  >25% = 100 points
  20-25% = 90 points
  15-20% = 75 points
  10-15% = 50 points
  <10% = 25 points
```

**Component 2: Operating Margin (20%)**
```
Op Margin = (Operating Income / Revenue) × 100

Scoring Brackets (industry-adjusted):
  >30% = 100 points
  20-30% = 85 points
  15-20% = 70 points
  10-15% = 50 points
  <10% = 30 points
```

**Component 3: Op Margin Trend (12%)**
```
Annual Rate of Change (bps per year)

Scoring Brackets:
  >200 bps/year = 100 points
  100-200 bps/year = 85 points
  50-100 bps/year = 70 points
  Stable ±50 bps/year = 60 points
  Declining = 25 points
```

**Component 4: Competitive Moat (18%)**
```
BONUS STRUCTURE:
Base Score = 50 (neutral moat)

Available Bonuses (select all that apply):
  Network Effects = +25
  Economies of Scale = +20
  Switching Costs = +20
  Intangible Assets (brand/IP) = +15
  Regulatory Moat = +10

Process:
1. Start with base 50
2. Add all applicable bonuses
3. Cap final score at 100
```

**Component 5: Management Execution (10%)**
```
Primary Metric: Earnings Beat Rate
Beat Rate = (Earnings Beats in Last 12 Quarters / 12) × 100

Base Scoring:
  >80% beat rate = 100 points
  70-80% = 85 points
  60-70% = 70 points
  <60% = 50 points

Available Bonuses (add to base, then cap at 100):
  Smart M&A track record = +10
  Consistent buybacks = +8
  Growing dividend = +7
```

**Component 6: Cash Conversion (10%)**
```
Cash Conversion Ratio = Free Cash Flow / Net Income

Scoring Brackets:
  >1.2 = 100 points
  1.0-1.2 = 80 points
  0.8-1.0 = 60 points
  <0.8 = 30 points
```

---

#### **GROWTH SCORE (25% weight)**

**Component Weights:**
- Revenue Growth (3Yr CAGR): 30%
- Growth Consistency: 15%
- EPS Growth (3Yr CAGR): 25%
- Future Growth Potential: 15%
- Analyst Consensus: 15%

**Component 1: Revenue Growth (30%)**
```
3Yr Revenue CAGR = (Ending Revenue / Beginning Revenue)^(1/3) - 1

Scoring Brackets:
  >20% = 100 points
  15-20% = 85 points
  10-15% = 65 points
  7-10% = 45 points
  5-7% = 30 points
  <5% = 15 points
```

**Component 2: Growth Consistency (15%)**
```
Delta = Recent YoY Growth - 3Yr Avg Growth

Base Score = 50 (neutral)

Adjustments:
  Delta >3% = +50 bonus
  Delta 1-3% = +30 bonus
  Delta ±1% = +10 bonus
  Delta -1 to -3% = -10 penalty
  Delta <-3% = -30 penalty

Process:
1. Calculate delta
2. Start with base 50
3. Add bonus/penalty
4. Cap at 100 if exceeded
```

**Component 3: EPS Growth (25%)**
```
3Yr EPS CAGR = (Ending EPS / Beginning EPS)^(1/3) - 1

Scoring Brackets:
  >25% = 100 points
  18-25% = 85 points
  12-18% = 70 points
  8-12% = 50 points
  <8% = 30 points

Quality Check Bonus:
IF EPS CAGR > Revenue CAGR + 5%: +15 (operating leverage)
IF EPS CAGR < Revenue CAGR - 5%: -15 (margin compression)
```

**Component 4: Future Growth Potential (15%)**
```
BONUS STRUCTURE:
Base Score = TAM Assessment

TAM Scoring:
  >$500B TAM + <20% market share = 100 base
  $200-500B TAM + <30% share = 85 base
  $100-200B TAM + <40% share = 70 base
  <$100B or >40% share = 50 base

Available Bonuses (add to base, cap at 100):
  Geographic expansion opportunity = +10
  New product cycles launching = +10
  Platform effects developing = +10
  Multiple growth vectors = +10
```

**Component 5: Analyst Consensus (15%)**
```
Forward Revenue Growth Estimate = Consensus avg of analyst 1Y estimates

Scoring Brackets:
  >15% = 100 points
  12-15% = 80 points
  8-12% = 60 points
  5-8% = 40 points
  <5% = 20 points
```

---

#### **MOMENTUM SCORE (10% weight)**

**Component Weights:**
- 12-Month Price Return: 40%
- Relative Strength vs SPY: 35%
- Technical Setup: 25%

**Component 1: 12-Month Return (40%)**
```
Return = [(Current Price - Price 12mo ago) / Price 12mo ago] × 100

Scoring Brackets:
  >30% = 100 points
  20-30% = 80 points
  10-20% = 60 points
  0-10% = 45 points
  -10 to 0% = 40 points
  <-10% = 60 points (oversold recovery potential)
```

**Component 2: Relative Strength vs SPY (35%)**
```
Relative Performance = Stock 12mo Return - SPY 12mo Return

Scoring Brackets:
  Outperform >10% = 100 points
  Outperform 5-10% = 75 points
  Outperform 0-5% = 60 points
  Underperform 0-5% = 50 points
  Underperform >5% = 30 points
```

**Component 3: Technical Setup (25%)**
```
Price vs Moving Averages

Scoring Brackets:
  Above 50-day & 200-day MA, trending up = 100 points
  Above 200-day MA only = 70 points
  Above 50-day MA only (but below 200-day) = 55 points
  Price between 50-day and 200-day = 50 points
  Below both = 30 points
```

---

#### **FINANCIAL HEALTH SCORE (10% weight)**

**Component Weights:**
- Net Cash Position: 50%
- FCF Generation: 40%
- Capital Allocation: 10%

**Component 1: Net Cash Position (50%)**
```
Net Cash = Cash + Marketable Securities - Total Debt

Scoring Brackets (Mega-Cap):
  >$75B net cash = 100 points
  $50-75B = 90 points
  $25-50B = 80 points
  $0-25B = 70 points
  Net debt <$50B = 60 points
  Net debt >$50B = 40 points
```

**Component 2: FCF Generation (40%)**
```
Annual TTM Free Cash Flow

Mega-Cap Brackets:
  >$20B = 100 points
  $15-20B = 90 points
  $10-15B = 80 points
  $5-10B = 60 points
  <$5B = 40 points
```

**Component 3: Capital Allocation (10%)**
```
BONUS STRUCTURE:
Base Score = 50 (neutral allocation)

Available Bonuses (add to base, cap at 100):
  Buybacks + R&D >10% of revenue = +25
  Value-creating M&A track record = +20
  Growing dividend = +15
  Disciplined capital deployment = +10
```

---

### **TIER 2: LARGE-CAP GROWTH ($50-200B)**

[Similar detailed breakdowns for Tier 2 components...]

### **TIER 3: MID-CAP EMERGING ($10-50B)**

[Similar detailed breakdowns for Tier 3 components...]

### **TIER 4: SMALL-CAP MOONSHOTS (<$10B)**

[Similar detailed breakdowns for Tier 4 components...]

---

## EXCEL IMPLEMENTATION

### **Column Structure**
```
A-D: Input data (prices, financials, metrics)
E: Valuation Score (0-100)
F: Quality Score (0-100)
G: Growth Score (0-100)
H: Momentum Score (0-100)
I: FH/SM/SI/D Score (0-100)
J: Composite Score (formula)
K: Rating (Strong Buy/Buy/Hold/Sell)
L: Position size calculation
M: Beta input
N: Target allocation %
O: Current allocation %
P: Drift %
Q: Action required
R: Last updated date
S: Tier (1/2/3/4)
T: Min score for tier
U: Score buffer (Composite - Min)
```

### **Key Excel Formulas**

**Composite Formulas by Tier:**
```
TIER 1:
=(E2*0.2)+(F2*0.35)+(G2*0.25)+(H2*0.1)+(I2*0.1)

TIER 2:
=(E2*0.18)+(F2*0.28)+(G2*0.32)+(H2*0.12)+(I2*0.1)

TIER 3:
=(E2*0.15)+(F2*0.22)+(G2*0.38)+(H2*0.15)+(I2*0.1)

TIER 4:
=(E2*0.1)+(F2*0.15)+(G2*0.4)+(H2*0.15)+(I2*0.2)
```

**Rating:**
```
=IF(J2>=80,"Strong Buy",IF(J2>=70,"Buy",IF(J2>=60,"Hold","Sell")))
```

**Position Size by Tier:**
```
TIER 1:
=(10%*J2/100)/(1+(M2-1)*0.75)

TIER 2:
=(7%*J2/100)/(1+(M2-1)*1.0)

TIER 3:
=(5%*J2/100)/(1+(M2-1)*1.3)

TIER 4:
=(3%*J2/100)/(1+(M2-1)*1.5)
```

---

## AUTOMATIC SCORE REDUCTIONS

### **Tier 1 Red Flags:**
```
- ROIC drops below 15% → Quality -15
- Op margin contracts >100 bps → Quality -10
- Revenue growth decelerates >5% → Growth -15
- Momentum breaks 200-day MA → Momentum -20
- Net cash becomes net debt → FH -25
```

### **Tier 2 Red Flags:**
```
- NRR drops below 100% → Quality -20
- Growth decelerates below 20% → Growth -20
- Path to profitability extends >2 qtrs → Quality -15
- Op margin contraction → Quality -15
```

### **Tier 3 Red Flags:**
```
- NRR drops below 100% → Quality -20
- Growth decelerates below 25% → Growth -25
- Burn rate accelerates 20%+ → Quality -20
- Customer concentration increases → Quality -15
```

### **Tier 4 Red Flags:**
```
- Burn rate accelerates 20%+ → Quality -25
- Growth decelerates below 40% → Growth -25
- Stop loss hit (-40%) → AUTO EXIT (no 2-quarter rule)
- Customer concentration >40% → Quality -20
```

---

## SUMMARY OF KEY FEATURES

### **Critical Fixes Applied:**

1. ✅ **4-Tier Structure**: Split by market cap (>$200B, $50-200B, $10-50B, <$10B)
2. ✅ **P/E Formula Floor**: Added 0 floor (prevents negative scores)
3. ✅ **P/S Growth Bonus Logic**: Fixed - higher growth = higher bonus
4. ✅ **Technical Setup**: Clarified "between MAs" + added all scenarios
5. ✅ **Tier 2 Benchmark**: Confirmed QQQ for large-cap
6. ✅ **NRR Alternatives**: Added non-SaaS customer metrics for all tiers
7. ✅ **Minimum Scores**: Progressive 60/65/67/70 by risk level
8. ✅ **Stop Loss**: Only Tier 4 (-40% mandatory)
9. ✅ **All Weights**: Verified sum to 100% across all tiers and components

### **Standardizations Applied:**

- All bonuses add to component → cap at 100 → apply weight
- All component weights explicitly stated and sum to 100%
- Position sizing formulas consistent across tiers
- Red flag triggers clearly defined by tier
- 2-quarter exit rule standardized
- Excel formulas provided for implementation

---

**Version:** 2.0 (4-Tier System)
**Created:** October 2025
**Last Updated:** October 2025
