# Incident Report: Payment API Rate Limiting Triggered by Traffic Surge

Date: 2024-09-17  
Service: payment-api  
Severity: Medium  
Duration: 54 minutes  

## Summary
A sudden increase in payment initiation requests caused the payment API rate limiter to activate more aggressively than expected, resulting in rejected requests.

## Impact
Approximately 14% of payment requests were blocked with rate-limit responses, leading to temporary checkout failures for a portion of users.

## Root Cause
A promotional campaign triggered a spike in concurrent requests that exceeded the configured rate limit thresholds. The limits were based on historical averages and did not account for burst traffic patterns.

## Resolution
Rate limit thresholds were temporarily increased and traffic was redistributed across additional API instances. Normal request acceptance resumed once traffic stabilized.

## Preventive Actions
- Adjust rate limit policies to support burst traffic
- Introduce adaptive rate limiting based on real-time load
- Coordinate traffic modeling before marketing campaigns
