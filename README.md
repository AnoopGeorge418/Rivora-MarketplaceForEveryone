# Rivora - Marketplace for Everyone

Rivora is a full-stack, multi-vendor ecommerce platform built to give anyone — individual sellers, small businesses, and established vendors alike — a place to reach customers, without the complexity or gatekeeping of traditional marketplaces.

## ✨ Highlights

- 🔐 **Full OAuth2 + JWT auth** — Google OAuth and credential-based login with role-based access control across four distinct portals
- 🏪 **Multi-vendor architecture** — vendors manage their own catalog and orders independently, with admin-level moderation and oversight
- ⚡ **SEO-optimized storefront** — Next.js-powered customer experience built for performance and discoverability
- 🧩 **Monorepo architecture** — Turborepo-powered, with independently deployable apps and a shared design system + typed API client
- 🐳 **Production-style infra** — Dockerized services, async SQLAlchemy, Alembic migrations, and CI/CD via GitHub Actions

## 👥 Roles

| Role | Description |
|------|-------------|
| **Customer** | Browses and purchases across a diverse, multi-vendor catalog via a fast, SEO-optimized storefront |
| **Vendor** | Manages their own products, inventory, and orders through a dedicated vendor panel |
| **Admin** | Oversees platform-wide moderation, vendor approval, and operational health |
| **Developer** | Integrates with Rivora through a dedicated API and developer portal |

## 🏗️ Architecture & Stack

**Backend**
- `FastAPI` · async `SQLAlchemy` · `PostgreSQL` (Neon) · `Redis` · `Alembic`
- Deployed independently on `Render`

**Frontend**
- `Turborepo` monorepo
- `Next.js` — customer storefront (SEO-critical)
- `React` + `Vite` — admin, vendor, and developer panels
- Deployed on `Vercel`

**Auth**
- OAuth2 (Google) + credential-based login
- `JWT`-based sessions with role-based access control across all portals

**Infrastructure**
- `Docker` containerized services
- `GitHub Actions` CI/CD
- Shared component library and typed API client across all frontend apps

## 📌 Why Rivora

Rivora reflects real-world ecommerce platform architecture — role-based multi-tenancy, independently deployable services, and a scalable monorepo structure — built as a hands-on deep dive into production-grade backend and full-stack system design.

---

<p align="center">Built as a deep-dive into full-stack architecture, from database schema to deployment.</p>

## 🧑‍💻 About the Developer

Built with passion and a lot of late-night debugging by **Anoop George** — a freelance full-stack developer specializing in backend architecture, scalable APIs, and production-grade system design.

Rivora showcases the kind of end-to-end thinking I bring to client projects — from database schema and auth architecture to multi-role platforms and deployment pipelines.

Open to freelance backend/full-stack work — let's build something solid together.

- GitHub / YouTube / Discord / Medium: [@AnoopGeorge418](https://github.com/AnoopGeorge418)

<p align="center">✨ Made with curiosity, coffee, and a genuine love for backend engineering ✨</p>
