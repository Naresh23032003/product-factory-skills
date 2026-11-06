---
name: security-scanning
description: Use when checking a repo for leaked secrets or keys, vulnerable dependencies, unsafe GitHub Actions workflows or LLM-app risks, and when deciding what to do about a finding. Covers free scanners and triage rules.
---

# Security scanning and triage

## Layers (all free)
| Layer | Where | Tool | Catches |
|---|---|---|---|
| Stop leaks at push | GitHub, public repos | Secret scanning and push protection | Known-format keys before they land |
| Every PR | Repo CI | Gitleaks, OSV-Scanner (PR mode), diff review | Secrets and vulnerable dependencies in the diff |
| Scheduled, all repos | A nightly workflow | Gitleaks (full history, `--redact`), TruffleHog (verified only), OSV-Scanner, zizmor | Old leaks, live keys, new advisories, workflow flaws |
| Continuous | GitHub, public repos | Dependabot alerts and security updates, CodeQL default setup | New CVEs in dependencies, code-level bugs |

Why two secret scanners: Gitleaks is fast pattern matching that flags things that *look* like
credentials. TruffleHog checks whether a credential is *still live* against its service. A
verified TruffleHog hit is an incident; a Gitleaks hit is a lead.

## Triage rules
1. Confirm before reporting: open the file at that commit and decide true or false positive with
   one line of evidence.
2. Severity order: live secret, then critical or high dependency advisory reachable from app code,
   then workflow template injection or an over-broad token, then everything else.
3. **Leaked secret**: rotate first (in the provider's console), then remove it from the code and
   read it from an environment variable. Rewriting git history (git filter-repo) is irreversible
   and needs its own sign-off; rotation makes the old value worthless anyway.
4. **Dependency advisory**: upgrade to the first fixed version. If none exists, record the reason
   and check whether the vulnerable function is reachable.
5. **Workflows**: pin third-party actions to a full commit SHA, set `permissions:` to the least
   needed, use `persist-credentials: false` on checkout, never interpolate `${{ github.event.* }}`
   into `run:` (pass it through an env var), and treat issue and PR text as untrusted input for
   any AI agent step.
6. Record false positives in a baseline file as `{fingerprint, repo, reason}`. Never silence a
   finding without a reason.

## LLM apps: OWASP Top 10 for LLM Applications 2025
LLM01 prompt injection, LLM02 sensitive information disclosure, LLM03 supply chain, LLM04 data and
model poisoning, LLM05 improper output handling, LLM06 excessive agency, LLM07 system prompt
leakage, LLM08 vector and embedding weaknesses, LLM09 misinformation, LLM10 unbounded
consumption. A minimum bar for an app that takes money: provider keys only on the server, per-user
rate and spend limits (LLM10), model output treated as untrusted before it reaches HTML, SQL,
shells or tools (LLM05), tools run with least privilege and a human confirmation for destructive
actions (LLM06), and no secrets in system prompts (LLM07).

## Repo baseline (add with the first PR to any app repo)
- A workflow on pull requests running the Gitleaks and OSV-Scanner PR scans.
- `.gitignore` covering `.env*`; `.env.example` lists variable names only.
- A `SECURITY.md` explaining how to report a problem (GitHub private vulnerability reporting).

## Never
Print, paste or commit a secret value, even partially. Refer to findings by detector, file and
line. Do not test a found credential against its service yourself. Do not disable a scanner to
make CI pass.

## Sources
- Gitleaks: https://github.com/gitleaks/gitleaks
- TruffleHog: https://github.com/trufflesecurity/trufflehog
- Gitleaks vs TruffleHog: https://appsecsanta.com/secret-scanning-tools/gitleaks-vs-trufflehog
- OSV-Scanner GitHub Action: https://google.github.io/osv-scanner/github-action/
- zizmor: https://github.com/zizmorcore/zizmor
- OWASP Top 10 for LLM Applications 2025: https://genai.owasp.org/2024/11/17/owasp-reveals-updated-2025-top-10-risks-for-llms-announces-new-llm-project-sponsorship-program-and-inaugural-sponsors/
- OWASP ASVS: https://owasp.org/www-project-application-security-verification-standard/
