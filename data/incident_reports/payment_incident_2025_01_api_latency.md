# Incident Report: Payment API Latency Regression

Date: 2025-01-08  
Service: payment-api  
Severity: Medium  
Duration: 46 minutes  

## Summary
The payment API experienced a latency regression that caused delayed transaction responses without a corresponding increase in error rates.

## Impact
Approximately 22% of payment requests exceeded the acceptable response time threshold, resulting in slow checkouts and user retries during the incident period.

## Root Cause
A configuration change increased synchronous logging within the request processing path. Under peak load, the additional I/O operations significantly increased request processing time.

## Resolution
Synchronous logging was disabled for latency-sensitive code paths and replaced with asynchronous batching. Latency metrics returned to normal shortly after the change.

## Preventive Actions
- Audit latency impact of logging changes before deployment
- Establish performance budgets for synchronous operations
- Add alerts for p95 latency regressions
