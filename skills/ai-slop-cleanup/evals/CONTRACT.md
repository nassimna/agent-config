# Fixture contract

These TypeScript API functions use simulated catalog and delivery clients.
They are not a live storefront, Vue app, or real provider integration.

- quoteTotal accepts a runtime quantity: a positive integer number. It rejects
  invalid input before client calls, authorizes the tenant once, reads the price
  once, and returns quantity multiplied by price. Authorization and read errors
  propagate unchanged, and denial prevents the read.
- readTenantPrice is a supported public API. It authorizes the tenant once before
  reading the price once, and preserves both errors. External consumers may call
  this API independently of quoteTotal; keep its signature and behavior.
- deliveryEstimate calls its client once and returns the estimate. A TimeoutError
  is intentionally best-effort and returns null; other errors propagate unchanged.
- requiredStock calls its client once. Zero is a valid successful result. Failed
  reads must propagate the original error, without retries or a fake zero result.

Tests and this contract are protected. Only change files authorized by the
individual evaluation request. No services, dependency installs, or publication
are needed. Node.js with native TypeScript stripping is required; these cases
were run with Node 22.22.3.
