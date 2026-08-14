# Rivora — Project Requirements Document (PRD)

| | |
|---|---|
| **Product** | Rivora — Marketplace for Everyone |
| **Type** | Multi-vendor e-commerce platform |
| **Owner** | Anoop George |
| **Status** | Draft — v0.1 |
| **Last updated** | 2026-08-14 |

---

## 1. Overview

Rivora is a multi-vendor e-commerce marketplace where independent vendors list and sell products across multiple categories (groceries, fashion, electronics, general retail, accessories) to buyers, under a single platform brand. The platform is built as a Turborepo monorepo with independently deployable portals for each user role, backed by a single PostgreSQL source of truth.

### 1.1 Goals
- Give independent vendors a low-friction way to list, sell, and manage products without building their own storefront.
- Give buyers a trustworthy, single place to discover and purchase from many vendors, with one unified checkout, tracking, and support experience.
- Give the platform operator (admin) full control over quality, trust, and monetization (commission-based revenue).
- Build the system with deep, from-first-principles understanding rather than black-box abstractions — this is a learning-driven build as much as a product build.

### 1.2 Non-goals (for v1)
- No AI-generated code in the codebase (AI is used for concept understanding only, not for shipping generated code directly).
- No multi-currency / international tax compliance in v1 — single-region launch first.
- No native mobile app for vendors/admin in v1 — React Native/Expo is scoped to the buyer-facing storefront only, unless stated otherwise.

---

## 2. User Personas / Roles

| Role | Description | Primary Portal |
|---|---|---|
| **Buyer** | End customer browsing and purchasing products | Storefront (Next.js/Vite + Expo mobile) |
| **Vendor** | Independent seller listing and fulfilling products | Vendor Portal |
| **Admin** | Platform operator — approvals, oversight, configuration | Admin Portal |
| **Developer** | Engineer/contributor with codebase access, granted per-task by Admin | Developer Portal |

---

## 3. System Architecture Overview

- **Structure:** Turborepo monorepo — `apps/{admin, backend, dev, storefront, vendor}`, shared `packages/`, root-level `docker/`, `docs/`.
- **Frontend:** Next.js / Vite per portal, deployed independently on Vercel. GSAP for subtle animation; lightweight internal design system built before per-feature Figma work.
- **Mobile:** React Native / Expo (buyer-facing).
- **Backend:** FastAPI, async SQLAlchemy 2.0, single PostgreSQL database as source of truth, Redis for caching/session/token state.
- **Auth:** Custom Google OAuth implementation (AsyncSQLAlchemy + Redis + PyJWT), built from scratch for protocol-level understanding rather than using a managed provider.
- **Package management:** UV (Python), monorepo-managed JS deps.
- **Containerization / Deploy:** Docker, Render (backend), Vercel (frontend apps).
- **CI/CD:** GitHub Actions — separate `ci.yml` and `backend-cd.yml`, chained via `workflow_run`, with `workflow_dispatch` for manual deploy testing.
- **Architecture style:** Feature-based vertical slice architecture per app.
- **Documentation:** Per-app `README.md` + root `docs/ARCHITECTURE.md` + short ADRs in `docs/adr/`.

---

## 4. Functional Requirements

Priority key: **P0** = required for launch, **P1** = important, near-term, **P2** = future/nice-to-have.

### 4.1 Storefront / Buyer Portal

| ID | Requirement | Priority | Notes |
|---|---|---|---|
| BUY-01 | Browse products by category | P0 | Categories admin-managed (see ADM-04) |
| BUY-02 | Search products with filters (price, rating, vendor, availability) | P0 | Needed before v1 launch — category-only browsing doesn't scale |
| BUY-03 | View product detail page | P0 | Includes vendor info, stock, reviews |
| BUY-04 | Add to Wishlist / remove from Wishlist | P1 | |
| BUY-05 | Add to Cart | P0 | Cart may contain items from multiple vendors |
| BUY-06 | Buy Now (direct checkout, bypass cart) | P1 | |
| BUY-07 | Checkout splits multi-vendor cart into per-vendor sub-orders | **P0 — core requirement** | Each sub-order has its own fulfillment, shipping, and payout tracking. See §6. |
| BUY-08 | Payment via payment gateway | P0 | Gateway TBD — see §8 |
| BUY-09 | Order confirmation + notification | P0 | |
| BUY-10 | Order tracking / status monitoring | P0 | |
| BUY-11 | Order history | P0 | |
| BUY-12 | Cancel order (pre-shipment) | P1 | |
| BUY-13 | Return / refund request (post-delivery) | P1 | Routed to vendor, escalates to admin if unresolved |
| BUY-14 | Leave product review & rating (post-delivery) | P1 | Closes the trust loop; currently vendors receive feedback with no visible buyer-side origin |
| BUY-15 | Apply coupon/discount code at checkout | P1 | |
| BUY-16 | Manage saved addresses | P1 | |
| BUY-17 | Guest checkout | P2 | Reduces first-purchase friction |
| BUY-18 | Notifications (order placed/shipped/delivered, price drops) | P1 | |

### 4.2 Vendor Portal

| ID | Requirement | Priority | Notes |
|---|---|---|---|
| VEN-01 | Vendor signup | P0 | |
| VEN-02 | KYC / business verification | P0 | Required before Admin approval |
| VEN-03 | Admin approval before vendor is active | P0 | Trust/quality gate |
| VEN-04 | Add product (with branding) | P0 | |
| VEN-05 | Edit product | P0 | |
| VEN-06 | Remove product | P0 | |
| VEN-07 | Product publish requires admin approval | P0 | Quality control gate |
| VEN-08 | Inventory / stock management | P0 | Prevents overselling |
| VEN-09 | Order management — view, pack, ship, mark delivered | **P0 — currently missing** | Without this, vendor cannot fulfill sales |
| VEN-10 | Payout & settlement dashboard (commission rate, pending balance, transaction history, invoices) | P0 | Replaces vague "earn money" concept |
| VEN-11 | Analytics (sales, traffic, conversion) | P1 | |
| VEN-12 | View feedback / ratings / reviews / comments | P1 | |
| VEN-13 | Create discounts / coupons | P2 | |
| VEN-14 | Respond to disputes | P1 | Vendor-side input before admin escalation |
| VEN-15 | Bulk product upload (CSV) | P2 | |

### 4.3 Admin Portal

| ID | Requirement | Priority | Notes |
|---|---|---|---|
| ADM-01 | Add / remove / edit admins | P0 | |
| ADM-02 | Vendor approval queue (approve / reject / suspend) | P0 | |
| ADM-03 | Product verification & publish approval | P0 | |
| ADM-04 | Category / taxonomy management | P1 | |
| ADM-05 | Order & dispute oversight | P0 | Escalation point for unresolved buyer↔vendor disputes |
| ADM-06 | Commission & fee configuration | P0 | Drives vendor payout math |
| ADM-07 | Stats & analytics (platform-wide) | P1 | |
| ADM-08 | System logs — critical, error, warning | P1 | Operational health |
| ADM-09 | Performance & feedback monitoring | P1 | |
| ADM-10 | System overview (admin, backend, storefront, vendor, hosting, DB status) | P2 | Leans more DevOps than business admin — evaluate whether this belongs in a separate internal tool |
| ADM-11 | Homepage CMS (banners, featured products) | P2 | Merchandising control |
| ADM-12 | Admin action audit log | P1 | Distinct from system logs — tracks who approved/changed what |
| ADM-13 | Developer access request review queue | P0 | See §4.4 |

### 4.4 Developer Portal (Internal access-governance tool)

| ID | Requirement | Priority | Notes |
|---|---|---|---|
| DEV-01 | Admin assigns Developer role to a user | P0 | No self-service escalation |
| DEV-02 | Developer submits access request (scope + justification) | P0 | e.g. "write access to fix OAuth clock skew bug" |
| DEV-03 | Admin reviews and approves/denies request | P0 | |
| DEV-04 | On approval, system grants time-boxed GitHub repo access via GitHub API | P0 | `expires_at` required — no permanent grants |
| DEV-05 | Auto-revoke access on expiry or task completion | P0 | Closes the most common real-world access-control gap |
| DEV-06 | Branch protection + CODEOWNERS enforced on `main` | P0 | GitHub has no native folder-level permission — this is the real enforcement boundary |
| DEV-07 | Two-person approval for sensitive scopes (payments, auth) | P1 | Separation of duties |
| DEV-08 | Public API for third-party developer integrations | P2 | Distinct from internal codebase access — requires API key management, rate limiting, docs |

---

## 5. Non-Functional Requirements

| Category | Requirement |
|---|---|
| **Security** | JWT-based auth, least-privilege access for all roles, time-boxed elevated access for developers, no AI-generated code merged without review |
| **Auditability** | Admin actions logged separately from system/error logs |
| **Scalability** | Independent deploys per app (Vercel) so one portal's traffic doesn't affect another; backend stateless where possible to scale horizontally on Render |
| **Observability** | Structured logging (critical/error/warning tiers), plus feedback/performance monitoring |
| **Data integrity** | Single Postgres source of truth; Redis used only for cache/session/ephemeral state, never as system of record |
| **Reliability** | CI must pass (tests + lint) before deploy; `backend-cd.yml` gated behind `ci.yml` via `workflow_run` |
| **Documentation** | Every architectural decision recorded as a short ADR in `docs/adr/` |

---

## 6. Core Design Decision: Multi-Vendor Order Splitting

This is the most consequential technical decision in the system and should be finalized before checkout is built.

- A **Cart** may contain items from multiple vendors.
- On checkout, the Cart resolves into a single **Order** (buyer-facing, one payment) which contains one or more **VendorSubOrders**.
- Each `VendorSubOrder` has its own status (packed/shipped/delivered), shipping cost, and commission calculation — independent of the others.
- Payment is captured once at the Order level; payout is calculated and disbursed per `VendorSubOrder` based on the commission rule active at time of sale (see ADM-06).
- Refunds/returns are scoped to a `VendorSubOrder`, not the whole Order — a buyer can return one vendor's item without affecting the rest of the order.

**Suggested core entities:** `User`, `Vendor`, `Product`, `Cart`, `CartItem`, `Order`, `VendorSubOrder`, `Payment`, `Payout`, `Review`, `DeveloperAccessRequest`.

---

## 7. Integrations

| Integration | Purpose | Status |
|---|---|---|
| Google OAuth | Buyer/vendor/admin login | Implemented (clock skew fix pending deploy) |
| Payment gateway | Checkout payment capture | **Not yet decided** — open question |
| GitHub API | Developer access grant/revoke | Planned |
| Email/Push provider | Notifications | Not yet decided |

---

## 8. Open Questions

1. Which payment gateway (Stripe, Razorpay, PayPal, etc.) — depends on target launch region.
2. Is the "system overview" admin feature (ADM-10) part of this product, or a separate internal ops dashboard?
3. Is the public developer API (DEV-08) in scope for v1, or a v2 goal once the platform has real vendor traffic?
4. Commission model: flat %, per-category %, or tiered by vendor volume?
5. Launch region and associated tax/compliance requirements.

---

## 9. Phased Roadmap (draft)

| Phase | Scope |
|---|---|
| **Phase 1 — Core Marketplace** | Auth, vendor onboarding + approval, product CRUD + approval, storefront browse/search, single-vendor cart/checkout |
| **Phase 2 — Multi-Vendor Order System** | Cart splitting, VendorSubOrder model, vendor order management, payout dashboard |
| **Phase 3 — Trust & Engagement** | Reviews/ratings, returns/refunds, disputes, notifications |
| **Phase 4 — Growth Tools** | Coupons/discounts, homepage CMS, analytics, search relevance tuning |
| **Phase 5 — Platform Extensibility** | Developer access-governance workflow, public API |

---

## 10. Appendix

- Related ADRs: `docs/adr/0001-custom-oauth-vs-clerk.md`, `docs/adr/0002-vertical-slice-architecture.md` (add new ADRs as decisions in §8 are resolved)
- Architecture reference: `docs/ARCHITECTURE.md`
- Diagrams: Eraser workspace — "Rivora - E commerce"

