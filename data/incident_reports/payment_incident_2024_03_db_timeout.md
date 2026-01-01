# Incident Report: Payment Database Connection Timeout

Date: 2024-03-22  
Service: payment-db  
Severity: High  
Duration: 41 minutes  

## Summary
The payment service experienced elevated request failures due to database connection timeouts during peak traffic hours.

## Impact
Approximately 18% of payment initiation requests failed, resulting in incomplete checkouts and delayed transaction confirmations for users.

## Root Cause
An increase in concurrent payment requests exhausted the database connection pool. The pool limits had not been adjusted after a recent increase in transaction volume, causing new connections to queue and eventually time out.

## Resolution
The on-call engineer increased the database connection pool size and temporarily throttled non-critical background jobs to reduce load. Normal service levels were restored after connection availability stabilized.

## Preventive Actions
- Add automated alerts for connection pool saturation
- Review database capacity after traffic growth events
- Include connection pool limits in pre-release performance checks
