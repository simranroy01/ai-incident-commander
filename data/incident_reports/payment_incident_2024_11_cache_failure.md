# Incident Report: Payment Cache Invalidation Failure

Date: 2024-11-04  
Service: payment-cache  
Severity: Medium  
Duration: 33 minutes  

## Summary
The payment service experienced elevated error rates due to failures in the cache layer responsible for storing session-level payment data.

## Impact
Approximately 11% of payment attempts failed as stale or missing cache entries caused request processing errors, particularly for repeat checkout attempts.

## Root Cause
A cache eviction policy change caused frequent invalidation of active payment session keys. The issue led to increased cache misses and fallback logic failures under load.

## Resolution
The eviction policy was reverted to the previous configuration and cache nodes were restarted to clear inconsistent entries. Error rates returned to baseline shortly after stabilization.

## Preventive Actions
- Validate cache eviction changes under realistic load
- Add monitoring for cache hit-to-miss ratios
- Improve fallback handling for missing session
