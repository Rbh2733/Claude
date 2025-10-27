#!/usr/bin/env python3
"""
Example: 4-Tier Quantitative Stock Scoring System
Demonstrates scoring stocks across all 4 tiers with sample data
"""

from scoring_engine_4tier import ScoringEngine


def main():
    """Run example scoring for stocks across all 4 tiers"""

    engine = ScoringEngine()

    print("=" * 100)
    print("4-TIER QUANTITATIVE STOCK SCORING SYSTEM - DEMONSTRATION")
    print("=" * 100)
    print()

    # ========================================================================
    # TIER 1: MEGA-CAP CORE (>$200B) - Example: GOOGL
    # ========================================================================

    print("\n" + "=" * 100)
    print("TIER 1: MEGA-CAP CORE (>$200B)")
    print("Example: GOOGL (Alphabet Inc)")
    print("=" * 100)

    googl_data = {
        # Basic info
        'market_cap_billions': 1800,
        'beta': 1.1,

        # Valuation
        'pe_ratio': 22,
        'historical_pe_avg': 25,
        'fcf_yield_pct': 4.17,
        'peg_ratio': 1.4,

        # Quality
        'roic_pct': 24.08,
        'operating_margin_pct': 32.08,
        'margin_trend_bps_per_year': 150,
        'moat_bonuses': {
            'network_effects': True,
            'economies_of_scale': True
        },
        'earnings_beat_rate_pct': 83.3,
        'mgmt_bonuses': {
            'consistent_buybacks': True
        },
        'cash_conversion_ratio': 1.25,

        # Growth
        'revenue_cagr_3yr_pct': 11.86,
        'revenue_growth_recent_yoy_pct': 16,
        'eps_cagr_3yr_pct': 15,
        'tam_billions': 500,
        'market_share_pct': 15,
        'future_growth_bonuses': {},
        'analyst_forward_growth_pct': 12,

        # Momentum
        'return_12m_pct': 35.2,
        'spy_return_12m_pct': 25,
        'price': 140,
        'ma_50': 135,
        'ma_200': 125,

        # Financial Health
        'net_cash_billions': 100,
        'fcf_billions': 75,
        'capital_allocation_bonuses': {
            'buybacks_rnd_gt_10pct': True,
            'value_creating_ma': True
        }
    }

    result = engine.calculate_score("GOOGL", googl_data)
    print_stock_report(result)

    # ========================================================================
    # TIER 2: LARGE-CAP GROWTH ($50-200B) - Example: PLTR
    # ========================================================================

    print("\n" + "=" * 100)
    print("TIER 2: LARGE-CAP GROWTH ($50-200B)")
    print("Example: PLTR (Palantir Technologies)")
    print("=" * 100)

    pltr_data = {
        # Basic info
        'market_cap_billions': 65,
        'beta': 1.5,

        # Valuation
        'is_profitable': True,
        'forward_pe': 45,
        'ps_ratio': 22,
        'peg_ratio': 1.8,
        'revenue_growth_recent_yoy_pct': 30,
        'sector_median_pe': 35,

        # Quality
        'revenue_billions': 2.5,
        'is_gaap_profitable': True,
        'operating_margin_pct': 12,
        'gross_margin_pct': 80,
        'margin_trend_bps_per_year': 350,
        'is_saas': True,
        'nrr_pct': 125,
        'dollar_based_retention_pct': 108,
        'market_position_bonuses': {
            'top_1_or_2': True,
            'gaining_share': True
        },

        # Growth
        'revenue_growth_ttm_pct': 30,
        'years_of_25plus_growth': 3,
        'is_accelerating': False,
        'analyst_forward_growth_pct': 28,
        'eps_growth_pct': 42,
        'tam_billions': 119,
        'market_penetration_pct': 2.1,
        'growth_driver_bonuses': {
            'multiple_segments_20plus': True,
            'geographic_expansion': True
        },
        'business_type': 'software',

        # Momentum
        'return_6m_pct': 42,
        'qqq_return_6m_pct': 30,
        'price': 28,
        'ma_50': 26,
        'ma_200': 24,
        'institutional_bonuses': {
            'increasing_ownership': True
        },
        'analyst_momentum_bonuses': {
            'multiple_upgrades': True
        },

        # Scale & Moat
        'sector_avg_growth_pct': 18,
        'moat_development_bonuses': {
            'network_effects': True,
            'switching_costs': True
        },
        'partnership_bonuses': {
            'gov_contracts': True,
            'major_tech_partners': True
        }
    }

    result = engine.calculate_score("PLTR", pltr_data)
    print_stock_report(result)

    # ========================================================================
    # TIER 3: MID-CAP EMERGING ($10-50B) - Example: CRWD
    # ========================================================================

    print("\n" + "=" * 100)
    print("TIER 3: MID-CAP EMERGING ($10-50B)")
    print("Example: CRWD (CrowdStrike)")
    print("=" * 100)

    crwd_data = {
        # Basic info
        'market_cap_billions': 45,
        'beta': 1.8,

        # Valuation
        'ps_ratio': 28,
        'revenue_growth_ttm_pct': 38,
        'sector_median_ps': 20,
        'insider_ownership_pct': 18,
        'insider_bonuses': {},

        # Quality
        'revenue_billions': 3.2,
        'is_profitable': True,
        'operating_margin_pct': 13,
        'path_to_profit_months': 0,
        'profit_path_penalties': {},
        'gross_margin_pct': 72,
        'ltv_cac_ratio': 2.8,
        'is_saas': True,
        'nrr_pct': 118,

        # Growth
        'quarters_accelerating': 5,
        'analyst_forward_growth_pct': 35,
        'tam_billions': 60,
        'market_penetration_pct': 5.3,
        'growth_driver_bonuses': {
            'multiple_segments_25plus': True,
            'platform_effects': True
        },
        'business_type': 'software',

        # Momentum
        'return_6m_pct': 55,
        'iwm_return_6m_pct': 38,
        'analyst_momentum_bonuses': {
            'upgrades_3plus': True,
            'price_target_raises': True
        },
        'volume_change_pct': 40,
        'sentiment_positive': True,

        # Scale Inflection
        'sector_avg_growth_pct': 22,
        'margin_trend_bps_per_year': 350,
        'moat_formation_bonuses': {
            'network_effects': True,
            'switching_costs': True
        },
        'partnership_bonuses': {
            'major_tech_partners': True,
            'gov_enterprise': True
        }
    }

    result = engine.calculate_score("CRWD", crwd_data)
    print_stock_report(result)

    # ========================================================================
    # TIER 4: SMALL-CAP MOONSHOTS (<$10B) - Example: RKLB
    # ========================================================================

    print("\n" + "=" * 100)
    print("TIER 4: SMALL-CAP MOONSHOTS (<$10B)")
    print("Example: RKLB (Rocket Lab)")
    print("=" * 100)

    rklb_data = {
        # Basic info
        'market_cap_billions': 4.5,
        'beta': 2.4,

        # Valuation
        'ps_ratio': 45,
        'revenue_growth_ttm_pct': 85,
        'sector_median_ps': 25,
        'insider_ownership_pct': 22,
        'insider_bonuses': {
            'recent_buying': True
        },

        # Quality
        'gross_margin_pct': 65,
        'recurring_revenue_pct': 65,
        'nrr_pct': 112,
        'top_customer_concentration_pct': 15,
        'top_3_concentration_pct': 28,
        'ltv_cac_ratio': 2.5,
        'is_profitable': False,
        'path_to_profit_months': 18,
        'profit_path_penalties': {},

        # Growth
        'quarters_accelerating': 6,
        'tam_billions': 350,
        'market_penetration_pct': 1.2,
        'growth_driver_bonuses': {
            'platform_forming': True,
            'gov_enterprise_accelerating': True
        },
        'analyst_forward_growth_pct': 75,
        'catalyst_bonuses': {
            'major_launch_6mo': True,
            'partnership_expected': True
        },

        # Momentum
        'return_6m_pct': 95,
        'iwo_return_6m_pct': 45,
        'sentiment_bonuses': {
            'rising_mentions_bullish': True,
            'analyst_upgrades_3plus': True
        },
        'sentiment_penalties': {},
        'volume_change_pct': 80,

        # Disruption
        'disruption_type': 'attacking_100b_plus',
        'tech_moat_bonuses': {
            'proprietary_ai_ml': False,
            'unique_supply_chain': True,
            'first_mover_scale': True
        },
        'market_structure': 'oligopoly_forming'
    }

    result = engine.calculate_score("RKLB", rklb_data)
    print_stock_report(result)

    # ========================================================================
    # PORTFOLIO SUMMARY
    # ========================================================================

    print("\n" + "=" * 100)
    print("PORTFOLIO CONSTRUCTION EXAMPLE ($100,000)")
    print("=" * 100)

    portfolio_value = 100000

    # Example portfolio based on scores
    tier1_allocation = 0.45  # 45%
    tier2_allocation = 0.28  # 28%
    tier3_allocation = 0.15  # 15%
    tier4_allocation = 0.07  # 7%
    cash_allocation = 0.05  # 5%

    print(f"\nTier 1 (Mega-Cap Core): ${portfolio_value * tier1_allocation:,.0f} (45%)")
    print(f"  Example: GOOGL @ 8.5% = ${portfolio_value * 0.085:,.0f}")
    print(f"  Target: 4-6 positions at 8-10% each")

    print(f"\nTier 2 (Large-Cap Growth): ${portfolio_value * tier2_allocation:,.0f} (28%)")
    print(f"  Example: PLTR @ 4% = ${portfolio_value * 0.04:,.0f}")
    print(f"  Target: 4-6 positions at 5-7% each")

    print(f"\nTier 3 (Mid-Cap Emerging): ${portfolio_value * tier3_allocation:,.0f} (15%)")
    print(f"  Example: CRWD @ 2% = ${portfolio_value * 0.02:,.0f}")
    print(f"  Target: 4-5 positions at 3-4% each")

    print(f"\nTier 4 (Small-Cap Moonshots): ${portfolio_value * tier4_allocation:,.0f} (7%)")
    print(f"  Example: RKLB @ 1% = ${portfolio_value * 0.01:,.0f}")
    print(f"  Target: 3-5 positions at 1-2% each")
    print(f"  MANDATORY: -40% stop loss on all Tier 4 positions")

    print(f"\nCash Reserve: ${portfolio_value * cash_allocation:,.0f} (5%)")
    print(f"  For: Rebalancing, opportunities, protection")

    print("\n" + "=" * 100)
    print("KEY INSIGHTS FROM 4-TIER SYSTEM")
    print("=" * 100)

    print("""
1. PROGRESSIVE RISK MANAGEMENT:
   - Tier 1: Quality-focused (35% weight), lowest minimum score (60)
   - Tier 2: Growth-focused (32% weight), moderate minimum (65)
   - Tier 3: High growth emphasis (38% weight), higher minimum (67)
   - Tier 4: Hypergrowth focus (40% weight), highest minimum (70)

2. DYNAMIC POSITION SIZING:
   - Automatically adjusts for volatility (beta)
   - Higher beta = smaller position for same score
   - Encourages diversification across tiers

3. 2-QUARTER EXIT RULE:
   - Allows temporary weakness without panic selling
   - Enforces discipline on deteriorating positions
   - Exception: Tier 4 has immediate -40% stop loss

4. SECTOR-SPECIFIC ADJUSTMENTS:
   - Different benchmarks by tier (SPY, QQQ, IWM, IWO)
   - Industry-adjusted margins and multiples
   - SaaS vs non-SaaS customer metrics

5. BONUS STRUCTURE PREVENTS GAMING:
   - Bonuses add BEFORE capping at 100
   - Prevents over-weighting single strong metrics
   - Encourages well-rounded companies
    """)

    print("=" * 100)


def print_stock_report(result: dict):
    """Print formatted stock score report"""

    print(f"\nStock: {result['ticker']}")
    print(f"Market Cap: ${result['market_cap_billions']:.1f}B")
    print(f"Tier: {result['tier']} - {result['tier_name']}")
    print(f"Beta: {result['beta']:.2f}")
    print("-" * 100)

    print(f"\nCOMPOSITE SCORE: {result['composite_score']}/100 {result['stars']}")
    print(f"Rating: {result['rating']}")
    print(f"Recommended Position Size: {result['position_size_pct']}%")

    print(f"\nScore Analysis:")
    print(f"  Minimum Required: {result['min_score_for_tier']}")
    print(f"  Current Score: {result['composite_score']}")
    print(f"  Buffer: +{result['score_buffer']} points")

    if result['score_buffer'] < 5:
        print(f"  ⚠️  WARNING: Low buffer - monitor closely")
    elif result['score_buffer'] < 10:
        print(f"  ⚡ CAUTION: Moderate buffer - watch for deterioration")
    else:
        print(f"  ✓ HEALTHY: Strong buffer above minimum")

    print(f"\nComponent Breakdown:")
    for component, score in result['components'].items():
        print(f"  {component:20s}: {score:5.1f}/100")

    print("-" * 100)


if __name__ == "__main__":
    main()
