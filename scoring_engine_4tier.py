#!/usr/bin/env python3
"""
4-Tier Quantitative Stock Scoring System - Core Scoring Engine
Implements the complete scoring methodology across all 4 tiers
"""

import math
from typing import Dict, Any, Tuple, Optional


class ScoringEngine:
    """
    Core scoring engine for the 4-tier quantitative stock scoring system.
    Implements all component scoring methodologies with bonus structures.
    """

    # Tier definitions by market cap (in billions)
    TIER_DEFINITIONS = {
        1: {"name": "Mega-Cap Core", "min_cap": 200, "max_cap": float('inf'), "min_score": 60},
        2: {"name": "Large-Cap Growth", "min_cap": 50, "max_cap": 200, "min_score": 65},
        3: {"name": "Mid-Cap Emerging", "min_cap": 10, "max_cap": 50, "min_score": 67},
        4: {"name": "Small-Cap Moonshots", "min_cap": 0, "max_cap": 10, "min_score": 70}
    }

    # Composite weights by tier
    TIER_WEIGHTS = {
        1: {"V": 0.20, "Q": 0.35, "G": 0.25, "M": 0.10, "FH": 0.10},
        2: {"V": 0.18, "Q": 0.28, "G": 0.32, "M": 0.12, "SM": 0.10},
        3: {"V": 0.15, "Q": 0.22, "G": 0.38, "M": 0.15, "SI": 0.10},
        4: {"V": 0.10, "Q": 0.15, "G": 0.40, "M": 0.15, "D": 0.20}
    }

    @staticmethod
    def determine_tier(market_cap_billions: float) -> int:
        """Determine tier based on market cap"""
        if market_cap_billions >= 200:
            return 1
        elif market_cap_billions >= 50:
            return 2
        elif market_cap_billions >= 10:
            return 3
        else:
            return 4

    @staticmethod
    def cap_score(score: float, maximum: float = 100.0) -> float:
        """Cap a score at maximum (default 100)"""
        return min(score, maximum)

    @staticmethod
    def floor_score(score: float, minimum: float = 0.0) -> float:
        """Floor a score at minimum (default 0)"""
        return max(score, minimum)

    @staticmethod
    def bracket_score(value: float, brackets: list) -> float:
        """
        Score based on bracket ranges.
        brackets = [(threshold, score), ...]
        Assumes descending thresholds
        """
        for threshold, score in brackets:
            if value >= threshold:
                return score
        return brackets[-1][1]

    # ============================================================================
    # TIER 1: MEGA-CAP CORE (>$200B)
    # ============================================================================

    def tier1_valuation(self, data: Dict[str, Any]) -> float:
        """
        Tier 1 Valuation Score (20% weight)
        Components: P/E Ratio (35%), FCF Yield (30%), PEG Ratio (35%)
        """
        # Component 1: P/E Ratio (35%)
        current_pe = data.get('pe_ratio', 0)
        historical_pe = data.get('historical_pe_avg', current_pe)

        if historical_pe > 0:
            pe_ratio_vs_hist = current_pe / historical_pe
            pe_score = 100 - ((pe_ratio_vs_hist - 1) * 100)
            pe_score = self.cap_score(self.floor_score(pe_score, 0), 100)
        else:
            pe_score = 50  # Neutral if no data

        # Component 2: FCF Yield (30%)
        fcf_yield = data.get('fcf_yield_pct', 0)
        fcf_brackets = [(5, 100), (3, 80), (2, 60), (1, 40), (0, 20)]
        fcf_score = self.bracket_score(fcf_yield, fcf_brackets)

        # Component 3: PEG Ratio (35%)
        peg_ratio = data.get('peg_ratio', 999)
        peg_brackets = [(0, 100), (1.0, 100), (1.5, 85), (2.0, 70), (2.5, 50), (0, 30)]
        peg_brackets_reversed = [(1.0, 100), (1.5, 85), (2.0, 70), (2.5, 50)]

        if peg_ratio < 1.0:
            peg_score = 100
        else:
            peg_score = 30
            for threshold, score in peg_brackets_reversed:
                if peg_ratio <= threshold:
                    peg_score = score
                    break

        # Weighted average
        valuation_score = (pe_score * 0.35) + (fcf_score * 0.30) + (peg_score * 0.35)
        return round(valuation_score, 2)

    def tier1_quality(self, data: Dict[str, Any]) -> float:
        """
        Tier 1 Quality Score (35% weight - HIGHEST)
        Components: ROIC (30%), Op Margin (20%), Op Margin Trend (12%),
                   Moat (18%), Mgmt Execution (10%), Cash Conversion (10%)
        """
        # Component 1: ROIC (30%)
        roic = data.get('roic_pct', 0)
        roic_brackets = [(25, 100), (20, 90), (15, 75), (10, 50), (0, 25)]
        roic_score = self.bracket_score(roic, roic_brackets)

        # Component 2: Operating Margin (20%)
        op_margin = data.get('operating_margin_pct', 0)
        op_margin_brackets = [(30, 100), (20, 85), (15, 70), (10, 50), (0, 30)]
        op_margin_score = self.bracket_score(op_margin, op_margin_brackets)

        # Component 3: Op Margin Trend (12%)
        margin_trend_bps = data.get('margin_trend_bps_per_year', 0)
        margin_trend_brackets = [(200, 100), (100, 85), (50, 70), (-50, 60), (-999, 25)]
        margin_trend_score = self.bracket_score(margin_trend_bps, margin_trend_brackets)

        # Component 4: Competitive Moat (18%)
        moat_base = 50
        moat_bonuses = data.get('moat_bonuses', {})
        moat_score = moat_base
        if moat_bonuses.get('network_effects', False):
            moat_score += 25
        if moat_bonuses.get('economies_of_scale', False):
            moat_score += 20
        if moat_bonuses.get('switching_costs', False):
            moat_score += 20
        if moat_bonuses.get('intangible_assets', False):
            moat_score += 15
        if moat_bonuses.get('regulatory_moat', False):
            moat_score += 10
        moat_score = self.cap_score(moat_score, 100)

        # Component 5: Management Execution (10%)
        earnings_beat_rate = data.get('earnings_beat_rate_pct', 50)
        if earnings_beat_rate > 80:
            mgmt_base = 100
        elif earnings_beat_rate >= 70:
            mgmt_base = 85
        elif earnings_beat_rate >= 60:
            mgmt_base = 70
        else:
            mgmt_base = 50

        mgmt_bonuses = data.get('mgmt_bonuses', {})
        mgmt_score = mgmt_base
        if mgmt_bonuses.get('smart_ma', False):
            mgmt_score += 10
        if mgmt_bonuses.get('consistent_buybacks', False):
            mgmt_score += 8
        if mgmt_bonuses.get('growing_dividend', False):
            mgmt_score += 7
        mgmt_score = self.cap_score(mgmt_score, 100)

        # Component 6: Cash Conversion (10%)
        cash_conversion_ratio = data.get('cash_conversion_ratio', 0)
        cash_brackets = [(1.2, 100), (1.0, 80), (0.8, 60), (0, 30)]
        cash_conv_score = self.bracket_score(cash_conversion_ratio, cash_brackets)

        # Weighted average
        quality_score = (
            (roic_score * 0.30) +
            (op_margin_score * 0.20) +
            (margin_trend_score * 0.12) +
            (moat_score * 0.18) +
            (mgmt_score * 0.10) +
            (cash_conv_score * 0.10)
        )
        return round(quality_score, 2)

    def tier1_growth(self, data: Dict[str, Any]) -> float:
        """
        Tier 1 Growth Score (25% weight)
        Components: Revenue Growth (30%), Growth Consistency (15%),
                   EPS Growth (25%), Future Growth (15%), Analyst Consensus (15%)
        """
        # Component 1: Revenue Growth 3Yr CAGR (30%)
        rev_cagr = data.get('revenue_cagr_3yr_pct', 0)
        rev_brackets = [(20, 100), (15, 85), (10, 65), (7, 45), (5, 30), (0, 15)]
        rev_growth_score = self.bracket_score(rev_cagr, rev_brackets)

        # Component 2: Growth Consistency (15%)
        consistency_base = 50
        recent_yoy = data.get('revenue_growth_recent_yoy_pct', 0)
        avg_3yr = data.get('revenue_cagr_3yr_pct', 0)
        delta = recent_yoy - avg_3yr

        if delta > 3:
            consistency_score = consistency_base + 50
        elif delta >= 1:
            consistency_score = consistency_base + 30
        elif abs(delta) <= 1:
            consistency_score = consistency_base + 10
        elif delta >= -3:
            consistency_score = consistency_base - 10
        else:
            consistency_score = consistency_base - 30
        consistency_score = self.cap_score(consistency_score, 100)

        # Component 3: EPS Growth 3Yr CAGR (25%)
        eps_cagr = data.get('eps_cagr_3yr_pct', 0)
        eps_brackets = [(25, 100), (18, 85), (12, 70), (8, 50), (0, 30)]
        eps_base_score = self.bracket_score(eps_cagr, eps_brackets)

        # Quality check bonus/penalty
        eps_score = eps_base_score
        if eps_cagr > rev_cagr + 5:
            eps_score += 15  # Operating leverage
        elif eps_cagr < rev_cagr - 5:
            eps_score -= 15  # Margin compression
        eps_score = self.cap_score(self.floor_score(eps_score, 0), 100)

        # Component 4: Future Growth Potential (15%)
        tam_billions = data.get('tam_billions', 0)
        market_share_pct = data.get('market_share_pct', 100)

        if tam_billions > 500 and market_share_pct < 20:
            future_base = 100
        elif tam_billions >= 200 and market_share_pct < 30:
            future_base = 85
        elif tam_billions >= 100 and market_share_pct < 40:
            future_base = 70
        else:
            future_base = 50

        future_bonuses = data.get('future_growth_bonuses', {})
        future_score = future_base
        if future_bonuses.get('geographic_expansion', False):
            future_score += 10
        if future_bonuses.get('new_product_cycles', False):
            future_score += 10
        if future_bonuses.get('platform_effects', False):
            future_score += 10
        if future_bonuses.get('multiple_growth_vectors', False):
            future_score += 10
        future_score = self.cap_score(future_score, 100)

        # Component 5: Analyst Consensus (15%)
        analyst_forward_growth = data.get('analyst_forward_growth_pct', 0)
        analyst_brackets = [(15, 100), (12, 80), (8, 60), (5, 40), (0, 20)]
        analyst_score = self.bracket_score(analyst_forward_growth, analyst_brackets)

        # Weighted average
        growth_score = (
            (rev_growth_score * 0.30) +
            (consistency_score * 0.15) +
            (eps_score * 0.25) +
            (future_score * 0.15) +
            (analyst_score * 0.15)
        )
        return round(growth_score, 2)

    def tier1_momentum(self, data: Dict[str, Any]) -> float:
        """
        Tier 1 Momentum Score (10% weight)
        Components: 12M Return (40%), Relative Strength vs SPY (35%), Technical (25%)
        """
        # Component 1: 12-Month Price Return (40%)
        return_12m = data.get('return_12m_pct', 0)
        return_brackets = [(30, 100), (20, 80), (10, 60), (0, 45), (-10, 40), (-999, 60)]
        if return_12m < -10:
            return_score = 60  # Oversold recovery potential
        else:
            return_score = self.bracket_score(return_12m, return_brackets[:-1])

        # Component 2: Relative Strength vs SPY (35%)
        stock_return = return_12m
        spy_return = data.get('spy_return_12m_pct', 0)
        rel_perf = stock_return - spy_return

        rel_brackets = [(10, 100), (5, 75), (0, 60), (-5, 50), (-999, 30)]
        rel_score = self.bracket_score(rel_perf, rel_brackets)

        # Component 3: Technical Setup (25%)
        price = data.get('price', 0)
        ma_50 = data.get('ma_50', 0)
        ma_200 = data.get('ma_200', 0)

        if price > ma_50 and price > ma_200:
            technical_score = 100
        elif price > ma_200:
            technical_score = 70
        elif price > ma_50:
            technical_score = 55
        elif ma_50 < price < ma_200:
            technical_score = 50
        else:
            technical_score = 30

        # Weighted average
        momentum_score = (
            (return_score * 0.40) +
            (rel_score * 0.35) +
            (technical_score * 0.25)
        )
        return round(momentum_score, 2)

    def tier1_financial_health(self, data: Dict[str, Any]) -> float:
        """
        Tier 1 Financial Health Score (10% weight)
        Components: Net Cash (50%), FCF Generation (40%), Capital Allocation (10%)
        """
        # Component 1: Net Cash Position (50%)
        net_cash_billions = data.get('net_cash_billions', 0)

        if net_cash_billions > 75:
            net_cash_score = 100
        elif net_cash_billions >= 50:
            net_cash_score = 90
        elif net_cash_billions >= 25:
            net_cash_score = 80
        elif net_cash_billions >= 0:
            net_cash_score = 70
        elif net_cash_billions >= -50:
            net_cash_score = 60
        else:
            net_cash_score = 40

        # Component 2: FCF Generation (40%)
        fcf_billions = data.get('fcf_billions', 0)
        fcf_brackets = [(20, 100), (15, 90), (10, 80), (5, 60), (0, 40)]
        fcf_score = self.bracket_score(fcf_billions, fcf_brackets)

        # Component 3: Capital Allocation (10%)
        cap_alloc_base = 50
        cap_alloc_bonuses = data.get('capital_allocation_bonuses', {})
        cap_alloc_score = cap_alloc_base
        if cap_alloc_bonuses.get('buybacks_rnd_gt_10pct', False):
            cap_alloc_score += 25
        if cap_alloc_bonuses.get('value_creating_ma', False):
            cap_alloc_score += 20
        if cap_alloc_bonuses.get('growing_dividend', False):
            cap_alloc_score += 15
        if cap_alloc_bonuses.get('disciplined_deployment', False):
            cap_alloc_score += 10
        cap_alloc_score = self.cap_score(cap_alloc_score, 100)

        # Weighted average
        fh_score = (
            (net_cash_score * 0.50) +
            (fcf_score * 0.40) +
            (cap_alloc_score * 0.10)
        )
        return round(fh_score, 2)

    def calculate_tier1_composite(self, data: Dict[str, Any]) -> Tuple[float, Dict[str, float]]:
        """Calculate Tier 1 composite score and component breakdown"""
        v_score = self.tier1_valuation(data)
        q_score = self.tier1_quality(data)
        g_score = self.tier1_growth(data)
        m_score = self.tier1_momentum(data)
        fh_score = self.tier1_financial_health(data)

        composite = (
            (v_score * 0.20) +
            (q_score * 0.35) +
            (g_score * 0.25) +
            (m_score * 0.10) +
            (fh_score * 0.10)
        )

        components = {
            "Valuation": v_score,
            "Quality": q_score,
            "Growth": g_score,
            "Momentum": m_score,
            "Financial_Health": fh_score
        }

        return round(composite, 2), components

    # ============================================================================
    # TIER 2: LARGE-CAP GROWTH ($50-200B)
    # ============================================================================

    def tier2_valuation(self, data: Dict[str, Any]) -> float:
        """
        Tier 2 Valuation Score (18% weight)
        Components: Forward P/E or P/S (55%), PEG (25%), Relative Valuation (20%)
        """
        # Component 1: Forward P/E or P/S (55%)
        is_profitable = data.get('is_profitable', True)

        if is_profitable:
            forward_pe = data.get('forward_pe', 999)
            pe_brackets = [(0, 100), (25, 100), (35, 85), (50, 70), (70, 50), (999, 35)]
            if forward_pe < 25:
                pe_ps_score = 100
            elif forward_pe < 35:
                pe_ps_score = 85
            elif forward_pe < 50:
                pe_ps_score = 70
            elif forward_pe < 70:
                pe_ps_score = 50
            else:
                pe_ps_score = 35
        else:
            # Use P/S for unprofitable
            ps_ratio = data.get('ps_ratio', 999)
            growth_rate = data.get('revenue_growth_recent_yoy_pct', 0)

            if ps_ratio < 8:
                pe_ps_score = 100
            elif ps_ratio < 12:
                pe_ps_score = 85
            elif ps_ratio < 18:
                pe_ps_score = 70
            elif ps_ratio < 25:
                pe_ps_score = 50
            elif ps_ratio < 35:
                pe_ps_score = 35
            else:
                pe_ps_score = 25

            # Growth context bonuses (NOTE: Higher growth = higher bonus)
            if growth_rate > 50 and ps_ratio > 35:
                pe_ps_score += 15
            elif growth_rate > 50 and 25 <= ps_ratio <= 35:
                pe_ps_score += 25
            elif growth_rate > 35 and 18 <= ps_ratio <= 25:
                pe_ps_score += 20

            pe_ps_score = self.cap_score(pe_ps_score, 100)

        # Component 2: PEG Ratio (25%)
        peg_ratio = data.get('peg_ratio', 999)
        if peg_ratio < 1.0:
            peg_score = 100
        elif peg_ratio < 1.5:
            peg_score = 85
        elif peg_ratio < 2.0:
            peg_score = 70
        elif peg_ratio < 2.5:
            peg_score = 50
        else:
            peg_score = 30

        # Component 3: Relative Valuation (20%)
        sector_median_pe = data.get('sector_median_pe', pe_ps_score)
        stock_pe = data.get('forward_pe', pe_ps_score)

        if stock_pe < sector_median_pe:
            rel_val_score = 100
        elif stock_pe <= sector_median_pe * 1.15:
            rel_val_score = 80
        elif stock_pe <= sector_median_pe * 1.30:
            rel_val_score = 60
        elif stock_pe <= sector_median_pe * 1.50:
            rel_val_score = 40
        else:
            rel_val_score = 20

        # Weighted average
        valuation_score = (
            (pe_ps_score * 0.55) +
            (peg_score * 0.25) +
            (rel_val_score * 0.20)
        )
        return round(valuation_score, 2)

    def tier2_quality(self, data: Dict[str, Any]) -> float:
        """
        Tier 2 Quality Score (28% weight)
        Components: Revenue Scale (15%), Profitability Status (18%), Gross Margin (20%),
                   Op Margin Trajectory (15%), Customer Retention (20%), Market Position (12%)
        """
        # Component 1: Revenue Scale (15%)
        revenue_billions = data.get('revenue_billions', 0)
        rev_scale_brackets = [(10, 100), (7, 90), (5, 80), (3, 70), (2, 60), (0, 45)]
        rev_scale_score = self.bracket_score(revenue_billions, rev_scale_brackets)

        # Component 2: Profitability Status (18%)
        is_gaap_profitable = data.get('is_gaap_profitable', False)
        op_margin = data.get('operating_margin_pct', 0)

        if is_gaap_profitable:
            if op_margin > 20:
                profit_score = 100
            elif op_margin >= 15:
                profit_score = 90
            elif op_margin >= 10:
                profit_score = 75
            elif op_margin >= 5:
                profit_score = 60
            else:
                profit_score = 50
        else:
            path_to_profit_quarters = data.get('path_to_profit_quarters', 999)
            if path_to_profit_quarters < 4:
                profit_score = 40
            elif path_to_profit_quarters < 8:
                profit_score = 30
            else:
                profit_score = 15

        # Component 3: Gross Margin (20%)
        gross_margin = data.get('gross_margin_pct', 0)

        if gross_margin > 75:
            gross_margin_score = 100
        elif gross_margin >= 65:
            gross_margin_score = 90
        elif gross_margin >= 55:
            gross_margin_score = 80
        elif gross_margin >= 45:
            gross_margin_score = 70
        elif gross_margin >= 35:
            gross_margin_score = 55
        else:
            gross_margin_score = 35

        # Component 4: Op Margin Trajectory (15%)
        margin_trend_bps = data.get('margin_trend_bps_per_year', 0)

        if margin_trend_bps > 300:
            margin_traj_score = 100
        elif margin_trend_bps >= 200:
            margin_traj_score = 90
        elif margin_trend_bps >= 100:
            margin_traj_score = 80
        elif margin_trend_bps >= 50:
            margin_traj_score = 65
        elif abs(margin_trend_bps) <= 50:
            margin_traj_score = 50
        else:
            margin_traj_score = 25

        # Component 5: Customer Retention (20%)
        is_saas = data.get('is_saas', False)

        if is_saas:
            nrr_pct = data.get('nrr_pct', 100)
            dbr_pct = data.get('dollar_based_retention_pct', 100)

            if nrr_pct > 130:
                retention_base = 100
            elif nrr_pct >= 120:
                retention_base = 90
            elif nrr_pct >= 110:
                retention_base = 80
            elif nrr_pct >= 100:
                retention_base = 65
            elif nrr_pct >= 90:
                retention_base = 45
            else:
                retention_base = 25

            retention_score = retention_base
            if dbr_pct > 105:
                retention_score += 15
            retention_score = self.cap_score(retention_score, 100)
        else:
            # Non-SaaS: Use best applicable metric
            repeat_revenue_pct = data.get('repeat_revenue_pct', 0)
            customer_churn_pct = data.get('customer_churn_pct', 100)
            customer_growth_pct = data.get('customer_growth_pct', 0)
            top_customer_concentration_pct = data.get('top_customer_concentration_pct', 100)

            # Try multiple metrics, use highest score
            scores = []

            # Option 1: Repeat Revenue
            if repeat_revenue_pct > 70:
                scores.append(100)
            elif repeat_revenue_pct >= 50:
                scores.append(80)
            elif repeat_revenue_pct >= 30:
                scores.append(60)
            else:
                scores.append(40)

            # Option 2: Churn
            if customer_churn_pct < 5:
                scores.append(100)
            elif customer_churn_pct < 10:
                scores.append(75)
            elif customer_churn_pct < 15:
                scores.append(50)
            else:
                scores.append(30)

            # Option 3: Customer Growth
            if customer_growth_pct > 25:
                scores.append(100)
            elif customer_growth_pct >= 15:
                scores.append(80)
            elif customer_growth_pct >= 5:
                scores.append(60)
            else:
                scores.append(40)

            # Option 4: Concentration
            if top_customer_concentration_pct < 10:
                scores.append(85)
            elif top_customer_concentration_pct < 20:
                scores.append(70)
            elif top_customer_concentration_pct < 30:
                scores.append(50)
            else:
                scores.append(25)

            retention_score = max(scores) if scores else 50

        # Component 6: Market Position (12%)
        market_pos_base = 50
        market_pos_bonuses = data.get('market_position_bonuses', {})
        market_pos_score = market_pos_base

        if market_pos_bonuses.get('top_1_or_2', False):
            market_pos_score += 35
        elif market_pos_bonuses.get('top_3_to_5', False):
            market_pos_score += 25
        if market_pos_bonuses.get('gaining_share', False):
            market_pos_score += 25
        if market_pos_bonuses.get('category_leader', False):
            market_pos_score += 30

        market_pos_score = self.cap_score(market_pos_score, 100)

        # Weighted average
        quality_score = (
            (rev_scale_score * 0.15) +
            (profit_score * 0.18) +
            (gross_margin_score * 0.20) +
            (margin_traj_score * 0.15) +
            (retention_score * 0.20) +
            (market_pos_score * 0.12)
        )
        return round(quality_score, 2)

    def tier2_growth(self, data: Dict[str, Any]) -> float:
        """
        Tier 2 Growth Score (32% weight - HIGHEST)
        Components: Revenue Growth (25%), Consistency (15%), Forward Estimates (20%),
                   EPS vs Revenue (10%), TAM (15%), Growth Drivers (10%), Cyclicality (5%)
        """
        # Component 1: Revenue Growth Rate (25%)
        ttm_growth = data.get('revenue_growth_ttm_pct', 0)

        if ttm_growth > 35:
            rev_growth_score = 100
        elif ttm_growth >= 28:
            rev_growth_score = 90
        elif ttm_growth >= 22:
            rev_growth_score = 80
        elif ttm_growth >= 18:
            rev_growth_score = 70
        elif ttm_growth >= 15:
            rev_growth_score = 55
        elif ttm_growth >= 12:
            rev_growth_score = 40
        else:
            rev_growth_score = 20

        # Component 2: Growth Consistency (15%)
        years_of_25plus_growth = data.get('years_of_25plus_growth', 0)
        is_accelerating = data.get('is_accelerating', False)

        if years_of_25plus_growth >= 3:
            consistency_score = 100
        elif years_of_25plus_growth == 2:
            consistency_score = 85
        elif is_accelerating:
            consistency_score = 80
        elif ttm_growth >= 20:
            consistency_score = 60
        else:
            consistency_score = 20

        # Component 3: Forward Growth Estimates (20%)
        forward_growth_estimate = data.get('analyst_forward_growth_pct', 0)
        current_growth = ttm_growth

        if forward_growth_estimate > 30:
            forward_base = 100
        elif forward_growth_estimate >= 25:
            forward_base = 85
        elif forward_growth_estimate >= 20:
            forward_base = 70
        elif forward_growth_estimate >= 15:
            forward_base = 55
        elif forward_growth_estimate >= 10:
            forward_base = 40
        else:
            forward_base = 20

        forward_score = forward_base
        if forward_growth_estimate > current_growth + 5:
            forward_score += 20
        forward_score = self.cap_score(forward_score, 100)

        # Component 4: EPS vs Revenue Growth (10%)
        eps_growth = data.get('eps_growth_pct', 0)
        rev_growth = ttm_growth
        eps_vs_rev_base = 50

        if eps_growth > rev_growth + 7:
            eps_vs_rev_score = eps_vs_rev_base + 50
        elif abs(eps_growth - rev_growth) <= 5:
            eps_vs_rev_score = eps_vs_rev_base + 20
        elif eps_growth < rev_growth - 5:
            eps_vs_rev_score = eps_vs_rev_base - 20
        else:
            eps_vs_rev_score = eps_vs_rev_base
        eps_vs_rev_score = self.cap_score(eps_vs_rev_score, 100)

        # Component 5: TAM & Penetration (15%)
        tam_billions = data.get('tam_billions', 0)
        penetration_pct = data.get('market_penetration_pct', 100)

        if tam_billions > 100 and penetration_pct < 10:
            tam_score = 100
        elif tam_billions >= 75 and penetration_pct < 12:
            tam_score = 90
        elif tam_billions >= 50 and penetration_pct < 15:
            tam_score = 80
        elif tam_billions >= 25 and penetration_pct < 20:
            tam_score = 65
        else:
            tam_score = 40

        # Component 6: Growth Drivers (10%)
        drivers_base = 50
        drivers_bonuses = data.get('growth_driver_bonuses', {})
        drivers_score = drivers_base

        if drivers_bonuses.get('multiple_segments_20plus', False):
            drivers_score += 25
        if drivers_bonuses.get('geographic_expansion', False):
            drivers_score += 15
        if drivers_bonuses.get('new_products', False):
            drivers_score += 15
        if drivers_bonuses.get('platform_effects', False):
            drivers_score += 15
        if drivers_bonuses.get('viral_network', False):
            drivers_score += 10

        drivers_score = self.cap_score(drivers_score, 100)

        # Component 7: Cyclicality Factor (5%)
        business_type = data.get('business_type', 'software')

        if business_type in ['software', 'saas']:
            cyclicality_score = 100
        elif business_type == 'early_mid_cycle':
            cyclicality_score = 85
        elif business_type == 'late_cycle_secular':
            cyclicality_score = 70
        elif business_type == 'peak_cycle':
            cyclicality_score = 40
        else:
            cyclicality_score = 20

        # Weighted average
        growth_score = (
            (rev_growth_score * 0.25) +
            (consistency_score * 0.15) +
            (forward_score * 0.20) +
            (eps_vs_rev_score * 0.10) +
            (tam_score * 0.15) +
            (drivers_score * 0.10) +
            (cyclicality_score * 0.05)
        )
        return round(growth_score, 2)

    def tier2_momentum(self, data: Dict[str, Any]) -> float:
        """
        Tier 2 Momentum Score (12% weight)
        Components: 6M Return (40%), Relative Strength vs QQQ (35%), Technical (25%)
        """
        # Component 1: 6-Month Price Performance (40%)
        return_6m = data.get('return_6m_pct', 0)

        if return_6m > 50:
            return_base = 100
        elif return_6m >= 35:
            return_base = 85
        elif return_6m >= 20:
            return_base = 70
        elif return_6m >= 10:
            return_base = 50
        elif return_6m >= 0:
            return_base = 40
        else:
            return_base = 60  # Oversold

        # Institutional flow bonuses
        inst_bonuses = data.get('institutional_bonuses', {})
        return_score = return_base
        if inst_bonuses.get('increasing_ownership', False):
            return_score += 15
        if inst_bonuses.get('smart_money', False):
            return_score += 10
        if inst_bonuses.get('insider_buying', False):
            return_score += 10
        return_score = self.cap_score(return_score, 100)

        # Component 2: Relative Strength vs QQQ (35%)
        qqq_return_6m = data.get('qqq_return_6m_pct', 0)
        rel_perf = return_6m - qqq_return_6m

        if rel_perf > 15:
            rel_base = 100
        elif rel_perf >= 8:
            rel_base = 80
        elif rel_perf >= 0:
            rel_base = 60
        elif rel_perf >= -8:
            rel_base = 45
        else:
            rel_base = 30

        # Analyst momentum bonuses
        analyst_bonuses = data.get('analyst_momentum_bonuses', {})
        rel_score = rel_base
        if analyst_bonuses.get('multiple_upgrades', False):
            rel_score += 15
        if analyst_bonuses.get('price_target_increases', False):
            rel_score += 10
        if analyst_bonuses.get('positive_revisions', False):
            rel_score += 10
        rel_score = self.cap_score(rel_score, 100)

        # Component 3: Technical Setup (25%)
        price = data.get('price', 0)
        ma_50 = data.get('ma_50', 0)
        ma_200 = data.get('ma_200', 0)

        if price > ma_50 and price > ma_200:
            technical_score = 100
        elif price > ma_200:
            technical_score = 70
        elif price > ma_50:
            technical_score = 55
        elif ma_50 < price < ma_200:
            technical_score = 50
        else:
            technical_score = 30

        # Weighted average
        momentum_score = (
            (return_score * 0.40) +
            (rel_score * 0.35) +
            (technical_score * 0.25)
        )
        return round(momentum_score, 2)

    def tier2_scale_moat(self, data: Dict[str, Any]) -> float:
        """
        Tier 2 Scale & Moat Score (10% weight)
        Components: Competitive Position (35%), Moat Development (30%),
                   Operating Leverage (20%), Strategic Partnerships (15%)
        """
        # Component 1: Competitive Position Evolution (35%)
        company_growth = data.get('revenue_growth_ttm_pct', 0)
        sector_growth = data.get('sector_avg_growth_pct', 0)

        if company_growth > sector_growth * 1.5:
            comp_pos_score = 100
        elif company_growth > sector_growth * 1.2:
            comp_pos_score = 80
        elif company_growth >= sector_growth:
            comp_pos_score = 60
        else:
            comp_pos_score = 30

        # Component 2: Moat Development (30%)
        moat_base = 50
        moat_bonuses = data.get('moat_development_bonuses', {})
        moat_score = moat_base

        if moat_bonuses.get('network_effects', False):
            moat_score += 30
        if moat_bonuses.get('switching_costs', False):
            moat_score += 25
        if moat_bonuses.get('economies_of_scale', False):
            moat_score += 20
        if moat_bonuses.get('brand_ecosystem', False):
            moat_score += 20
        if moat_bonuses.get('data_ip_moat', False):
            moat_score += 15

        moat_score = self.cap_score(moat_score, 100)

        # Component 3: Operating Leverage Inflection (20%)
        margin_expansion_bps = data.get('margin_trend_bps_per_year', 0)
        revenue_growth_pct = company_growth

        if margin_expansion_bps > revenue_growth_pct * 10:  # Rough proxy
            op_leverage_score = 100
        elif margin_expansion_bps > 0:
            op_leverage_score = 75
        elif margin_expansion_bps > -100:
            op_leverage_score = 50
        else:
            op_leverage_score = 30

        # Component 4: Strategic Partnerships (15%)
        partnership_base = 50
        partnership_bonuses = data.get('partnership_bonuses', {})
        partnership_score = partnership_base

        if partnership_bonuses.get('major_tech_partners', False):
            partnership_score += 25
        if partnership_bonuses.get('gov_contracts', False):
            partnership_score += 25
        if partnership_bonuses.get('ecosystem_integrations', False):
            partnership_score += 20
        if partnership_bonuses.get('strategic_customers', False):
            partnership_score += 15

        partnership_score = self.cap_score(partnership_score, 100)

        # Weighted average
        sm_score = (
            (comp_pos_score * 0.35) +
            (moat_score * 0.30) +
            (op_leverage_score * 0.20) +
            (partnership_score * 0.15)
        )
        return round(sm_score, 2)

    def calculate_tier2_composite(self, data: Dict[str, Any]) -> Tuple[float, Dict[str, float]]:
        """Calculate Tier 2 composite score and component breakdown"""
        v_score = self.tier2_valuation(data)
        q_score = self.tier2_quality(data)
        g_score = self.tier2_growth(data)
        m_score = self.tier2_momentum(data)
        sm_score = self.tier2_scale_moat(data)

        composite = (
            (v_score * 0.18) +
            (q_score * 0.28) +
            (g_score * 0.32) +
            (m_score * 0.12) +
            (sm_score * 0.10)
        )

        components = {
            "Valuation": v_score,
            "Quality": q_score,
            "Growth": g_score,
            "Momentum": m_score,
            "Scale_Moat": sm_score
        }

        return round(composite, 2), components

    # ============================================================================
    # TIER 3: MID-CAP EMERGING ($10-50B)
    # ============================================================================

    def tier3_valuation(self, data: Dict[str, Any]) -> float:
        """
        Tier 3 Valuation Score (15% weight)
        Components: P/S (60%), Relative Valuation (25%), Insider Ownership (15%)
        """
        # Component 1: Price-to-Sales (60%)
        ps_ratio = data.get('ps_ratio', 999)
        growth_rate = data.get('revenue_growth_ttm_pct', 0)

        if ps_ratio < 10:
            ps_base = 100
        elif ps_ratio < 15:
            ps_base = 85
        elif ps_ratio < 22:
            ps_base = 70
        elif ps_ratio < 30:
            ps_base = 55
        elif ps_ratio < 40:
            ps_base = 40
        else:
            ps_base = 30

        # Growth context bonuses
        ps_score = ps_base
        if growth_rate > 40 and 22 <= ps_ratio <= 30:
            ps_score += 25
        elif growth_rate > 50 and 30 <= ps_ratio <= 40:
            ps_score += 30
        elif growth_rate > 60 and ps_ratio > 40:
            ps_score += 20
        ps_score = self.cap_score(ps_score, 100)

        # Component 2: Relative Valuation (25%)
        sector_median_ps = data.get('sector_median_ps', ps_ratio)
        if ps_ratio < sector_median_ps:
            rel_val_score = 100
        elif ps_ratio <= sector_median_ps:
            rel_val_score = 75
        elif ps_ratio <= sector_median_ps * 1.5:
            rel_val_score = 60
        elif ps_ratio <= sector_median_ps * 2.0:
            rel_val_score = 40
        else:
            rel_val_score = 20

        # Component 3: Insider Ownership (15%)
        insider_ownership_pct = data.get('insider_ownership_pct', 0)

        if insider_ownership_pct > 20:
            insider_base = 100
        elif insider_ownership_pct >= 15:
            insider_base = 90
        elif insider_ownership_pct >= 10:
            insider_base = 75
        elif insider_ownership_pct >= 5:
            insider_base = 60
        else:
            insider_base = 40

        insider_bonuses = data.get('insider_bonuses', {})
        insider_score = insider_base
        if insider_bonuses.get('recent_buying', False):
            insider_score += 20
        if insider_ownership_pct > 25:
            insider_score += 15
        insider_score = self.cap_score(insider_score, 100)

        valuation_score = (
            (ps_score * 0.60) +
            (rel_val_score * 0.25) +
            (insider_score * 0.15)
        )
        return round(valuation_score, 2)

    def tier3_quality(self, data: Dict[str, Any]) -> float:
        """
        Tier 3 Quality Score (22% weight)
        Components: Revenue Scale (18%), Profitability Path (20%), Gross Margin (22%),
                   Unit Economics (20%), Customer Quality (20%)
        """
        # Component 1: Revenue Scale (18%)
        revenue_billions = data.get('revenue_billions', 0)
        if revenue_billions > 5:
            scale_score = 100
        elif revenue_billions >= 3:
            scale_score = 85
        elif revenue_billions >= 2:
            scale_score = 75
        elif revenue_billions >= 1:
            scale_score = 60
        elif revenue_billions >= 0.5:
            scale_score = 45
        else:
            scale_score = 30

        # Component 2: Profitability Path (20%)
        is_profitable = data.get('is_profitable', False)
        op_margin = data.get('operating_margin_pct', 0)
        path_to_profit_months = data.get('path_to_profit_months', 999)

        if is_profitable:
            if op_margin > 15:
                profit_base = 100
            elif op_margin >= 10:
                profit_base = 85
            elif op_margin >= 5:
                profit_base = 70
            else:
                profit_base = 60
        else:
            if path_to_profit_months < 12:
                profit_base = 50
            elif path_to_profit_months < 24:
                profit_base = 40
            elif path_to_profit_months < 36:
                profit_base = 30
            else:
                profit_base = 15

        profit_penalties = data.get('profit_path_penalties', {})
        profit_score = profit_base
        if profit_penalties.get('burn_accelerating', False):
            profit_score -= 20
        if profit_penalties.get('no_guidance', False):
            profit_score -= 15
        if profit_penalties.get('frequent_raises', False):
            profit_score -= 10
        profit_score = self.floor_score(profit_score, 0)

        # Component 3: Gross Margin (22%)
        gross_margin = data.get('gross_margin_pct', 0)
        if gross_margin > 75:
            gross_score = 100
        elif gross_margin >= 65:
            gross_score = 90
        elif gross_margin >= 55:
            gross_score = 80
        elif gross_margin >= 45:
            gross_score = 65
        elif gross_margin >= 35:
            gross_score = 50
        else:
            gross_score = 30

        # Component 4: Unit Economics (20%)
        ltv_cac_ratio = data.get('ltv_cac_ratio', 0)

        if ltv_cac_ratio > 3:
            unit_econ_score = 100
        elif ltv_cac_ratio >= 2:
            unit_econ_score = 75
        elif ltv_cac_ratio >= 1:
            unit_econ_score = 40
        else:
            # Use proxies if LTV/CAC not available
            cac_payback_months = data.get('cac_payback_months', 999)
            gross_margin_expanding = data.get('gross_margin_expanding', False)
            cohorts_improving = data.get('cohorts_improving', False)

            if cac_payback_months < 12:
                unit_econ_score = 85
            elif gross_margin_expanding:
                unit_econ_score = 70
            elif cohorts_improving:
                unit_econ_score = 60
            else:
                unit_econ_score = 40

        # Component 5: Customer Quality (20%)
        is_saas = data.get('is_saas', False)

        if is_saas:
            nrr_pct = data.get('nrr_pct', 100)
            if nrr_pct > 125:
                customer_score = 100
            elif nrr_pct >= 115:
                customer_score = 85
            elif nrr_pct >= 105:
                customer_score = 70
            elif nrr_pct >= 95:
                customer_score = 50
            else:
                customer_score = 30
        else:
            # Non-SaaS alternatives
            concentration = data.get('top_customer_concentration_pct', 100)
            customer_growth = data.get('customer_growth_pct', 0)
            repeat_revenue = data.get('repeat_revenue_pct', 0)

            scores = []
            if concentration < 10:
                scores.append(100)
            elif concentration < 20:
                scores.append(80)
            elif concentration < 30:
                scores.append(60)
            else:
                scores.append(30)

            if customer_growth > 25:
                scores.append(100)
            elif customer_growth >= 15:
                scores.append(80)
            elif customer_growth >= 5:
                scores.append(60)
            else:
                scores.append(40)

            if repeat_revenue > 60:
                scores.append(100)
            elif repeat_revenue >= 40:
                scores.append(75)
            elif repeat_revenue >= 20:
                scores.append(50)
            else:
                scores.append(30)

            customer_score = max(scores) if scores else 50

        quality_score = (
            (scale_score * 0.18) +
            (profit_score * 0.20) +
            (gross_score * 0.22) +
            (unit_econ_score * 0.20) +
            (customer_score * 0.20)
        )
        return round(quality_score, 2)

    def tier3_growth(self, data: Dict[str, Any]) -> float:
        """
        Tier 3 Growth Score (38% weight - HIGHEST)
        Components: Revenue Growth (28%), Growth Acceleration (18%), Forward Estimates (18%),
                   TAM & Penetration (18%), Growth Driver Diversity (12%), Cyclicality (6%)
        """
        # Component 1: Revenue Growth (28%)
        ttm_growth = data.get('revenue_growth_ttm_pct', 0)
        if ttm_growth > 50:
            rev_score = 100
        elif ttm_growth >= 40:
            rev_score = 90
        elif ttm_growth >= 32:
            rev_score = 80
        elif ttm_growth >= 25:
            rev_score = 70
        elif ttm_growth >= 20:
            rev_score = 55
        elif ttm_growth >= 15:
            rev_score = 35
        else:
            rev_score = 15

        # Component 2: Growth Acceleration (18%)
        quarters_accelerating = data.get('quarters_accelerating', 0)

        if quarters_accelerating >= 4:
            accel_base = 100
            if quarters_accelerating > 4:
                accel_base += 10 * (quarters_accelerating - 4)
        elif quarters_accelerating == 3:
            accel_base = 90
        elif quarters_accelerating == 2:
            accel_base = 75
        elif ttm_growth >= 30:
            accel_base = 60
        else:
            accel_base = 30
        accel_score = self.cap_score(accel_base, 100)

        # Component 3: Forward Estimates (18%)
        forward_est = data.get('analyst_forward_growth_pct', 0)
        current_growth = ttm_growth

        if forward_est > 40:
            forward_base = 100
        elif forward_est >= 32:
            forward_base = 85
        elif forward_est >= 25:
            forward_base = 70
        elif forward_est >= 20:
            forward_base = 55
        elif forward_est >= 15:
            forward_base = 40
        else:
            forward_base = 20

        forward_score = forward_base
        if forward_est > current_growth + 8:
            forward_score += 20
        forward_score = self.cap_score(forward_score, 100)

        # Component 4: TAM & Penetration (18%)
        tam_billions = data.get('tam_billions', 0)
        penetration = data.get('market_penetration_pct', 100)

        if tam_billions > 75 and penetration < 8:
            tam_score = 100
        elif tam_billions >= 50 and penetration < 12:
            tam_score = 85
        elif tam_billions >= 30 and penetration < 15:
            tam_score = 70
        elif tam_billions >= 15 and penetration < 20:
            tam_score = 55
        else:
            tam_score = 35

        # Component 5: Growth Driver Diversity (12%)
        drivers_base = 50
        driver_bonuses = data.get('growth_driver_bonuses', {})
        drivers_score = drivers_base
        if driver_bonuses.get('multiple_segments_25plus', False):
            drivers_score += 30
        if driver_bonuses.get('geographic_expansion', False):
            drivers_score += 20
        if driver_bonuses.get('new_product_launches', False):
            drivers_score += 20
        if driver_bonuses.get('platform_effects', False):
            drivers_score += 20
        if driver_bonuses.get('viral_network', False):
            drivers_score += 15
        drivers_score = self.cap_score(drivers_score, 100)

        # Component 6: Cyclicality (6%)
        business_type = data.get('business_type', 'software')
        if business_type in ['software', 'saas', 'non_cyclical']:
            cyclical_score = 100
        elif business_type == 'early_mid_cycle_secular':
            cyclical_score = 85
        elif business_type == 'mid_cycle':
            cyclical_score = 70
        elif business_type == 'late_cycle':
            cyclical_score = 45
        else:
            cyclical_score = 25

        growth_score = (
            (rev_score * 0.28) +
            (accel_score * 0.18) +
            (forward_score * 0.18) +
            (tam_score * 0.18) +
            (drivers_score * 0.12) +
            (cyclical_score * 0.06)
        )
        return round(growth_score, 2)

    def tier3_momentum(self, data: Dict[str, Any]) -> float:
        """
        Tier 3 Momentum Score (15% weight)
        Components: 6M Return (40%), Relative Strength vs IWM (35%), Volume & Sentiment (25%)
        """
        # Component 1: 6-Month Return (40%)
        return_6m = data.get('return_6m_pct', 0)
        if return_6m > 70:
            return_score = 100
        elif return_6m >= 50:
            return_score = 90
        elif return_6m >= 30:
            return_score = 75
        elif return_6m >= 15:
            return_score = 55
        elif return_6m >= 0:
            return_score = 40
        else:
            return_score = 60  # Oversold

        # Component 2: Relative Strength vs IWM (35%)
        iwm_return_6m = data.get('iwm_return_6m_pct', 0)
        rel_perf = return_6m - iwm_return_6m

        if rel_perf > 20:
            rel_base = 100
        elif rel_perf >= 12:
            rel_base = 80
        elif rel_perf >= 5:
            rel_base = 60
        elif rel_perf >= 0:
            rel_base = 45
        else:
            rel_base = 30

        analyst_bonuses = data.get('analyst_momentum_bonuses', {})
        rel_score = rel_base
        if analyst_bonuses.get('upgrades_3plus', False):
            rel_score += 15
        if analyst_bonuses.get('price_target_raises', False):
            rel_score += 10
        rel_score = self.cap_score(rel_score, 100)

        # Component 3: Volume & Sentiment (25%)
        volume_change_pct = data.get('volume_change_pct', 0)
        sentiment_positive = data.get('sentiment_positive', False)

        sentiment_base = 50
        if volume_change_pct > 50:
            sentiment_base += 25
        elif volume_change_pct >= 25:
            sentiment_base += 15
        elif volume_change_pct < -25:
            sentiment_base -= 15

        if sentiment_positive:
            sentiment_base += 15
        if analyst_bonuses.get('analyst_momentum', False):
            sentiment_base += 15

        sentiment_score = self.cap_score(sentiment_base, 100)

        momentum_score = (
            (return_score * 0.40) +
            (rel_score * 0.35) +
            (sentiment_score * 0.25)
        )
        return round(momentum_score, 2)

    def tier3_scale_inflection(self, data: Dict[str, Any]) -> float:
        """
        Tier 3 Scale Inflection Score (10% weight)
        Components: Market Position (30%), Operating Leverage (30%),
                   Moat Formation (25%), Partnerships (15%)
        """
        # Component 1: Market Position (30%)
        company_growth = data.get('revenue_growth_ttm_pct', 0)
        sector_growth = data.get('sector_avg_growth_pct', 0)

        growth_delta = company_growth - sector_growth
        if growth_delta >= 10:
            market_pos_score = 100
        elif growth_delta >= 5:
            market_pos_score = 80
        elif growth_delta >= 0:
            market_pos_score = 60
        else:
            market_pos_score = 30

        # Component 2: Operating Leverage (30%)
        margin_expansion_bps = data.get('margin_trend_bps_per_year', 0)
        if margin_expansion_bps > 400:
            op_lev_score = 100
        elif margin_expansion_bps >= 250:
            op_lev_score = 85
        elif margin_expansion_bps >= 150:
            op_lev_score = 70
        elif margin_expansion_bps >= 100:
            op_lev_score = 55
        else:
            op_lev_score = 35

        # Component 3: Moat Formation (25%)
        moat_base = 50
        moat_bonuses = data.get('moat_formation_bonuses', {})
        moat_score = moat_base
        if moat_bonuses.get('network_effects', False):
            moat_score += 30
        if moat_bonuses.get('switching_costs', False):
            moat_score += 25
        if moat_bonuses.get('scale_advantages', False):
            moat_score += 20
        if moat_bonuses.get('data_ip_moat', False):
            moat_score += 20
        if moat_bonuses.get('brand_emerging', False):
            moat_score += 15
        moat_score = self.cap_score(moat_score, 100)

        # Component 4: Partnerships (15%)
        partnership_base = 50
        partnership_bonuses = data.get('partnership_bonuses', {})
        partnership_score = partnership_base
        if partnership_bonuses.get('major_tech_partners', False):
            partnership_score += 30
        if partnership_bonuses.get('gov_enterprise', False):
            partnership_score += 25
        if partnership_bonuses.get('critical_integrations', False):
            partnership_score += 20
        if partnership_bonuses.get('ecosystem_role', False):
            partnership_score += 15
        partnership_score = self.cap_score(partnership_score, 100)

        si_score = (
            (market_pos_score * 0.30) +
            (op_lev_score * 0.30) +
            (moat_score * 0.25) +
            (partnership_score * 0.15)
        )
        return round(si_score, 2)

    def calculate_tier3_composite(self, data: Dict[str, Any]) -> Tuple[float, Dict[str, float]]:
        """Calculate Tier 3 composite score and component breakdown"""
        v_score = self.tier3_valuation(data)
        q_score = self.tier3_quality(data)
        g_score = self.tier3_growth(data)
        m_score = self.tier3_momentum(data)
        si_score = self.tier3_scale_inflection(data)

        composite = (
            (v_score * 0.15) +
            (q_score * 0.22) +
            (g_score * 0.38) +
            (m_score * 0.15) +
            (si_score * 0.10)
        )

        components = {
            "Valuation": v_score,
            "Quality": q_score,
            "Growth": g_score,
            "Momentum": m_score,
            "Scale_Inflection": si_score
        }

        return round(composite, 2), components

    # ============================================================================
    # TIER 4: SMALL-CAP MOONSHOTS (<$10B)
    # ============================================================================

    def tier4_valuation(self, data: Dict[str, Any]) -> float:
        """
        Tier 4 Valuation Score (10% weight)
        Components: P/S (60%), Relative Valuation (25%), Insider Ownership (15%)
        """
        # Component 1: Price-to-Sales (60%)
        ps_ratio = data.get('ps_ratio', 999)
        growth_rate = data.get('revenue_growth_ttm_pct', 0)

        if ps_ratio < 12:
            ps_base = 100
        elif ps_ratio < 20:
            ps_base = 85
        elif ps_ratio < 35:
            ps_base = 70
        elif ps_ratio < 50:
            ps_base = 50
        elif ps_ratio < 75:
            ps_base = 35
        else:
            ps_base = 25

        # Growth context bonuses (higher growth = higher bonus)
        ps_score = ps_base
        if growth_rate > 75 and 35 <= ps_ratio <= 50:
            ps_score += 35
        elif growth_rate > 100 and 50 <= ps_ratio <= 75:
            ps_score += 30
        elif growth_rate > 100 and ps_ratio > 75:
            ps_score += 25
        ps_score = self.cap_score(ps_score, 100)

        # Component 2: Relative Valuation (25%)
        sector_median_ps = data.get('sector_median_ps', ps_ratio)
        ratio_to_sector = ps_ratio / sector_median_ps if sector_median_ps > 0 else 1.0

        if ratio_to_sector < 1.0:
            rel_val_score = 100
        elif ratio_to_sector <= 1.0:
            rel_val_score = 75
        elif ratio_to_sector <= 2.0:
            rel_val_score = 60
        elif ratio_to_sector <= 3.0:
            rel_val_score = 40
        else:
            rel_val_score = 20

        # Component 3: Insider Ownership (15%)
        insider_pct = data.get('insider_ownership_pct', 0)

        if insider_pct > 25:
            insider_base = 100
        elif insider_pct >= 20:
            insider_base = 90
        elif insider_pct >= 15:
            insider_base = 80
        elif insider_pct >= 10:
            insider_base = 65
        elif insider_pct >= 5:
            insider_base = 45
        else:
            insider_base = 30

        insider_bonuses = data.get('insider_bonuses', {})
        insider_score = insider_base
        if insider_bonuses.get('recent_buying', False):
            insider_score += 20
        if insider_pct > 30:
            insider_score += 20
        insider_score = self.cap_score(insider_score, 100)

        valuation_score = (
            (ps_score * 0.60) +
            (rel_val_score * 0.25) +
            (insider_score * 0.15)
        )
        return round(valuation_score, 2)

    def tier4_quality(self, data: Dict[str, Any]) -> float:
        """
        Tier 4 Quality Score (15% weight)
        Components: Gross Margin (30%), Revenue Quality (30%),
                   Unit Economics (20%), Path to Profitability (20%)
        """
        # Component 1: Gross Margin (30%)
        gross_margin = data.get('gross_margin_pct', 0)
        if gross_margin > 70:
            gross_score = 100
        elif gross_margin >= 60:
            gross_score = 85
        elif gross_margin >= 50:
            gross_score = 70
        elif gross_margin >= 40:
            gross_score = 50
        elif gross_margin >= 30:
            gross_score = 35
        else:
            gross_score = 20

        # Component 2: Revenue Quality (30%)
        rev_quality_base = 50
        recurring_pct = data.get('recurring_revenue_pct', 0)
        nrr_pct = data.get('nrr_pct', 100)
        top_customer_pct = data.get('top_customer_concentration_pct', 100)
        top_3_customers_pct = data.get('top_3_concentration_pct', 100)

        rev_quality_score = rev_quality_base
        if recurring_pct > 70:
            rev_quality_score += 30
        elif recurring_pct >= 50:
            rev_quality_score += 20

        if nrr_pct > 110:
            rev_quality_score += 20

        if top_customer_pct < 10:
            rev_quality_score += 15
        elif top_customer_pct > 50:
            rev_quality_score -= 35

        if top_3_customers_pct < 25:
            rev_quality_score += 5
        elif top_3_customers_pct > 30:
            rev_quality_score -= 20

        rev_quality_score = self.cap_score(self.floor_score(rev_quality_score, 0), 100)

        # Component 3: Unit Economics (20%)
        ltv_cac = data.get('ltv_cac_ratio', 0)

        if ltv_cac > 3:
            unit_econ_score = 100
        elif ltv_cac >= 2:
            unit_econ_score = 75
        elif ltv_cac >= 1:
            unit_econ_score = 40
        else:
            # Proxies
            cac_payback = data.get('cac_payback_months', 999)
            if cac_payback < 12:
                unit_econ_score = 85
            elif data.get('gross_margin_expanding', False):
                unit_econ_score = 70
            elif data.get('cohorts_improving', False):
                unit_econ_score = 60
            else:
                unit_econ_score = 40

        # Component 4: Path to Profitability (20%)
        is_profitable = data.get('is_profitable', False)
        path_months = data.get('path_to_profit_months', 999)

        if is_profitable:
            profit_path_base = 100
        elif path_months < 12:
            profit_path_base = 80
        elif path_months < 24:
            profit_path_base = 60
        elif path_months < 36:
            profit_path_base = 40
        elif path_months < 48:
            profit_path_base = 25
        else:
            profit_path_base = 15

        penalties = data.get('profit_path_penalties', {})
        profit_path_score = profit_path_base
        if penalties.get('burn_accelerating', False):
            profit_path_score -= 25
        if penalties.get('no_guidance', False):
            profit_path_score -= 15
        if penalties.get('frequent_raises', False):
            profit_path_score -= 10
        profit_path_score = self.floor_score(profit_path_score, 0)

        quality_score = (
            (gross_score * 0.30) +
            (rev_quality_score * 0.30) +
            (unit_econ_score * 0.20) +
            (profit_path_score * 0.20)
        )
        return round(quality_score, 2)

    def tier4_growth(self, data: Dict[str, Any]) -> float:
        """
        Tier 4 Growth Score (40% weight - HIGHEST)
        Components: Revenue Growth (28%), Growth Consistency (15%), TAM Size (15%),
                   Market Penetration (10%), Growth Driver Strength (15%),
                   Forward Estimates (12%), Catalyst Pipeline (5%)
        """
        # Component 1: Revenue Growth (28%)
        ttm_growth = data.get('revenue_growth_ttm_pct', 0)
        if ttm_growth > 100:
            rev_score = 100
        elif ttm_growth >= 75:
            rev_score = 95
        elif ttm_growth >= 55:
            rev_score = 85
        elif ttm_growth >= 40:
            rev_score = 70
        elif ttm_growth >= 30:
            rev_score = 50
        elif ttm_growth >= 20:
            rev_score = 30
        else:
            rev_score = 15

        # Component 2: Growth Consistency (15%)
        quarters_accel = data.get('quarters_accelerating', 0)

        if quarters_accel >= 5:
            consist_base = 100 + (10 * (quarters_accel - 5))
        elif quarters_accel == 4:
            consist_base = 90
        elif quarters_accel == 3:
            consist_base = 80
        elif ttm_growth >= 40:
            consist_base = 70
        else:
            consist_base = 30
        consist_score = self.cap_score(consist_base, 100)

        # Component 3: TAM Size (15%)
        tam_billions = data.get('tam_billions', 0)
        if tam_billions > 150:
            tam_score = 100
        elif tam_billions >= 100:
            tam_score = 90
        elif tam_billions >= 50:
            tam_score = 75
        elif tam_billions >= 25:
            tam_score = 55
        elif tam_billions >= 10:
            tam_score = 35
        else:
            tam_score = 20

        # Component 4: Market Penetration (10%)
        penetration_pct = data.get('market_penetration_pct', 100)
        if penetration_pct < 3:
            penetration_score = 100
        elif penetration_pct < 5:
            penetration_score = 90
        elif penetration_pct < 10:
            penetration_score = 75
        elif penetration_pct < 15:
            penetration_score = 55
        else:
            penetration_score = 35

        # Component 5: Growth Driver Strength (15%)
        drivers_base = 50
        driver_bonuses = data.get('growth_driver_bonuses', {})
        drivers_score = drivers_base
        if driver_bonuses.get('network_effects', False):
            drivers_score += 25
        if driver_bonuses.get('viral_growth_50plus', False):
            drivers_score += 25
        if driver_bonuses.get('platform_forming', False):
            drivers_score += 20
        if driver_bonuses.get('multiple_streams_35plus', False):
            drivers_score += 20
        if driver_bonuses.get('gov_enterprise_accelerating', False):
            drivers_score += 20
        drivers_score = self.cap_score(drivers_score, 100)

        # Component 6: Forward Estimates (12%)
        forward_est = data.get('analyst_forward_growth_pct', 0)
        current_growth = ttm_growth

        if forward_est > 60:
            forward_base = 100
        elif forward_est >= 50:
            forward_base = 90
        elif forward_est >= 40:
            forward_base = 80
        elif forward_est >= 30:
            forward_base = 65
        elif forward_est >= 20:
            forward_base = 45
        else:
            forward_base = 25

        forward_score = forward_base
        if forward_est > current_growth + 12:
            forward_score += 20
        forward_score = self.cap_score(forward_score, 100)

        # Component 7: Catalyst Pipeline (5%)
        catalyst_base = 50
        catalyst_bonuses = data.get('catalyst_bonuses', {})
        catalyst_score = catalyst_base
        if catalyst_bonuses.get('major_launch_6mo', False):
            catalyst_score += 30
        if catalyst_bonuses.get('market_expansion', False):
            catalyst_score += 25
        if catalyst_bonuses.get('partnership_expected', False):
            catalyst_score += 25
        if catalyst_bonuses.get('regulatory_milestone', False):
            catalyst_score += 30
        if catalyst_bonuses.get('index_inclusion', False):
            catalyst_score += 20
        catalyst_score = self.cap_score(catalyst_score, 100)

        growth_score = (
            (rev_score * 0.28) +
            (consist_score * 0.15) +
            (tam_score * 0.15) +
            (penetration_score * 0.10) +
            (drivers_score * 0.15) +
            (forward_score * 0.12) +
            (catalyst_score * 0.05)
        )
        return round(growth_score, 2)

    def tier4_momentum(self, data: Dict[str, Any]) -> float:
        """
        Tier 4 Momentum Score (15% weight)
        Components: 6M Return (40%), Relative Strength vs IWO (30%),
                   Social Sentiment (20%), Volume Surge (10%)
        """
        # Component 1: 6-Month Return (40%)
        return_6m = data.get('return_6m_pct', 0)
        if return_6m > 100:
            return_score = 100
        elif return_6m >= 70:
            return_score = 95
        elif return_6m >= 50:
            return_score = 85
        elif return_6m >= 30:
            return_score = 70
        elif return_6m >= 15:
            return_score = 50
        elif return_6m >= 0:
            return_score = 35
        else:
            return_score = 60  # Oversold

        # Component 2: Relative Strength vs IWO (30%)
        iwo_return_6m = data.get('iwo_return_6m_pct', 0)
        rel_perf = return_6m - iwo_return_6m

        if rel_perf > 30:
            rel_score = 100
        elif rel_perf >= 20:
            rel_score = 85
        elif rel_perf >= 10:
            rel_score = 65
        elif rel_perf >= 0:
            rel_score = 45
        else:
            rel_score = 25

        # Component 3: Social Sentiment (20%)
        sentiment_base = 50
        sentiment_bonuses = data.get('sentiment_bonuses', {})
        sentiment_score = sentiment_base
        if sentiment_bonuses.get('rising_mentions_bullish', False):
            sentiment_score += 25
        if sentiment_bonuses.get('positive_reddit', False):
            sentiment_score += 20
        if sentiment_bonuses.get('analyst_upgrades_3plus', False):
            sentiment_score += 25
        if sentiment_bonuses.get('target_increases', False):
            sentiment_score += 20
        if sentiment_bonuses.get('positive_media', False):
            sentiment_score += 15

        sentiment_penalties = data.get('sentiment_penalties', {})
        if sentiment_penalties.get('negative_trending', False):
            sentiment_score -= 25
        if sentiment_penalties.get('unsustainable_meme', False):
            sentiment_score -= 20

        sentiment_score = self.cap_score(self.floor_score(sentiment_score, 0), 100)

        # Component 4: Volume Surge (10%)
        volume_change_30d_vs_90d = data.get('volume_change_pct', 0)

        if volume_change_30d_vs_90d > 75:
            volume_score = 100
        elif volume_change_30d_vs_90d >= 50:
            volume_score = 85
        elif volume_change_30d_vs_90d >= 25:
            volume_score = 65
        elif abs(volume_change_30d_vs_90d) <= 25:
            volume_score = 50
        else:
            volume_score = 30

        momentum_score = (
            (return_score * 0.40) +
            (rel_score * 0.30) +
            (sentiment_score * 0.20) +
            (volume_score * 0.10)
        )
        return round(momentum_score, 2)

    def tier4_disruption(self, data: Dict[str, Any]) -> float:
        """
        Tier 4 Disruption Potential Score (20% weight)
        Components: Market Disruption (35%), Technology Moat (25%),
                   Competitive Dynamics (25%), Catalyst Pipeline (15%)
        """
        # Component 1: Market Disruption (35%)
        disruption_type = data.get('disruption_type', 'incremental')

        if disruption_type == 'attacking_100b_plus':
            disruption_score = 100
        elif disruption_type == 'creating_new_category':
            disruption_score = 95
        elif disruption_type == 'significant_share_gains':
            disruption_score = 85
        elif disruption_type == 'niche_10_50b':
            disruption_score = 70
        else:  # incremental
            disruption_score = 50

        # Component 2: Technology Moat (25%)
        tech_moat_base = 50
        tech_bonuses = data.get('tech_moat_bonuses', {})
        tech_moat_score = tech_moat_base
        if tech_bonuses.get('proprietary_ai_ml', False):
            tech_moat_score += 30
        if tech_bonuses.get('strong_patents', False):
            tech_moat_score += 25
        if tech_bonuses.get('unique_data_assets', False):
            tech_moat_score += 25
        if tech_bonuses.get('first_mover_scale', False):
            tech_moat_score += 20
        if tech_bonuses.get('unique_supply_chain', False):
            tech_moat_score += 25
        tech_moat_score = self.cap_score(tech_moat_score, 100)

        # Component 3: Competitive Dynamics (25%)
        market_structure = data.get('market_structure', 'highly_competitive')

        if market_structure == 'winner_take_most':
            comp_dyn_score = 100
        elif market_structure == 'oligopoly_forming':
            comp_dyn_score = 80
        elif market_structure == 'crowded_differentiated':
            comp_dyn_score = 60
        elif market_structure == 'highly_competitive':
            comp_dyn_score = 40
        else:  # commodity_risk
            comp_dyn_score = 20

        # Component 4: Catalyst Pipeline (15%)
        catalyst_base = 50
        catalyst_bonuses = data.get('catalyst_bonuses', {})
        catalyst_score = catalyst_base
        if catalyst_bonuses.get('major_launch_6mo', False):
            catalyst_score += 30
        if catalyst_bonuses.get('partnership_expected', False):
            catalyst_score += 25
        if catalyst_bonuses.get('market_expansion', False):
            catalyst_score += 25
        if catalyst_bonuses.get('regulatory_approval', False):
            catalyst_score += 30
        if catalyst_bonuses.get('acquisition_target', False):
            catalyst_score += 20
        catalyst_score = self.cap_score(catalyst_score, 100)

        disruption_total = (
            (disruption_score * 0.35) +
            (tech_moat_score * 0.25) +
            (comp_dyn_score * 0.25) +
            (catalyst_score * 0.15)
        )
        return round(disruption_total, 2)

    def calculate_tier4_composite(self, data: Dict[str, Any]) -> Tuple[float, Dict[str, float]]:
        """Calculate Tier 4 composite score and component breakdown"""
        v_score = self.tier4_valuation(data)
        q_score = self.tier4_quality(data)
        g_score = self.tier4_growth(data)
        m_score = self.tier4_momentum(data)
        d_score = self.tier4_disruption(data)

        composite = (
            (v_score * 0.10) +
            (q_score * 0.15) +
            (g_score * 0.40) +
            (m_score * 0.15) +
            (d_score * 0.20)
        )

        components = {
            "Valuation": v_score,
            "Quality": q_score,
            "Growth": g_score,
            "Momentum": m_score,
            "Disruption": d_score
        }

        return round(composite, 2), components

    # ============================================================================
    # MAIN CALCULATION METHOD
    # ============================================================================

    def calculate_score(self, ticker: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Main method to calculate score for any stock.
        Determines tier and calls appropriate composite calculation.
        """
        market_cap_billions = data.get('market_cap_billions', 0)
        tier = self.determine_tier(market_cap_billions)

        if tier == 1:
            composite, components = self.calculate_tier1_composite(data)
        elif tier == 2:
            composite, components = self.calculate_tier2_composite(data)
        elif tier == 3:
            composite, components = self.calculate_tier3_composite(data)
        else:  # tier == 4
            composite, components = self.calculate_tier4_composite(data)

        # Determine rating
        if composite >= 80:
            rating = "Strong Buy"
            stars = "⭐⭐⭐⭐⭐"
        elif composite >= 70:
            rating = "Buy"
            stars = "⭐⭐⭐⭐"
        elif composite >= 60:
            rating = "Hold"
            stars = "⭐⭐⭐"
        elif composite >= 50:
            rating = "Reduce"
            stars = "⭐⭐"
        else:
            rating = "Sell"
            stars = "⭐"

        # Calculate position size
        beta = data.get('beta', 1.0)
        position_size = self.calculate_position_size(tier, composite, beta)

        return {
            "ticker": ticker,
            "tier": tier,
            "tier_name": self.TIER_DEFINITIONS[tier]["name"],
            "market_cap_billions": market_cap_billions,
            "composite_score": composite,
            "rating": rating,
            "stars": stars,
            "position_size_pct": position_size,
            "min_score_for_tier": self.TIER_DEFINITIONS[tier]["min_score"],
            "score_buffer": round(composite - self.TIER_DEFINITIONS[tier]["min_score"], 2),
            "components": components,
            "beta": beta
        }

    def calculate_position_size(self, tier: int, score: float, beta: float) -> float:
        """
        Calculate position size based on tier, score, and beta.
        Uses the formulas from the specification.
        """
        base_allocations = {1: 10.0, 2: 7.0, 3: 5.0, 4: 3.0}
        vol_multipliers = {1: 0.75, 2: 1.0, 3: 1.3, 4: 1.5}

        base = base_allocations[tier]
        vol_mult = vol_multipliers[tier]

        vol_adjustment = 1 + ((beta - 1) * vol_mult)
        position = (base * (score / 100.0)) / vol_adjustment

        # Round to nearest 0.5%
        position = round(position * 2) / 2

        return position


# Example usage
if __name__ == "__main__":
    engine = ScoringEngine()

    # Example Tier 1 stock (GOOGL-like mega-cap)
    googl_data = {
        'market_cap_billions': 1800,
        'pe_ratio': 22,
        'historical_pe_avg': 25,
        'fcf_yield_pct': 4.17,
        'peg_ratio': 1.4,
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
        'revenue_cagr_3yr_pct': 11.86,
        'revenue_growth_recent_yoy_pct': 16,
        'eps_cagr_3yr_pct': 15,
        'tam_billions': 500,
        'market_share_pct': 15,
        'future_growth_bonuses': {},
        'analyst_forward_growth_pct': 12,
        'return_12m_pct': 35.2,
        'spy_return_12m_pct': 25,
        'price': 140,
        'ma_50': 135,
        'ma_200': 125,
        'net_cash_billions': 100,
        'fcf_billions': 75,
        'capital_allocation_bonuses': {
            'buybacks_rnd_gt_10pct': True,
            'value_creating_ma': True
        },
        'beta': 1.1
    }

    result = engine.calculate_score("GOOGL", googl_data)

    print("=" * 80)
    print(f"STOCK SCORE REPORT: {result['ticker']}")
    print("=" * 80)
    print(f"Tier: {result['tier']} - {result['tier_name']}")
    print(f"Market Cap: ${result['market_cap_billions']:.1f}B")
    print(f"Composite Score: {result['composite_score']} {result['stars']}")
    print(f"Rating: {result['rating']}")
    print(f"Position Size: {result['position_size_pct']}%")
    print(f"Score Buffer: {result['score_buffer']} points above minimum ({result['min_score_for_tier']})")
    print(f"\nComponent Scores:")
    for component, score in result['components'].items():
        print(f"  {component}: {score}")
    print("=" * 80)
