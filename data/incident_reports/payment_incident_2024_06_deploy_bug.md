# Incident Report: Payment Request Validation Failure After Deployment

Date: 2024-06-09  
Service: payment-api  
Severity: High  
Duration: 27 minutes  

## Summary
A production deployment introduced a request validation failure in the payment API, causing a subset of legitimate payment requests to be rejected.

## Impact
Roughly 9% of payment attempts returned client-side validation errors, preventing affected users from completing transactions during the incident window.

## Root Cause
A schema validation change incorrectly marked an optional payment metadata field as required. The issue was not detected in staging because traffic samples did not include the affected request variant.

## Resolution
The deployment was rolled back to the previous stable version and the validation schema was corrected. A hotfix was deployed after additional request pattern testing.

## Preventive Actions
- Expand staging test coverage to include diverse request payloads
- Introduce schema compatibility checks during deployment
- Require canary releases for validation-related changes
